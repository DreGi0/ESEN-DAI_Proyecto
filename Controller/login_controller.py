from Model.login_model import validate_credentials, get_admin_by_credentials


class LoginController:
    """
    Controlador para manejar el proceso de autenticación de usuarios.
    """
    
    def __init__(self, view):
        """
        Inicializa el controlador de login.
        
        Args:
            view: Vista asociada al controlador de login
        """
        self.view = view
    
    # ==========================================================================
    # OPERACIONES DE AUTENTICACIÓN
    # ==========================================================================
    
    def login(self, user, password):
        """
        Procesa el intento de inicio de sesión del usuario.
        
        Args:
            user (str): Nombre de usuario
            password (str): Contraseña del usuario
        """
        if validate_credentials(user, password):
            self.view.show_feedback("Iniciando sesión")
            self.view.hide()
            self.open_main_window()
        else:
            self.view.show_feedback("Credenciales incorrectas")
    
    def open_main_window(self):
        """
        Abre la ventana principal después de un login exitoso.
        """
        from View.main_view import StartWindow
        self.main_window = StartWindow()
        self.main_window.show()
