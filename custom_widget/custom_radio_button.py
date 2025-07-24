from PyQt6.QtWidgets import QRadioButton, QSizePolicy
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QColor


class FullCellRadioButton(QRadioButton):
    """A custom radio button widget that fills its entire grid cell with hover effects.

    This class extends QRadioButton to create a radio button that responds to mouse
    interactions across its entire cell area, not just the radio button indicator.
    It includes hover effects and ensures clicking anywhere in the cell triggers
    the radio button selection.

    Args:
        label (str, optional): The text label for the radio button. Defaults to None.
        center (bool, optional): Whether to center the radio button indicator.
            Defaults to True.

    Attributes:
        hovered (bool): Tracks whether the mouse is currently hovering over the button.
    """
    def __init__(self, label=None, center=True):
        super().__init__(label)
        self.hovered = False

        # Make the button fill the grid cell
        # self.setMinimumWidth(50)
        # self.setMinimumHeight(50)
        self.setStyleSheet("""
            FullCellRadioButton {
                background-color: transparent;
                border: none;
            }
        """)

        if center:
            self.setStyleSheet("""
              QRadioButton::indicator {
                    subcontrol-position: center; /* Center the indicator */
                    subcontrol-origin: padding; /* Align relative to the padding */
                }
                    """)

    def enterEvent(self, event):
        """Change appearance when mouse enters the button's space."""
        self.hovered = True
        self.update()
        super().enterEvent(event)

    def leaveEvent(self, event):
        """Reset appearance when mouse leaves the button's space."""
        self.hovered = False
        self.update()
        super().leaveEvent(event)

    def paintEvent(self, event):
        """Paint hover effect and call base drawing."""
        super().paintEvent(event)
        if self.hovered:
            # Draw hover effect across the entire cell area
            painter = QPainter(self)
            painter.setBrush(QColor(173, 216, 230, 100))  # Light blue with transparency
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawRect(self.rect())

    def mousePressEvent(self, event):
        """Ensure that clicking anywhere in the grid cell selects the radio button."""
        if event.button() == Qt.MouseButton.LeftButton:
            self.setChecked(True)
        super().mousePressEvent(event)