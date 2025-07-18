from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QPushButton, QLabel, QApplication
)
from PyQt6.QtCore import Qt
from View.product_view import ProductWindow
from View.billing_view import BillingDialog
from View.inventory_view import InventoryDialog
from View.provider_view import ProviderDialog
from View.client_view import ClientDialog

class StartWindow(QMainWindow):
    """Ventana principal de inicio del sistema"""
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Ferretería Mónaco - Inicio")
        self.setGeometry(200, 200, 800, 400)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Título principal
        title = QLabel("Sistema de Gestión - Ferretería Mónaco")
        title.setStyleSheet("font-size: 28px; font-weight: bold; margin-bottom: 30px; color: #2c3e50;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        # Subtítulo
        subtitle = QLabel("Selecciona un módulo para comenzar")
        subtitle.setStyleSheet("font-size: 16px; margin-bottom: 40px; color: #7f8c8d;")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(subtitle)

        # Layout para botones en dos filas
        buttons_main_layout = QVBoxLayout()
        
        # Primera fila de botones
        first_row_layout = QHBoxLayout()
        first_row_layout.setSpacing(20)
        
        # Botón para la gestión de productos
        products_btn = QPushButton("📦 Gestión de Productos")
        products_btn.setFixedSize(200, 60)
        products_btn.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                font-weight: bold;
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        products_btn.clicked.connect(self.open_products_module)
        first_row_layout.addWidget(products_btn)

        # Botón para la facturación
        billing_btn = QPushButton("💰 Facturación")
        billing_btn.setFixedSize(200, 60)
        billing_btn.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                font-weight: bold;
                background-color: #27ae60;
                color: white;
                border: none;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #229954;
            }
        """)
        billing_btn.clicked.connect(self.open_billing_module)
        first_row_layout.addWidget(billing_btn)

        # Botón para la gestión de inventario
        inventory_btn = QPushButton("📊 Gestión de Inventario")
        inventory_btn.setFixedSize(200, 60)
        inventory_btn.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                font-weight: bold;
                background-color: #e74c3c;
                color: white;
                border: none;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        inventory_btn.clicked.connect(self.open_inventory_module)
        first_row_layout.addWidget(inventory_btn)

        # Segunda fila de botones
        second_row_layout = QHBoxLayout()
        second_row_layout.setSpacing(20)
        
        # Botón para la gestión de proveedores
        provider_btn = QPushButton("🏢 Proveedores")
        provider_btn.setFixedSize(200, 60)
        provider_btn.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                font-weight: bold;
                background-color: #9b59b6;
                color: white;
                border: none;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #8e44ad;
            }
        """)
        provider_btn.clicked.connect(self.open_provider_module)
        second_row_layout.addWidget(provider_btn)
        
        # Botón para la gestión de clientes
        client_btn = QPushButton("👥 Clientes")
        client_btn.setFixedSize(200, 60)
        client_btn.setStyleSheet("""
            QPushButton {
                font-size: 14px;
                font-weight: bold;
                background-color: #f39c12;
                color: white;
                border: none;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #e67e22;
            }
        """)
        client_btn.clicked.connect(self.open_client_module)
        second_row_layout.addWidget(client_btn)

        # Centrar botones en la segunda fila
        second_row_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Agregar layouts de botones
        buttons_main_layout.addLayout(first_row_layout)
        buttons_main_layout.addSpacing(20)
        buttons_main_layout.addLayout(second_row_layout)

        layout.addLayout(buttons_main_layout)
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

# Mantener compatibilidad con el código existente
MainWindow = StartWindow