from PyQt6.QtWidgets import QWidget, QLabel, QGridLayout, QSizePolicy
from PyQt6.QtCore import Qt
import config as cfg


class QuestionHeader(QWidget):
    """
    A PyQt widget that creates a header section for displaying scale labels in a questionnaire.

    This widget creates a horizontal header with scale labels evenly distributed across the width.
    It includes a spacer at the start and automatically fills remaining space with empty labels.

    Parameters:
        parent: The parent widget this header belongs to
        scale_labels (list): List of strings representing the scale labels to be displayed
    """
    def __init__(self, parent, scale_labels):
        super().__init__()
        self.parentWidget = parent

        layout_main = QGridLayout()

        spacer = QLabel(" ")
        spacer.setMinimumWidth(400)
        span = cfg.question_span
        layout_main.addWidget(spacer, 0, 0, 1, span)

        for i, lab in enumerate(scale_labels):
            label = QLabel(lab)
            label.setWordWrap(True)
            #label.setMaximumWidth(200)
            #label.setMinimumHeight(150)
            label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout_main.addWidget(label, 0, i + span, 1, 1)

        # Fill res of the space with spacers
        num_options = len(scale_labels)
        for i in range(cfg.max_cols - (num_options + span)):
            layout_main.addWidget(QLabel(""), 0, num_options + i + span, 1, 1)

        self.setLayout(layout_main)
