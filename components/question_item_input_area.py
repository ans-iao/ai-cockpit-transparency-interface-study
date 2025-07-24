from PyQt6.QtWidgets import QWidget, QLabel, QGridLayout, QPlainTextEdit, QSizePolicy, QRadioButton, QMessageBox
from PyQt6.QtCore import Qt
import config as cfg
from custom_widget import FullCellRadioButton


class QuestionItemInputArea(QWidget):
    """A widget class for creating question input areas with radio buttons and text field.

    This class creates a question input area containing:
    - A question label
    - Optional input label
    - Two radio buttons ("Ja" and "Nein")
    - A text input area

    The widget is used to collect user responses where they can select Yes/No
    and provide additional text input when selecting "Yes".

    Attributes:
        parentWidget: Parent widget reference
        code: Question identifier code
        selected_radio: Currently selected radio button value
        text_area: Text input field for additional information
    """
    def __init__(self, parent, code, question, input_label):
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

        num_items = 0

        if len(input_label) > 0:
            text_label = QLabel(input_label)
            layout_main.addWidget(text_label, 0, span, 1, 1)
            num_items += 1

        radio_button_no = FullCellRadioButton("Nein", False)
        radio_button_no.toggled.connect(self.on_checked_no)
        radio_button_no.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        radio_button_no.setMinimumHeight(50)
        layout_main.addWidget(radio_button_no, 0, span + num_items, 1, 1)
        num_items += 1

        radio_button_yes = FullCellRadioButton("Ja, und zwar", False)
        radio_button_yes.toggled.connect(self.on_checked_yes)
        radio_button_yes.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        radio_button_yes.setMinimumHeight(50)
        layout_main.addWidget(radio_button_yes, 0, span + num_items, 1, 1, alignment=Qt.AlignmentFlag.AlignRight)
        num_items += 1

        self.text_area = QPlainTextEdit()
        self.text_area.setFixedSize(400, 80)
        layout_main.addWidget(self.text_area, 0, span + num_items, 1, 5)
        num_items += 5

        for i in range(cfg.max_cols - (num_items + span)):
            layout_main.addWidget(QLabel("A"), 0, num_items + i + span, 1, 1)

        self.setLayout(layout_main)

        self.selected_radio = None

    def on_checked_no(self):
        self.selected_radio = "1"

    def on_checked_yes(self):
        self.selected_radio = "2"

    def get_answer_value(self):
        if self.selected_radio is None:
            QMessageBox.warning(
                self,
                'Anmerkung',
                'Bitte alle Fragen ausfüllen.'
            )
            return None

        if self.selected_radio == "1":
            return self.code, "1"

        if self.selected_radio == "2":
            if len(self.text_area.toPlainText()) == 0:
                QMessageBox.warning(
                    self,
                    'Anmerkung',
                    'Bitte Textfeld ausfüllen, ansonsten auf Nein ankreuzen.'
                )
                return None

        return self.code, self.text_area.toPlainText()
