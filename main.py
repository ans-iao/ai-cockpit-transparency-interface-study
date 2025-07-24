from PyQt6.QtWidgets import QApplication
import sys
from windows import MainWindow
import config as cfg
from PyQt6.QtGui import QFont


if __name__ == '__main__':
    app = QApplication(sys.argv)
    font = QFont("Segoe UI", 14)
    app.setFont(font)

    # Load stylesheet
    # with open("style.qss", "r") as f:
    #     app.setStyleSheet(f.read())

    screen_geometry = app.screens()[cfg.monitor_index].geometry()

    window = MainWindow()
    window.move(screen_geometry.x(), screen_geometry.y())
    window.show()

    app.exec()
