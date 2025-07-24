from PyQt6.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton, QLabel, QFrame
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont
from components import QuestionItemRadio, QuestionHeader, QuestionItemInput, QuestionItemInputArea
from database.scale_types import scale_types as st
import random
import config as cfg


class QuestionnaireView(QWidget):
    """
    A PyQt widget that displays a dynamic questionnaire with various question types.

    This widget creates and manages a questionnaire interface for the AI-Cockpit transparency study.
    It supports different question types including radio buttons, text inputs, and text areas.
    Questions can be randomly shuffled and displayed with configurable scale headers.

    Parameters:
        parent: Parent widget that handles questionnaire results
        q_data (dict): Dictionary containing questionnaire configuration and questions
        scenario_id (str): ID of the current scenario being evaluated
        shuffle (bool): Whether to randomize question order (default: True)
        display_scale_once (bool): Whether to show scale header once or for each question (default: True)

    View Type: 1 (QuestionView)
    """
    def __init__(self, parent, q_data, scenario_id="", shuffle=True, display_scale_once=True):
        super().__init__()

        self.parent = parent

        self.questionItems = []

        questions = q_data["questions"]
        for key in questions:

            key_f = key.format(scenario=scenario_id)

            question = questions[key]["val"]

            match questions[key]["type"]:
                case "text_input":
                    question_item = QuestionItemInput(self, key_f, question, questions[key]["label"],
                                                      questions[key]["numeric"])
                case "text_area":
                    question_item = QuestionItemInputArea(self, key_f, question,
                                                          questions[key]["label"])
                case "single_choice":
                    num_radios = len(st["single_choice"][questions[key]["misc"]])
                    question_item = QuestionItemRadio(self, key_f, question, num_radios)

            self.questionItems.append((questions[key], question_item))

        if shuffle:
            random.shuffle(self.questionItems)

        layout_main = QVBoxLayout()
        layout_main.setContentsMargins(cfg.w_width // 8, cfg.w_height // 15, cfg.w_width // 8, cfg.w_height // 15)
        layout_main.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        header_label = self.create_header(q_data)
        layout_main.addWidget(header_label)

        """ Question """
        if display_scale_once:
            if self.questionItems[0][0]["type"] == "single_choice":
                question_header = QuestionHeader(self, st["single_choice"][self.questionItems[0][0]["misc"]])
                question_header.setContentsMargins(0, 50, 0, 0)
                layout_main.addWidget(question_header)

        for questionItem in self.questionItems:

            if not display_scale_once:
                if questionItem[0]["type"] == "single_choice":
                    question_header = QuestionHeader(self, st["single_choice"][questionItem[0]["misc"]])
                    # question_header.setContentsMargins(0, 50, 0, 0)
                    layout_main.addWidget(question_header)

            layout_main.addWidget(questionItem[1])
            layout_main.addWidget(self.add_line())

        """ Button """
        button_continue = QPushButton("Weiter")
        button_continue.clicked.connect(self.on_continue_clicked)
        button_continue.setFixedSize(QSize(200, 50))

        layout_main.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        layout_main.addWidget(button_continue, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(layout_main)

    def on_continue_clicked(self):
        results_dict = {}
        all_good = True
        for items in self.questionItems:
            val = items[1].get_answer_value()
            if val is not None:
                results_dict[val[0]] = val[1]
            else:
                all_good = False
                break

        if all_good:
            self.parent.set_questionnaire_result(results_dict)

    def create_header(self, q_data):
        header_label = QLabel(q_data["header"])
        header_label.setWordWrap(True)
        header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont()
        font.setPointSize(16)  # Set font size
        header_label.setFont(font)
        return header_label

    def add_line(self):
        h_line = QFrame()
        h_line.setFrameShape(QFrame.Shape.HLine)  # Horizontal line
        h_line.setFrameShadow(QFrame.Shadow.Sunken)  # Optional shadow effect
        h_line.setLineWidth(1)
        return h_line

    def get_view_type(self):
        return 1
