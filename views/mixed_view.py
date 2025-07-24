from PyQt6.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton, QLabel, QFrame, QMessageBox
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont
from components import QuestionItemRadio, QuestionHeader, QuestionItemInput, QuestionItemInputArea
from database.scale_types import scale_types as st
import config as cfg


class MixedView(QWidget):
    """
    A custom widget for displaying mixed question types in a questionnaire interface.

    This widget combines different types of questions (text input, text area, single choice)
    in a single view with a title, instructions, header, and content sections.

    Args:
        parent: The parent widget this view belongs to
        title (str): The title text to display at the top
        instr (str): Instructions text to display below the title
        header (str): Header text to display below instructions
        content (str): Main content text to display
        q_data (dict): Dictionary containing question data and configuration
        scenario_id (str, optional): ID of the scenario being displayed. Defaults to ""

    The widget includes:
    - Title section (if provided)
    - Instruction panel (if provided)
    - Header panel (if provided)
    - Content panel
    - Question items (various types)
    - Continue button
    """

    def __init__(self, parent, title, instr, header, content, q_data, scenario_id=""):
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

        layout_main = QVBoxLayout()
        layout_main.setContentsMargins(cfg.w_width // 5, cfg.w_height // 15, cfg.w_width // 5, cfg.w_height // 15)
        layout_main.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        """ Title """
        if len(instr) > 0:
            title_label = QLabel(title)
            title_label.setWordWrap(True)
            title_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            font = QFont()
            font.setPointSize(18)  # Set font size
            font.setBold(True)
            title_label.setFont(font)
            title_label.setContentsMargins(0, 0, 0, 50)
            layout_main.addWidget(title_label)

        """ Instruction Panel """
        if len(instr) > 0:
            instr_label = QLabel(instr)
            instr_label.setWordWrap(True)
            instr_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            font = QFont()
            # font.setPointSize(18)  # Set font size
            font.setBold(True)
            instr_label.setFont(font)
            instr_label.setContentsMargins(0, 0, 0, 25)
            layout_main.addWidget(instr_label)

        """ Header Panel """
        if len(header) > 0:
            header_label = QLabel(header)
            layout_main.addWidget(header_label)

        """ Content Panel """
        content_label = QLabel(content)
        content_label.setWordWrap(True)
        layout_main.addWidget(content_label)

        """ Question """
        question_header_label = self.create_header(q_data)
        layout_main.addWidget(question_header_label)
        if self.questionItems[0][0]["type"] == "single_choice":
            question_header = QuestionHeader(self, st["single_choice"][self.questionItems[0][0]["misc"]])
            question_header.setContentsMargins(0, 50, 0, 0)
            layout_main.addWidget(question_header)

        for questionItem in self.questionItems:
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
                if val[0] in ["CIR1", "CIR2_o"] or val[0][-3:] == "CIS":
                    if val[1] == 2:  # User selects "no"
                        QMessageBox.information(
                            self,
                            'Information',
                            'Hatten Sie Probleme, sich in die Rolle oder Szenario zu versetzen? Melden Sie sich einfach! Die Versuchungsleitung hilft Ihnen gerne weiter.'
                        )
                        all_good = False
                        break

                    else:
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
