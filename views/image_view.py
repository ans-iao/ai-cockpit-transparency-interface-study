from PyQt6.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel, QSpacerItem
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QSize
import os


class ImageView(QWidget):
    """
    A widget class for displaying images with navigation and control buttons in a study interface.

    This class creates a view containing an image with optional forward/backward navigation
    buttons and a continue button. It is used to display different scenarios and transparency
    interface types in an AI study application.

    Args:
        parent: The parent widget that contains this view
        img_path (str): Path to the image file to display
        ti_type (str): Type of transparency interface ('system_goal', 'system_type', 'data', 'control')
        forward (bool): Whether to enable the forward navigation button (default: True)
        backward (bool): Whether to enable the backward navigation button (default: True)
        next_button (bool): Whether to enable the continue button (default: True)

    Attributes:
        parent: Reference to parent widget
        scenario (str): Single character identifier of the scenario (a-f)
        number (str): Page/level number within the scenario
        ti_type (str): Type of transparency interface being displayed
    """
    def __init__(self, parent, img_path, ti_type, forward=True, backward=True, next_button=True):
        super().__init__()

        self.parent = parent

        path = os.path.basename(os.path.normpath(img_path))

        self.scenario = path[0]
        self.number = path[-5:-4]
        self.ti_type = ti_type
        print(path, self.scenario, self.number)

        layout_main = QGridLayout()
        layout_main.setContentsMargins(0, 0, 0, 0)

        """ Add Image """
        pixmap = QPixmap(img_path)
        label = QLabel()
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        layout_main.addWidget(label, 0, 0, 2, 1)

        """ Button Panel """
        layout_button = QGridLayout()
        layout_button.setContentsMargins(50, 50, 50, 50)

        self.button_backward = QPushButton("<")
        self.button_backward.clicked.connect(self.on_backward_clicked)
        self.button_backward.setFixedSize(QSize(70, 50))
        self.button_backward.setEnabled(backward)
        layout_button.addWidget(self.button_backward, 0, 0, Qt.AlignmentFlag.AlignRight)

        self.button_forward = QPushButton(">")
        self.button_forward.clicked.connect(self.on_forward_clicked)
        self.button_forward.setFixedSize(QSize(70, 50))
        self.button_forward.setEnabled(forward)
        layout_button.addWidget(self.button_forward, 0, 1, Qt.AlignmentFlag.AlignLeft)

        self.button_next = QPushButton("Weiter")
        self.button_next.clicked.connect(self.on_continue_clicked)
        self.button_next.setFixedSize(QSize(200, 50))
        self.button_next.setEnabled(next_button)
        layout_button.addWidget(self.button_next, 0, 1, Qt.AlignmentFlag.AlignRight)

        layout_main.addLayout(layout_button, 1, 0)

        # spacer = QLabel()
        # spacer.setFixedHeight(50)
        # spacer.setStyleSheet("QLabel { background-color: lightblue; }")
        # layout_main.addWidget(spacer, 2, 0, 1, 2)

        self.setLayout(layout_main)

    def on_forward_clicked(self):
        self.parent.next_text(1)

    def on_backward_clicked(self):
        self.parent.next_text(-1)

    def on_continue_clicked(self):
        self.parent.next()

    def get_view_type(self):
        d = {
            'a': "1",
            'b': "2",
            'c': "3",
            'd': "4",
            'e': "5",
            'f': "6"
        }

        ti_d = {
            "system_goal": "1",
            "system_type": "2",
            "data": "3",
            "control": "4",
        }

        return int(f"{d[self.scenario]}{ti_d[self.ti_type]}{self.number}")
