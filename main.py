from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QWidget
from PySide6.QtCore import Qt, QTimer

roshan_dead = """
QPushButton {
    background-color: #000000;
    color: #a1a1a1; /* White */
    border: 2px solid #a1a1a1;
    font-size: 20px;
    font-weight: bold;
    background-image: url("icons/roshan_resized.jpg");
    background-repeat: no-repeat;
    background-position: center;
}
"""

roshan_up = """
QPushButton {
    background-color: #000000;
    color: #54cc67; /* Moderate Green */
    font-size: 20px;
    font-weight: bold;
    border: 2px solid #54cc67;
    background-image: url("icons/roshan_resized.jpg");
    background-repeat: no-repeat;
    background-position: center;
    text-shadow: 2px 2px 4px #000000; /* horizontal offset, vertical offset, blur radius, color */
}
"""



class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # Create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create the button and label
        self.button = self._create_rosh_button()

        # Position the button and label
        button_x, button_y = 0, 1062  # Replace with desired coordinates for button
        self.button.move(button_x, button_y)

        # Set window properties
        self.setStyleSheet("background-color: transparent;")
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint) 
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setFixedSize(QApplication.primaryScreen().size())
        self.show()

        # Countdown Timer Setup
        self.countdown_duration = 660  # 11 minutes in seconds
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_countdown)

    def _create_rosh_button(self) -> QPushButton:
        button = QPushButton("START TIMER!", self.centralWidget())
        button.setFixedSize(325, 50)
        # Use the appropriate stylesheet here
        button.setStyleSheet(roshan_dead)
        button.clicked.connect(self.start_countdown)
        return button

    def start_countdown(self) -> None: 
        self.current_time = self.countdown_duration
        self.timer.start(1000)  # Timer updates every second
        self.update_countdown()  # To immediately update the button text

    def update_countdown(self) -> None:
        minutes, seconds = divmod(self.current_time, 60)
        self.button.setText(f"{minutes:02d}:{seconds:02d}")
        if self.current_time == 480:  # 8 minutes remaining
            # Change to the appropriate stylesheet and text
            self.button.setStyleSheet(roshan_up)
            self.button.setText(f"{minutes:02d}:{seconds:02d}")
        if self.current_time <= 0:
            self.timer.stop()
            self.button.setStyleSheet(roshan_up)
            self.button.setText("ROSHAN IS UP!")
        self.current_time -= 1

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec()