import random

from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt6.QtCore import Qt, QSize
import config as cfg
from components import QuestionItemRadio, QuestionHeader


class ControlQuestionView(QWidget):
    """
    A view class that displays control questions to users in the AI-Cockpit transparency interface study.

    This view presents a question with multiple radio button answer options in a randomized order.
    Used for control/verification questions in the study interface with eye tracker marker 3.

    Attributes:
        parent: Parent widget reference
        key: Question identifier key
        answerList: List of possible answers
        answerIndex: Mapping of answer text to numeric index
        selectedAnswer: Currently selected answer value
    """

    def __init__(self, parent, key, question, answer_options):
        super().__init__()

        self.parent = parent
        self.key = key

        self.answerList = []
        self.answerIndex = {}

        for answer in answer_options:
            self.answerIndex[answer[1]] = int(answer[0])
            self.answerList.append(answer[1])

        random.shuffle(self.answerList)

        question_header = QuestionHeader(self, self.answerList)
        self.question_item = QuestionItemRadio(self, key, question, len(self.answerList))

        layout_main = QVBoxLayout()
        layout_main.setContentsMargins(cfg.w_width // 10, 0, cfg.w_width // 10, cfg.w_height // 10)
        layout_main.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        layout_main.addWidget(question_header)
        layout_main.addWidget(self.question_item)

        """ Button Panel """
        button_continue = QPushButton("Weiter")
        button_continue.clicked.connect(self.on_continue_clicked)
        button_continue.setFixedSize(QSize(200, 50))

        layout_main.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        layout_main.addWidget(button_continue, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(layout_main)

        self.selectedAnswer = None

    def on_continue_clicked(self):
        val = self.question_item.get_answer_value()
        if val is not None:
            q_index = val[1]
            print("index", q_index)
            self.selectedAnswer = self.answerIndex[self.answerList[q_index - 1]]
            self.parent.set_questionnaire_result({self.key: self.selectedAnswer + 1})

    def get_view_type(self):
        return 3
