from PyQt6.QtWidgets import QApplication
import sys
from View.login_view import LoginWindow
from View.main_view import MainWindow

def main():
    app = QApplication(sys.argv)

    with open(r"Resources\style.qss") as styles:
        style = styles.read()
        app.setStyleSheet(style)

    main_window = MainWindow()
    login_window = LoginWindow()
    main_window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()