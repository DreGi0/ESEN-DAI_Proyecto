from Model.db import validate_credentials

class LoginController:
    def __init__(self, view):
        self.view = view

    def login(self, user, password):
        if validate_credentials(user, password):
            self.view.show_feedback("Iniciando sesión")
            self.view.close()
            self.open_main_window()
        else:
            self.view.show_feedback("Credenciales incorrectas")
    
    def open_main_window(self):
        from View.main_view import MainWindow
        self.main_window = MainWindow()
        self.main_window.show()
