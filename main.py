from PyQt6.QtWidgets import QApplication
import sys
from View.login_view import LoginWindow

def main():
    app = QApplication(sys.argv)

    with open(r"Resources\style.qss") as styles:
        style = styles.read()
        app.setStyleSheet(style)

    ventana = LoginWindow()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()