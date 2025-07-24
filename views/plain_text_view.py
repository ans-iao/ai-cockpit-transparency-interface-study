from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication, QLabel, QSpinBox, QHBoxLayout, QSpacerItem, \
    QSizePolicy
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QSize
import config as cfg


class PlainTextView(QWidget):
    """
    A PyQt widget that displays plain text content with an optional instruction and header.

    This widget is used to present text-based information in the AI-Cockpit transparency interface study.
    It consists of three main sections: instruction text, header text, and content text, along with
    a continue button for navigation.

    Parameters:
        parent: Parent widget that handles navigation between views
        instr (str): Instruction text to display at the top (optional)
        header (str): Header text to display below instructions (optional) 
        content (str): Main content text to display

    View Type: 2 (Plaintext)
    """

    def __init__(self, parent, instr, header, content):
        super().__init__()

        self.parent = parent

        layout_main = QVBoxLayout()
        layout_main.setContentsMargins(cfg.w_width // 4, cfg.w_width // 5, cfg.w_width // 4, cfg.w_height // 5)
        # layout_main.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        """ Instruction Panel """
        if len(instr) > 0:
            instr_label = QLabel(instr)
            instr_label.setWordWrap(True)
            instr_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            font = QFont()
            # font.setPointSize(18)  # Set font size
            font.setBold(True)
            instr_label.setFont(font)
            instr_label.setContentsMargins(0, 0, 0, 50)
            layout_main.addWidget(instr_label)

        """ Header Panel """
        if len(header) > 0:
            header_label = QLabel(header)
            header_label.setWordWrap(True)
            layout_main.addWidget(header_label)

        """ Content Panel """
        content_label = QLabel(content)
        content_label.setWordWrap(True)
        # content_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        layout_main.addWidget(content_label)

        """ Button Panel """
        button_continue = QPushButton("Weiter")
        button_continue.clicked.connect(self.on_continue_clicked)
        button_continue.setFixedSize(QSize(200, 50))

        layout_main.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        layout_main.addWidget(button_continue, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(layout_main)

    def on_continue_clicked(self):
        self.parent.next()

    def get_view_type(self):
        return 2