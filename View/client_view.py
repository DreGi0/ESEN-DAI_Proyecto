from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox,
    QTableWidget, QTableWidgetItem, QSpinBox, QLineEdit, QMessageBox, QFormLayout, Q
)
from Controller.client_controller import ClientController

class ClientDialog(QDialog):
    def __init__(self, parent=None, client_data=None):
        super().__init__(parent)
        self.controller = ClientController()
        self.setWindowTitle("Gestión de clientes")
        self.client_data = client_data
        self.setup_ui()
        self.load_clients()
        
        layout = QHBoxLayout()
        
        add_cliente_layout = QFormLayout()
        self.set_nombre_label = QLabel("Nombre")
        self.set_nombre = QLineEdit()
        self.set_apellido_label = QLabel("Apellido")
        self.set_apellido = QLineEdit()
        self.set_correo_label = QLabel("Correo")
        self.set_correo = QLineEdit()
        self.btn_add_client = QPushButton("Crear cliente")
        self.btn_add_client.clicked.connect(self.add_client)
        
        add_cliente_layout.addRow(self.set_nombre_label, self.set_nombre)
        add_cliente_layout.addRow(self.set_apellido_label, self.set_apellido)
        add_cliente_layout.addRow(self.set_correo_label, self.set_correo)

        
        layout.addLayout(add_cliente_layout)
        self.setLayout(layout)
        
    def add_client(self):
        nombre = self.set_nombre.text().strip()
        apellido = self.set_apellido.text().strip()
        correo = self.set_correo.text().strip()
        
        if not nombre or not apellido or not correo:
            QMessageBox.warning(self, "Error", "Campos vacíos. Todos los campos deben ser llenados")
            return
        
        add_success = self.controller.save_client(nombre, apellido, correo)
        
        if add_success:
            print("Cliente agregado con éxito")
            self.set_nombre.clear()
            self.set_apellido.clear()
            self.set_correo.clear()