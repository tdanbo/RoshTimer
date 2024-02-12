from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton,  QWidget
from PySide6.QtCore import Qt, QTimer
from detect_rosh import check_for_roshan
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
roshan_dead = """
QPushButton {
    background-color: #000000;
    color: #a1a1a1; /* White */
    border: 1px solid #a1a1a1;
    font-size: 18px;
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
    font-size: 18px;
    font-weight: bold;
    border: 1px solid #54cc67;
    background-image: url("icons/roshan_resized.jpg");
    background-repeat: no-repeat;
    background-position: center;
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
        self.rosh_alive()
        # Position the button and label
        button_x, button_y = 750, 1200  # Replace with desired coordinates for button
        self.button.move(button_x, button_y)

        self.primary_monitor = QApplication.primaryScreen().size()

        # Set window properties
        self.setStyleSheet("background-color: transparent;")
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint) 
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setFixedSize(self.primary_monitor)
        self.show()



        # Countdown Timer Setup
        self.countdown_duration = 660  # 11 minutes in seconds
        # self.countdown_duration = 200  # 11 minutes in seconds
        self.rosh_spawn_timer = QTimer(self)
        self.rosh_spawn_timer.timeout.connect(self.update_countdown)

        self.roshan_listener_timer = QTimer(self)
        self.roshan_listener_timer.timeout.connect(self.start_roshan_listener)
        self.roshan_listener_timer.start(5000)  # Timer updates every second

    def _create_rosh_button(self) -> QPushButton:
        button = QPushButton("", self.centralWidget())
        button.setFixedSize(100, 45)

        # Use the appropriate stylesheet here
        
        return button

    def start_roshan_listener(self) -> None:
        #check_for_roshan(width= self.primary_monitor.width(), height= self.primary_monitor.height())
        if check_for_roshan(width= self.primary_monitor.width(), height= self.primary_monitor.height()):
            print("Roshan has been killed!")
            self.start_countdown()
        else:
            print("...")
            pass

    def start_countdown(self) -> None: 
        print("Starting countdown")
        self.current_time = self.countdown_duration
        self.rosh_spawn_timer.start(1000)  # Timer updates every second
        print(self.current_time)
        self.update_countdown()  # To immediately update the button text

    def update_countdown(self) -> None:
        minutes, seconds = divmod(self.current_time, 60)
        self.button.setText(f"{minutes:02d}:{seconds:02d}")
        self.rosh_dead()
        if self.current_time <= 180:  # 8 minutes passed (3 minutes remaining)
            self.rosh_spawn()
            self.button.setText(f"{minutes:02d}:{seconds:02d}")
        if self.current_time == 0:
            self.rosh_alive()
            self.rosh_spawn_timer.stop()
        self.current_time -= 1

    def rosh_alive(self) -> None:
        self.button.setStyleSheet(roshan_up)
        self.button.setIcon(QIcon("icons/roshan_up.png"))
        self.button.setIconSize(QSize(50, 50))
        self.button.setText("")

    def rosh_spawn(self) -> None:
        self.button.setStyleSheet(roshan_up)
        self.button.setIcon(QIcon("icons/roshan_up.png"))
        self.button.setIconSize(QSize(30, 30))
                                
    def rosh_dead(self) -> None:
        self.button.setStyleSheet(roshan_dead)
        self.button.setIcon(QIcon("icons/roshan_dead.png"))
        self.button.setIconSize(QSize(30, 30))

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec()