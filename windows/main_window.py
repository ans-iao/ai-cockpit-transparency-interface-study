import random

from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtCore
import config as cfg
from views import MenuView, QuestionnaireView, PlainTextView, ImageView, ControlQuestionView, EndView, MixedView
import csv
from database import questionnaires as quest
from collections import deque
from database import plain_text
from database import scenarios as db_scenarios
import json
import os
from datetime import datetime
from pylsl import StreamInlet
from helpers import LSLRecorder


class MainWindow(QMainWindow):
    """
    Main window class that manages the experimental flow and questionnaire presentation.

    This class handles:
    - Experiment initialization and participant group/role assignment
    - Questionnaire presentation and data collection
    - Eye tracking data recording via LSL
    - Scenario and transparency interface presentation
    - Results saving to CSV files

    The window is created as a frameless window of fixed size defined in config.
    Various views (menu, questionnaires, text, images) are presented as central widgets.
    The experimental flow is managed through a queue system.
    """
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setFixedSize(QtCore.QSize(cfg.w_width, cfg.w_height))

        self.group = None
        self.role = None
        self.scenarioOrder = None
        self.pmOrder = None
        self.quest_dir = None

        # load config json file
        with open("config.json") as json_file:
            self.json_data = json.load(json_file)

        self.menu_view = MenuView(self, int(self.json_data["last_subj"]) + 1)
        self.setCentralWidget(self.menu_view)

        self.queue = deque()

        self.results_dict = {}
        self.current_ti_list = None
        self.current_ti_ind = 0
        self.recorder = None

    def start(self, subj_id, stream=None):
        """Initialize and start the experiment for a participant.

        Parameters
        ----------
        subj_id : str
            The unique identifier for the participant
        stream : pylsl.StreamInfo or None
            LSL stream object for eye tracking data recording. If None, eye tracking
            is disabled

        Notes
        -----
        This method:
        - Updates the config.json with the new subject ID
        - Determines questionnaire type and role from participants_randomized.csv
        - Creates subject directory and files for data saving
        - Initializes LSL recorder if stream is provided
        - Sets up the experimental flow queue with appropriate views
        """
        # Save config json file
        with open("config.json", "w") as outfile:
            self.json_data["last_subj"] = str(subj_id)
            json.dump(self.json_data, outfile)
        print("config.json updated")

        # Determine questionnaire type and role by file
        with open("participants_randomized.csv", mode="r") as file:
            csv_file = csv.reader(file)
            for lines in csv_file:
                if lines[0] == subj_id:
                    self.group = lines[1]
                    self.role = lines[2]
                    self.scenarioOrder = lines[3:7]
                    self.pmOrder = lines[7:]
                    break

        print(self.scenarioOrder)
        print(self.pmOrder)

        # Create subject directory
        save_path = os.path.join(cfg.save_dir, f"{int(subj_id):02}")
        if not os.path.isdir(save_path):
            os.makedirs(save_path)

        # Create subject questionnaire csv file
        now = datetime.now()
        date_code = now.strftime("%Y%m%d%H%M%S")  # Format as a date code string

        self.quest_dir = os.path.join(save_path,
                                      f"subj-{int(subj_id):02}_group-{self.group}_role-{self.role}_questionnaires_{date_code}.csv")
        with open(self.quest_dir, "w", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(["Code", "Value"])
            writer.writerow(["Group", self.group])
            writer.writerow(["Role", "1" if self.role == "Operator" else "2"])

        # Create LSL recorder
        if stream:
            inlet = StreamInlet(stream)
            lsl_save_dir = os.path.join(save_path,
                                        f"subj-{int(subj_id):02}_group-{self.group}_role-{self.role}_eye_tracking_{date_code}.csv")
            self.recorder = LSLRecorder(inlet, lsl_save_dir)
            self.recorder.start()

        """ Initialize view orders """
        group_content = plain_text.intro_group[self.group]
        self.queue.append(
            PlainTextView(self, plain_text.intro_group["instr"], group_content["header"], group_content["desc"]))

        if self.group == "1":
            self.init_pm_survey()
        self.init_role()
        self.init_scenario()
        if self.group == "2":
            self.init_pm_survey()
        self.init_demographic()

        self.next()

    def next(self):
        """
        Advance to the next view in the experimental flow queue.

        This method manages the progression through different views in the experiment by:
        1. Taking the next view from the queue
        2. Handling special cases for lists of views (transparency interface texts)
        3. Managing eye tracking markers if recording is active
        4. Displaying the end view when queue is empty
        5. Saving questionnaire results if available

        Notes
        -----
        - If the next item is a list, it's treated as a transparency interface text sequence
        - Updates eye tracking markers for each new view if recording is enabled
        - Saves any pending questionnaire results before proceeding
        - Shows end screen when queue is empty

        See Also
        --------
        next_text : Handles navigation through transparency interface texts
        append_quest_csv : Saves questionnaire results to CSV
        """
        if len(self.queue) > 0:
            view = self.queue.popleft()
            if isinstance(view, list):
                self.current_ti_list = view
                self.current_ti_ind = -1
                self.next_text(1)
            else:
                if self.recorder:
                    self.recorder.change_marker(view.get_view_type())
                self.setCentralWidget(view)
        else:
            view = EndView(self, "Vielen Dank!", "Bitte wenden Sie sich an die Versuchsleitung")
            if self.recorder:
                self.recorder.change_marker(view.get_view_type())
                self.recorder.end_run()
                self.recorder.join()
            self.setCentralWidget(view)

        if self.results_dict:
            self.append_quest_csv()

    def next_text(self, direction):
        """Navigate through transparency interface text screens.

        This method handles navigation between different transparency interface text screens
        by updating the current index and creating appropriate ImageViews.

        Parameters
        ----------
        direction : int
            Direction of navigation:
                1 = forward
                -1 = backward

        Notes
        -----
        - Updates current_ti_ind based on direction
        - Creates ImageView with parameters from current_ti_list
        - Updates eye tracking marker if recorder is active
        - Sets the new view as central widget

        The current_ti_list contains lists of parameters for each view:
        [file_path, ti_type, forward_enabled, backward_enabled, next_button_enabled]
        """
        self.current_ti_ind += direction
        view = ImageView(self,
                         self.current_ti_list[self.current_ti_ind][0],
                         ti_type=self.current_ti_list[self.current_ti_ind][1],
                         forward=self.current_ti_list[self.current_ti_ind][2],
                         backward=self.current_ti_list[self.current_ti_ind][3],
                         next_button=self.current_ti_list[self.current_ti_ind][4])
        if self.recorder:
            self.recorder.change_marker(view.get_view_type())

        self.setCentralWidget(view)

    def set_questionnaire_result(self, res):
        """Update questionnaire results and advance to next view.

        Parameters
        ----------
        res : dict
            Dictionary containing questionnaire results to be added to results_dict.
            Keys are question identifiers and values are participant responses.

        Notes
        -----
        This method:
        1. Updates the internal results dictionary with new questionnaire responses
        2. Prints the updated results dictionary for debugging
        3. Advances to the next view in the experimental flow

        The results are later saved to CSV when advancing to the next view.
        """
        self.results_dict.update(res)
        print(self.results_dict)
        self.next()

    def init_pm_survey(self):
        """Initialize and queue personality measurement survey views.

        This method sets up the personality measurement questionnaire views in the experiment 
        queue. It handles both single-part and split questionnaires (BFI and ATI).

        Notes
        -----
        For BFI and ATI questionnaires:
        - Questions are randomly split into two parts
        - Each part is presented separately to reduce cognitive load

        For other questionnaires:
        - Questions are presented in a single view

        The method performs the following steps:
        1. Adds introduction text view
        2. For each questionnaire in pmOrder:
            - If BFI or ATI: splits into two parts and creates two views
            - Otherwise: creates single questionnaire view
        3. All questionnaire views are shuffled and use scale display optimization

        See Also
        --------
        QuestionnaireView : View class for presenting questionnaires
        PlainTextView : View class for presenting text instructions
        """
        self.queue.append(
            PlainTextView(self, plain_text.intro_quest["instr"], plain_text.intro_quest["header"],
                          plain_text.intro_quest["desc"]))

        for pm in self.pmOrder:
            if pm in ["bfi", "ati"]:
                keys = list(quest.questionnaires[pm]["questions"].keys())
                random.shuffle(keys)
                divider = int(len(keys) / 2)
                part_1 = keys[:divider]
                part_2 = keys[divider:]
                dict_1 = {"header": "Inwieweit treffen die folgenden Aussagen auf Sie zu?", "questions": {}}
                dict_2 = {"header": "Inwieweit treffen die folgenden Aussagen auf Sie zu?", "questions": {}}
                for key in part_1:
                    dict_1["questions"][key] = quest.questionnaires[pm]['questions'][key]
                for key in part_2:
                    dict_2["questions"][key] = quest.questionnaires[pm]['questions'][key]

                self.queue.append(
                    QuestionnaireView(self, dict_1, shuffle=True, display_scale_once=True))
                self.queue.append(
                    QuestionnaireView(self, dict_2, shuffle=True, display_scale_once=True))

            else:
                self.queue.append(
                    QuestionnaireView(self, quest.questionnaires[pm], shuffle=True, display_scale_once=True))

    def init_role(self):
        """Initialize and queue role-specific content and questionnaire views.

        This method sets up the experimental views related to the participant's assigned role 
        (User or Operator). It adds role description and control items to the view queue.

        The method performs the following steps:
        1. Gets role-specific content from plain_text.role_desc
        2. Creates and queues a MixedView with role description and control items
        3. For Operator role only: adds an additional control item questionnaire

        See Also
        --------
        MixedView : Combined text and questionnaire view
        QuestionnaireView : View for presenting questionnaires
        """
        # Role Description
        role_content = plain_text.role_desc[self.role]
        # self.queue.append(
        #     PlainTextView(self, plain_text.role_desc["instr"], role_content["header"], role_content["desc"]))

        # Control-Item
        mixed = MixedView(self, "", plain_text.role_desc["instr"], role_content["header"], role_content["desc"],
                          quest.questionnaires["cir"])
        self.queue.append(mixed)

        if self.role == "Operator":
            self.queue.append(
                QuestionnaireView(self, quest.questionnaires["cir_o"], shuffle=False, display_scale_once=True))

    def init_scenario(self):
        """Initialize and queue scenario-related views and questionnaires.

        This method sets up the experimental flow for each scenario by creating and queueing
        appropriate views in sequence. For each scenario in scenarioOrder, it creates:

        - Mixed view with scenario context and control items
        - Pre-survey questionnaires
        - Eye tracker recalibration prompt
        - Transparency interface texts for different system aspects
        - Control questions
        - Post-survey questionnaires

        Notes
        -----
        The method follows this sequence for each scenario:
        1. Present scenario context and initial control items
        2. Conduct pre-survey (perceived control, trust, reliability)
        3. Recalibrate eye tracker
        4. Show transparency interface texts for:
           - System goals
           - System type
           - Data handling
           - Control mechanisms
        5. Present control questions
        6. Conduct post-survey (system perception, trust, fairness)

        The transparency interface texts are presented in three levels/pages each,
        tracked by eye tracking markers as defined in README.md.
        
        """
        header = db_scenarios.scenarios["Header"]

        for s in self.scenarioOrder:
            # Contextualization scenario and AI System
            target_scenario = db_scenarios.scenarios[s]

            mixed = MixedView(self, target_scenario["Title"], header, "", target_scenario[self.role],
                              quest.questionnaires["cis"], scenario_id=s)
            self.queue.append(mixed)

            # Pre-survey
            role_string = "End-User" if self.role == "User" else "Überwachende Person"
            self.queue.append(PlainTextView(self, plain_text.post_survey["instr"], plain_text.post_survey["header"],
                                            plain_text.post_survey["desc"].format(role=role_string)))

            self.queue.append(
                QuestionnaireView(self, quest.questionnaires["pc_pre"], scenario_id=s, shuffle=True,
                                  display_scale_once=True))

            self.queue.append(QuestionnaireView(self, quest.questionnaires["a1"], scenario_id=s, shuffle=False,
                                                display_scale_once=True))
            self.queue.append(
                QuestionnaireView(self, quest.questionnaires["trust"], scenario_id=s,
                                  shuffle=True, display_scale_once=True))
            self.queue.append(
                QuestionnaireView(self, quest.questionnaires["relC"], scenario_id=s, shuffle=True,
                                  display_scale_once=True))

            # Recalibrate Eye Tracker
            self.queue.append(
                PlainTextView(self, plain_text.re_calibrate_et["instr"], plain_text.re_calibrate_et["header"],
                              plain_text.re_calibrate_et["desc"]))

            # Presentation of the TI-texts (all levels)
            self.queue.append(PlainTextView(self, "", "", db_scenarios.scenarios["Desc"]))
            for con_sys in ["system_goal", "system_type", "data", "control"]:
                ti = [
                    [target_scenario["Text"][con_sys]["Files"][0], con_sys, True, False, False],
                    [target_scenario["Text"][con_sys]["Files"][1], con_sys, True, True, False],
                    [target_scenario["Text"][con_sys]["Files"][2], con_sys, False, True, True]
                ]
                self.queue.append(ti)

            self.queue.append(ControlQuestionView(self,
                                                  f"{s}_kf",
                                                  target_scenario["Question"],
                                                  target_scenario["Answers"]))

            # Post-survey
            self.queue.append(
                QuestionnaireView(self, quest.questionnaires["con"], scenario_id=s, shuffle=True,
                                  display_scale_once=False))

            self.queue.append(
                QuestionnaireView(self, quest.questionnaires["se"], scenario_id=s, shuffle=True,
                                  display_scale_once=True))

            self.queue.append(
                PlainTextView(self, plain_text.system_wahrnehmung["instr"], plain_text.system_wahrnehmung["header"],
                              plain_text.system_wahrnehmung["desc"]))

            self.queue.append(
                QuestionnaireView(self, quest.questionnaires["pc_post"], scenario_id=s, shuffle=True,
                                  display_scale_once=True))

            self.queue.append(
                QuestionnaireView(self, quest.questionnaires["a2"], scenario_id=s, shuffle=True,
                                  display_scale_once=True))

            self.queue.append(
                QuestionnaireView(self, quest.questionnaires["tw_ad"], scenario_id=s,
                                  shuffle=True, display_scale_once=True))
            self.queue.append(
                QuestionnaireView(self, quest.questionnaires["tw_aa"], scenario_id=s,
                                  shuffle=True, display_scale_once=True))
            self.queue.append(
                QuestionnaireView(self, quest.questionnaires["tw_be"], scenario_id=s,
                                  shuffle=True, display_scale_once=True))
            self.queue.append(
                QuestionnaireView(self, quest.questionnaires["tw_in"], scenario_id=s,
                                  shuffle=True, display_scale_once=True))
            self.queue.append(
                QuestionnaireView(self, quest.questionnaires["tw_tr"], scenario_id=s,
                                  shuffle=True, display_scale_once=True))
            self.queue.append(
                QuestionnaireView(self, quest.questionnaires["trust2"], scenario_id=s,
                                  shuffle=True, display_scale_once=True))

            self.queue.append(
                QuestionnaireView(self, quest.questionnaires["pg"], scenario_id=s, shuffle=True,
                                  display_scale_once=True))
            self.queue.append(
                QuestionnaireView(self, quest.questionnaires["ig"], scenario_id=s, shuffle=True,
                                  display_scale_once=True))
            self.queue.append(
                QuestionnaireView(self, quest.questionnaires["fairness"], scenario_id=s, shuffle=True,
                                  display_scale_once=True))

    def init_demographic(self):
        """Initialize and queue demographic questionnaire view.

        This method creates and adds a questionnaire view for collecting demographic 
        information to the experiment queue. The demographic questions are presented 
        in a fixed order without shuffling.

        Notes
        -----
        The demographic questionnaire:
        - Uses questions defined in quest.questionnaires["demography"]
        - Is presented without shuffling questions (shuffle=False)
        - Shows scale labels for each question (display_scale_once=False)

        See Also
        --------
        QuestionnaireView : View class for presenting questionnaires
        """
        self.queue.append(
            QuestionnaireView(self, quest.questionnaires["demography"], shuffle=False,
                              display_scale_once=False))

    def append_quest_csv(self):
        """Append questionnaire results to CSV file and clear results dictionary.

        Writes the current questionnaire results stored in results_dict to the 
        participant's CSV file and clears the dictionary afterwards.

        Notes
        -----
        - Opens quest_dir CSV file in append mode
        - Writes each key-value pair from results_dict as a new row
        - Uses semicolon as delimiter
        - Clears results_dict after writing
        """
        print("update csv")
        with open(self.quest_dir, "a", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=";")
            for key, value in self.results_dict.items():
                writer.writerow([key, value])

        self.results_dict.clear()
