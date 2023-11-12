from PySide6.QtWidgets import *
from PySide6.QtCore import Qt


button_style = """
QPushButton {
    background-color: #2E2E2E;
    border: 1px solid #FFFFFF;
    border-radius: 25px;
    color: #FFFFFF;
    font-size: 20px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #FFFFFF;
    color: #2E2E2E;
}
"""

from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # Create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create and set layout on the central widget
        main_layout = QVBoxLayout(central_widget)
        main_layout.addWidget(self._create_rosh_button())

        self.setStyleSheet("background-color: transparent;")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.setFixedSize(QApplication.primaryScreen().size())

        self.show()

    def _create_rosh_button(self) -> QPushButton:
        button = QPushButton(self)
        button.setFixedSize(50, 50)
        button.setStyleSheet(button_style)  # Example style
        return button

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec_()
