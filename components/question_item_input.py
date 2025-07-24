from PyQt6.QtWidgets import QWidget, QLabel, QGridLayout, QLineEdit, QMessageBox, QSizePolicy
from PyQt6.QtCore import Qt
import config as cfg


class QuestionItemInput(QWidget):
    """
    A custom widget for handling question input fields in the AI-Cockpit study interface.

    This widget creates a question item with a question label and an input field.
    It supports both numeric and text input validation.

    Parameters:
        parent: The parent widget
        code: Question identifier code
        question: The question text to display
        input_label: Label for the input field (can be empty)
        is_numeric: Boolean indicating if input should be numeric (default: True)
    """
    def __init__(self, parent, code, question, input_label, is_numeric=True):
        super().__init__()
        self.parentWidget = parent

        self.isNumeric = is_numeric
        self.code = code

        layout_main = QGridLayout()

        label_question = QLabel(question)
        label_question.setWordWrap(True)
        label_question.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        label_question.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        label_question.setMinimumWidth(400)
        span = cfg.question_span
        layout_main.addWidget(label_question, 0, 0, 1, span)

        num_items = 0

        if len(input_label) > 0:
            text_label = QLabel(input_label)
            layout_main.addWidget(text_label, 0, span, 1, 1, alignment=Qt.AlignmentFlag.AlignRight)
            num_items += 1

        self.text_input = QLineEdit()
        layout_main.addWidget(self.text_input, 0, span + num_items, 1, 2)
        num_items += 2

        for i in range(cfg.max_cols - (num_items + span)):
            layout_main.addWidget(QLabel(""), 0, num_items + i + span, 1, 1)

        self.setLayout(layout_main)

    def get_answer_value(self):
        if self.isNumeric:
            print(self.text_input.text())
            if not self.text_input.text().isnumeric():
                QMessageBox.warning(
                    self,
                    'Anmerkung',
                    'Eine Eingabe muss eine Zahl sein.'
                )
                return None

        if len(self.text_input.text()) <= 0:
            QMessageBox.warning(
                self,
                'Anmerkung',
                'Texteingabe fehlt'
            )
            return None

        return self.code, self.text_input.text()
