from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication, QLabel, QSpinBox, QHBoxLayout, QSpacerItem, \
    QSizePolicy
from PyQt6.QtCore import Qt, QSize
import config as cfg
from pylsl import resolve_byprop


class MenuView(QWidget):
    """
    A widget representing the main menu interface for the AI-Cockpit study application.

    This menu provides controls for:
    - Setting the subject (participant) number
    - Checking and searching for eye tracker LSL stream connection
    - Starting the study
    - Exiting the application

    The menu ensures proper eye tracker connectivity before allowing the study to start.
    All interface elements are arranged vertically with proper spacing and margins.

    Attributes:
        parent: The parent widget/controller managing this view
        spinbox_subj_num (QSpinBox): Input for subject number (1-90)
        button_start (QPushButton): Button to start the study
        eye_label (QLabel): Status label for eye tracker connection
        stream: The detected eye tracker LSL stream
    """

    def __init__(self, parent, init_subj_num):
        super().__init__()

        self.parent = parent

        """ Subj Number Panel """
        label_subj_num = QLabel("Versuchsperson Nummer")
        self.spinbox_subj_num = QSpinBox()
        self.spinbox_subj_num.setValue(init_subj_num)
        self.spinbox_subj_num.setMinimum(1)
        self.spinbox_subj_num.setMaximum(90)
        self.spinbox_subj_num.setSingleStep(1)
        self.spinbox_subj_num.setFixedSize(QSize(100, 50))

        layout_subj_num = QHBoxLayout()
        layout_subj_num.addWidget(label_subj_num, alignment=Qt.AlignmentFlag.AlignRight)
        layout_subj_num.addWidget(self.spinbox_subj_num, alignment=Qt.AlignmentFlag.AlignLeft)

        """ Button Panel """
        self.button_start = QPushButton("Starten")
        self.button_start.setFixedSize(QSize(200, 50))
        self.button_start.clicked.connect(self.on_start_clicked)

        button_exit = QPushButton("Schließen")
        button_exit.setFixedSize(QSize(200, 50))
        button_exit.clicked.connect(self.on_exit_clicked)

        layout_button = QHBoxLayout()
        layout_button.addWidget(button_exit, alignment=Qt.AlignmentFlag.AlignRight)
        layout_button.addWidget(self.button_start, alignment=Qt.AlignmentFlag.AlignLeft)

        """ Eye Tracker LSL Check """
        streams = resolve_byprop("name", cfg.lsl_name, timeout=1)
        if len(streams) > 0:
            self.eye_label = QLabel("Eye-Tracker Stream gefunden")
            self.button_start.setEnabled(True)
            self.stream = streams[0]
        else:
            self.eye_label = QLabel("Kein Eye-Tracker Stream gefunden")
            self.button_start.setEnabled(False)
            self.stream = None

        layout_eye_checker = QHBoxLayout()
        eye_button = QPushButton("Suchen")
        eye_button.setFixedSize(QSize(200, 50))
        eye_button.clicked.connect(self.on_search_clicked)
        layout_eye_checker.addWidget(self.eye_label, alignment=Qt.AlignmentFlag.AlignRight)
        layout_eye_checker.addWidget(eye_button, alignment=Qt.AlignmentFlag.AlignLeft)

        """ Main Layout """
        layout_main = QVBoxLayout()
        layout_main.setContentsMargins(cfg.w_width // 3, 0, cfg.w_width // 3, 0)
        layout_main.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        layout_main.addLayout(layout_subj_num)
        layout_main.addLayout(layout_eye_checker)
        layout_main.addLayout(layout_button)
        layout_main.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        self.setLayout(layout_main)

    @staticmethod
    def on_exit_clicked():
        QApplication.closeAllWindows()

    def on_start_clicked(self):
        self.parent.start(self.spinbox_subj_num.text(), self.stream)

    def on_search_clicked(self):
        streams = resolve_byprop("name", cfg.lsl_name, timeout=1)
        if len(streams) > 0:
            self.eye_label.setText("Eye-Tracker Stream gefunden")
            self.button_start.setEnabled(True)
            self.stream = streams[0]
        else:
            self.eye_label.setText("Kein Eye-Tracker Stream gefunden")
            self.button_start.setEnabled(False)
            self.stream = None

    def get_view_type(self):
        return 0
