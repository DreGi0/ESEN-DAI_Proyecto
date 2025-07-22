from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QGridLayout,
    QPushButton, QLabel, QSizePolicy
)
from PyQt6.QtCore import Qt
from View.product_view import ProductWindow
from View.billing_view import BillingDialog
from View.inventory_view import InventoryDialog
from View.provider_view import ProviderDialog
from View.client_view import ClientDialog
from View.search_view import SearchDialog

class StartWindow(QMainWindow):
    """Ventana principal de inicio del sistema"""
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Ferretería Mónaco - Inicio")
        self.setGeometry(200, 200, 800, 500)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(30)

        # Título principal
        title = QLabel("Sistema de Gestión\nFerretería Mónaco")
        title.setProperty("cssClass", "title")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        # Subtítulo
        subtitle = QLabel("Selecciona un módulo para comenzar")
        subtitle.setProperty("cssClass", "subtitle")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(subtitle)

        # Botones en grid
        grid = QGridLayout()
        grid.setSpacing(20)
        button_style = """
            QPushButton {
                font-size: 15px;
                font-weight: 500;
                background-color: #2b3c56;
                color: white;
                border: none;
                border-radius: 8px;
                min-width: 180px;
                min-height: 50px;
            }
            QPushButton:hover {
                background-color: #3d4d6a;
            }
        """

        btns = [
            ("Gestión de Productos", self.open_products_module),
            ("Facturación", self.open_billing_module),
            ("Inventario", self.open_inventory_module),
            ("Proveedores", self.open_provider_module),
            ("Clientes", self.open_client_module),
            ("Búsqueda", self.open_search_module),
        ]
        positions = [(i, j) for i in range(2) for j in range(3)]
        for pos, (text, slot) in zip(positions, btns):
            btn = QPushButton(text)
            btn.setStyleSheet(button_style)
            btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            btn.clicked.connect(slot)
            grid.addWidget(btn, *pos)

        layout.addLayout(grid)

        # Botón cerrar sesión
        logout_btn = QPushButton("Cerrar sesión")
        logout_btn.setObjectName("btnCerrarSesion")
        logout_btn.clicked.connect(self.logout)
        layout.addWidget(logout_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(central_widget)

    def open_products_module(self):
        """Abrir ventana de gestión de productos"""
        self.products_window = ProductWindow(self)
        self.products_window.show()

    def open_billing_module(self):
        """Abrir ventana de facturación"""
        billing_window = BillingDialog(self)
        billing_window.exec()

    def open_inventory_module(self):
        """Abrir ventana de inventario"""
        inventory_window = InventoryDialog(self)
        inventory_window.exec()

    def open_provider_module(self):
        """Abrir ventana de proveedores"""
        provider_window = ProviderDialog(self)
        provider_window.exec()

    def open_client_module(self):
        """Abrir ventana de clientes"""
        client_window = ClientDialog(self)
        client_window.exec()

    def open_search_module(self):
        """Abrir ventana de búsqueda"""
        search_window = SearchDialog(self)
        search_window.exec()

    def logout(self):
        self.close()
        from View.login_view import LoginWindow
        self.login_window = LoginWindow()
        self.login_window.show()

# Mantener compatibilidad con el código existente
MainWindow = StartWindow