from PyQt6.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel
from Controller.main_controller import MainController
from View.factura_window import FacturaWindow

class MainWindow(QMainWindow):
    def __init__(self, user_id, user_name):
        super().__init__()
        self.user_id = user_id
        self.user_name = user_name

        self.controller = MainController(self, user_id, user_name)
        self.init_ui()

    def init_ui(self):
        """Interfaz gráfica"""
        self.setWindowTitle(f"Ferretería - Usuario: {self.user_name}")
        self.setGeometry(100, 100, 600, 400)

        # Contenedor central
        widget = QWidget()
        layout = QVBoxLayout()

        # Label de bienvenida con el nombre del usuario
        self.label = QLabel(f"Bienvenido {self.user_name}!")
        layout.addWidget(self.label)

        # Botón para gestión de productos
        self.btn_productos = QPushButton("Gestionar Productos")
        layout.addWidget(self.btn_productos)

        # Botón para abrir ventana de facturación
        self.btn_factura = QPushButton("Crear Factura")
        self.btn_factura.clicked.connect(self.abrir_factura)
        layout.addWidget(self.btn_factura)

        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def abrir_factura(self):
        """Crea y mostra la ventana de facturación"""
        self.factura_window = FacturaWindow(self.user_id)
        self.factura_window.show()