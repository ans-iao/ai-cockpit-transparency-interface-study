from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QApplication
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QSize
import config as cfg


class EndView(QWidget):
    """
    A view class that displays the final screen of the application.

    This view shows an instruction text and content message to the user,
    along with a close button to exit the application. It represents the end
    state (marker 4) in the eye tracking study flow.

    Args:
        parent: The parent widget this view belongs to
        instr (str): The instruction text to display at the top
        content (str): The main content text to display in the center
    """
    def __init__(self, parent, instr, content):
        super().__init__()

        self.parent = parent

        layout_main = QVBoxLayout()
        layout_main.setContentsMargins(cfg.w_width // 4, cfg.w_height // 5, cfg.w_width // 4, cfg.w_height // 5)
        layout_main.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        """ Instruction Panel """
        instr_label = QLabel(instr)
        instr_label.setWordWrap(True)
        instr_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        font = QFont()
        font.setPointSize(16)  # Set font size

        instr_label.setFont(font)
        instr_label.setContentsMargins(0, 0, 0, cfg.w_height // 20)
        layout_main.addWidget(instr_label, alignment=Qt.AlignmentFlag.AlignCenter)

        """ Content Panel """
        content_label = QLabel(content)
        content_label.setWordWrap(True)
        content_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        layout_main.addWidget(content_label, alignment=Qt.AlignmentFlag.AlignCenter)

        """ Button Panel """
        button_continue = QPushButton("Schließen")
        button_continue.clicked.connect(self.on_close_clicked)
        button_continue.setFixedSize(QSize(200, 50))

        layout_main.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        layout_main.addWidget(button_continue, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout_main)

    def on_close_clicked(self):
        QApplication.closeAllWindows()

    def get_view_type(self):
        return 4
