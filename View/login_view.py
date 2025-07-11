from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLabel, QLineEdit, QPushButton
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QCursor
from Controller.login_controller import LoginController


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.controller = LoginController(self)
        self.setup_layout()
        self.setup_styles()
        self.connect_signals()

    def init_ui(self):
        """Configuración inicial de la ventana"""
        self.setWindowTitle("Super Duper App")
        self.setGeometry(100, 100, 1000, 700)

    def setup_layout(self):
        """Configuración del layout principal"""
        # Contenedor principal
        self.main_container = QWidget()
        self.main_layout = QVBoxLayout()
        self.login_container = QWidget()
        self.login_layout = QFormLayout()
        self.login_container.setLayout(self.login_layout)
        
        # Logo
        self.setup_logo()
        
        # Elementos de interfaz
        self.setup_ui_elements()
        
        # Layouts para centrar elementos
        self.setup_centered_layouts()
        
        # Agregar elementos al formulario
        self.add_elements_to_form()
        
        # Configurar contenedor principal
        self.main_layout.addWidget(self.login_container)
        self.main_container.setLayout(self.main_layout)
        self.setCentralWidget(self.main_container)

    def setup_logo(self):
        """Configuración del logo"""
        self.logo = QLabel()
        self.logo_img = QPixmap(r"Resources\img\logo.png")
        self.logo.setFixedSize(420, 200)
        self.logo.setScaledContents(True)
        self.logo.setPixmap(self.logo_img)
        
        # Layout para centrar el logo
        self.logo_layout = QHBoxLayout()
        self.logo_layout.addStretch()
        self.logo_layout.addWidget(self.logo)
        self.logo_layout.addStretch()

    def setup_ui_elements(self):
        """Configuración de elementos de interfaz"""
        # Titulo
        self.welcome_label = QLabel("Inicio de sesión")
        
        # Etiquetas
        self.user_label = QLabel("      Usuario")
        self.password_label = QLabel("Contraseña")
        
        # Campos entrada
        self.user_input = QLineEdit()
        self.password_input = QLineEdit()
        
        # Mensaje feedback
        self.feedback_label = QLabel("Esta es una prueba de feedback")
        self.feedback_label.setObjectName("feedback")
        
        # Botón ingreso
        self.login_button = QPushButton("Ingresar")
        
        # Espaciado
        self.spacer = QLabel()
        self.spacer.setFixedHeight(30)

    def setup_styles(self):
        """Configuración de estilos"""
        self.welcome_label.setStyleSheet("font-size: 25px")
        self.user_input.setFixedWidth(150)
        self.password_input.setFixedWidth(150)
        self.login_button.setFixedSize(150, 20)
        self.login_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

    def setup_centered_layouts(self):
        """Configuración de layouts centrados"""
        # Centrar título
        self.title_layout = QHBoxLayout()
        self.title_layout.addStretch()
        self.title_layout.addWidget(self.welcome_label)
        self.title_layout.addStretch()
        
        # Centrar campo usuario
        self.user_layout = QHBoxLayout()
        self.user_layout.addStretch()
        self.user_layout.addWidget(self.user_label)
        self.user_layout.addWidget(self.user_input)
        self.user_layout.addStretch()
        
        # Centrar campo contraseña
        self.password_layout = QHBoxLayout()
        self.password_layout.addStretch()
        self.password_layout.addWidget(self.password_label)
        self.password_layout.addWidget(self.password_input)
        self.password_layout.addStretch()
        
        # Centrar feedback
        self.feedback_layout = QHBoxLayout()
        self.feedback_layout.addStretch()
        self.feedback_layout.addWidget(self.feedback_label)
        self.feedback_layout.addStretch()
        
        # Centrar botón
        self.button_layout = QHBoxLayout()
        self.button_layout.addStretch()
        self.button_layout.addWidget(self.login_button)
        self.button_layout.addStretch()

    def add_elements_to_form(self):
        """Agregar elementos al formulario"""
        self.login_layout.addRow(self.logo_layout)
        self.login_layout.addRow(self.title_layout)
        self.login_layout.addRow(self.spacer)
        self.login_layout.addRow(self.user_layout)
        self.login_layout.addRow(self.password_layout)
        self.login_layout.addRow(self.feedback_layout)
        self.login_layout.addRow(QLabel())
        self.login_layout.addRow(self.button_layout)

    def connect_signals(self):
        """Conectar señales de la interfaz"""
        self.login_button.clicked.connect(self.try_login)

    def try_login(self):
        user = self.user_input.text().strip()
        password = self.password_input.text().strip()
        
        if not user or not password:
            self.show_feedback("Completa todos los campos")
            return
        
        if len(user) < 3 or len(password) < 3:
            self.show_feedback("Usuario y contraseña deben tener al menos 3 caracteres")
            return
    
        self.controller.login(user, password)

    def show_feedback(self, message):
        """Mostrar mensaje de feedback"""
        self.feedback_label.setText(message)

    def clear_inputs(self):
        """Limpiar campos de entrada"""
        self.user_input.clear()
        self.password_input.clear()

    def get_user_input(self):
        """Obtener texto del campo usuario"""
        return self.user_input.text()

    def get_password_input(self):
        """Obtener texto del campo contraseña"""
        return self.password_input.text()

    def set_user_focus(self):
        """Establecer foco en el campo usuario"""
        self.user_input.setFocus()

    def set_password_focus(self):
        """Establecer foco en el campo contraseña"""
        self.password_input.setFocus()