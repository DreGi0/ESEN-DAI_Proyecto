from Model.db import validate_credentials

class LoginController:
    def __init__(self, view):
        self.view = view

    def login(self, user, password):
        if validate_credentials(user, password):
            self.view.show_feedback("Iniciando sesión")
            '''Aqui va la logica del login (redirigi a otra ventana por ejemplo)'''

        else:
            self.view.show_feedback("Credenciales incorrectas")