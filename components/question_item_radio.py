from PyQt6.QtWidgets import QWidget, QLabel, QGridLayout, QMessageBox, QSizePolicy
from PyQt6.QtCore import Qt
import config as cfg
from custom_widget import FullCellRadioButton


class QuestionItemRadio(QWidget):
    """A custom widget that represents a single radio button question item.

    This widget displays a question with multiple radio button options arranged horizontally.
    Used for gathering survey responses where only one option can be selected.

    Attributes:
        parentWidget: Reference to the parent widget
        code: Identifier code for the question
        radioBoxList (list): List of radio button widgets
        selectedIndex (int): Index of currently selected radio button (1-based)

    Methods:
        on_checked(): Handles radio button selection events
        get_answer_value(): Returns tuple of (code, selected_value) or None if nothing selected
    """
    def __init__(self, parent, code, question, num_options=7):
        super().__init__()
        self.parentWidget = parent

        self.code = code

        layout_main = QGridLayout()

        label_question = QLabel(question)
        label_question.setWordWrap(True)
        label_question.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        label_question.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        label_question.setMinimumWidth(400)
        span = cfg.question_span
        layout_main.addWidget(label_question, 0, 0, 1, span)

        self.radioBoxList = []
        for i in range(num_options):
            radio_button = FullCellRadioButton()

            radio_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
            radio_button.setMinimumHeight(50)

            radio_button.toggled.connect(self.on_checked)
            self.radioBoxList.append(radio_button)
            layout_main.addWidget(radio_button, 0, i + span, 1, 1)

        # Fill res of the space with spacers
        for i in range(cfg.max_cols - (num_options + span)):
            layout_main.addWidget(QLabel(""), 0, num_options + i + span, 1, 1)

        self.setLayout(layout_main)

        self.selectedIndex = None

    def on_checked(self):
        sender = self.sender()
        if sender.isChecked():
            self.selectedIndex = self.radioBoxList.index(sender)

    def get_answer_value(self):
        if self.selectedIndex is None:
            QMessageBox.warning(
                self,
                'Anmerkung',
                'Bitte alle Fragen ausfüllen.'
            )
            return None

        return self.code, self.selectedIndex + 1
