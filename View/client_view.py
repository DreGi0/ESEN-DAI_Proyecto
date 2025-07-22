from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox,
    QTableWidget, QTableWidgetItem, QLineEdit, QMessageBox,
    QFormLayout, QHeaderView, QWidget
)
from Controller.client_controller import ClientController
from PyQt6.QtCore import Qt

class ClientDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.client_controller = ClientController()
        self.setWindowTitle("Gestión de clientes -- Ferretería Mónaco")
        self.resize(700, 650)  # Más alto
        self.setup_interface()
        self.load_cliente()
        
    def setup_interface(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        # --- Descripción ---
        desc_label = QLabel("Administra los clientes registrados en el sistema. "
                            "Puedes agregar, editar o eliminar clientes según sea necesario.")
        desc_label.setWordWrap(True)
        desc_label.setStyleSheet("font-size: 15px; color: #555; margin-bottom: 10px;")
        layout.addWidget(desc_label)

        # --- Tabla de clientes (Read) ---
        self.table = QTableWidget()
        self.table.setMinimumWidth(600)
        self.table.setMinimumHeight(320)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Nombre", "Apellido"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)

        # --- Sección de creación (Create) ---
        new_client_layout = QFormLayout()
        self.new_client_container = QWidget()
        self.new_client_container.setLayout(new_client_layout)
        self.new_client_container.setVisible(False)

        self.text_nombre = QLabel("Nombre:")
        self.nombre_cliente = QLineEdit()
        self.nombre_cliente.setPlaceholderText("Ej: Juan")
        self.text_apellido = QLabel("Apellido:")
        self.apellido_cliente = QLineEdit()
        self.apellido_cliente.setPlaceholderText("Ej: Pérez")
        self.btn_crear_cliente = QPushButton("Agregar cliente")
        self.btn_cancelar = QPushButton("Cancelar")
        self.btn_cancelar.setVisible(False)
        self.btn_cancelar.setFixedWidth(150)
        self.btn_cancelar.setStyleSheet("background-color: red; color: white")

        new_client_layout.addWidget(QLabel("Agregue un nuevo Cliente"))
        new_client_layout.addRow(self.text_nombre, self.nombre_cliente)
        new_client_layout.addRow(self.text_apellido, self.apellido_cliente)
        new_client_layout.addWidget(self.btn_crear_cliente)

        # --- Sección de actualización (Update) ---
        self.btn_edit = QPushButton("Editar")
        self.btn_edit.setFixedWidth(150)
        self.edit_lay = QFormLayout()
        self.edit_container = QWidget()
        self.edit_container.setLayout(self.edit_lay)
        self.edit_container.setVisible(False)
        self.elegir_id = QComboBox()
        self.nombre_edit = QLineEdit()
        self.nombre_edit.setPlaceholderText("Ej: Juan")
        self.apellido_edit = QLineEdit()
        self.apellido_edit.setPlaceholderText("Ej: Pérez")
        self.btn_actualizar = QPushButton("Actualizar")
        self.btn_actualizar.setFixedWidth(150)
        self.edit_lay.addWidget(QLabel("Elige el cliente que deseas editar"))
        self.edit_lay.addRow(QLabel("ID:"), self.elegir_id)
        self.edit_lay.addRow(QLabel("Nombre:"), self.nombre_edit)
        self.edit_lay.addRow(QLabel("Apellido:"), self.apellido_edit)
        self.edit_lay.addWidget(self.btn_actualizar)

        # --- Sección de eliminación (Delete) ---
        self.btn_del = QPushButton("Eliminar")
        self.btn_del.setFixedWidth(150)
        self.del_lay = QFormLayout()
        self.del_container = QWidget()
        self.del_container.setLayout(self.del_lay)
        self.del_container.setVisible(False)
        self.elegir_id_del = QComboBox()
        self.btn_eliminar = QPushButton("Eliminar registro")
        self.btn_eliminar.setFixedWidth(150)
        self.del_lay.addWidget(QLabel("Elige el cliente que deseas eliminar"))
        self.del_lay.addRow(QLabel("ID:"), self.elegir_id_del)
        self.del_lay.addWidget(self.btn_eliminar)

        # --- Botones principales ---
        self.btn_new = QPushButton("Nuevo cliente")
        self.btn_new.setFixedWidth(180)
        self.lay_btn = QHBoxLayout()
        self.lay_btn.setSpacing(20)
        self.container_btn = QWidget()
        self.container_btn.setLayout(self.lay_btn)
        self.lay_btn.addWidget(self.btn_new)
        self.lay_btn.addWidget(self.btn_edit)
        self.lay_btn.addWidget(self.btn_del)

        # --- Agregar al layout principal ---
        layout.addWidget(self.new_client_container)
        layout.addWidget(self.table)
        layout.addWidget(self.container_btn)
        layout.addWidget(self.edit_container)
        layout.addWidget(self.del_container)
        layout.addWidget(self.btn_cancelar)

        # Botón regresar (idéntico a proveedores)
        self.btn_regresar = QPushButton("Regresar")
        self.btn_regresar.setStyleSheet("background-color: #e74c3c; color: white;")
        self.btn_regresar.setMinimumHeight(48)
        self.btn_regresar.clicked.connect(self.close)
        layout.addWidget(self.btn_regresar)

        self.setLayout(layout)

        # Conectar señales
        self.btn_crear_cliente.clicked.connect(self.create_cliente)
        self.btn_new.clicked.connect(self.show_new_lay)
        self.btn_cancelar.clicked.connect(self.cancelar)
        self.btn_edit.clicked.connect(self.show_edit_lay)
        self.btn_actualizar.clicked.connect(self.update_cliente)
        self.btn_del.clicked.connect(self.show_del_cliente)
        self.btn_eliminar.clicked.connect(self.delete_cliente)
        
    def create_cliente(self):
        nombre_cliente = self.nombre_cliente.text().strip()
        apellido_cliente = self.apellido_cliente.text().strip()
        
        if not nombre_cliente or not apellido_cliente:
            QMessageBox.warning(self, "Error", "Debe completar los datos antes de continuar")
            return
        
        success = self.client_controller.create_client(nombre_cliente, apellido_cliente)
        
        if success:
            self.mostrar_mensaje_success("Cliente agregado correctamente.")
            self.load_cliente()
            self.nombre_cliente.clear()
            self.apellido_cliente.clear()
        else:
            QMessageBox.critical(self, "Error", "Error al guardar el cliente.")
    
    
    def load_cliente(self):
        """Cargar clientes desde la base de datos"""    
        cliente = self.client_controller.load_client()
        self.table.clearContents()
        self.table.setRowCount(len(cliente))
        for row, (id_cliente, nombre_cliente, apellido_cliente) in enumerate(cliente):
            self.table.setItem(row, 0, QTableWidgetItem(str(id_cliente)))
            self.table.setItem(row, 1, QTableWidgetItem(str(nombre_cliente)))
            self.table.setItem(row, 2, QTableWidgetItem(str(apellido_cliente)))
        self.table.resizeColumnsToContents()
        header = self.table.horizontalHeader()
        for col in range(self.table.columnCount()):
            header.setSectionResizeMode(col, QHeaderView.ResizeMode.Stretch)
        # Centrar texto en encabezados y celdas
        for col in range(self.table.columnCount()):
            item = self.table.horizontalHeaderItem(col)
            if item:
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount()):
                cell = self.table.item(row, col)
                if cell:
                    cell.setTextAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
        # Mostrar el número de filas correctamente en el encabezado vertical
        self.table.setVerticalHeaderLabels([str(i+1) for i in range(len(cliente))])
    
    def update_cliente(self):
        nombre = self.nombre_edit.text().strip()
        apellido = self.apellido_edit.text().strip()
        id_cliente = int(self.elegir_id.currentText())
        
        if not apellido or not nombre or not id_cliente:
            QMessageBox.critical(self,"Error", "Debe completar los datos antes de continuar")
            return
        success = self.client_controller.update_client(id_cliente, nombre, apellido)
        
        if success:
            self.mostrar_mensaje_success("Cliente actualizado correctamente.")
        else:
            QMessageBox.critical(self, "Error", "Error al actualizar el cliente.")

    def delete_cliente(self):
        id_cliente = int(self.elegir_id_del.currentText().strip())
        
        if not id_cliente:
            QMessageBox.critical(self,"Error", "Debe completar los datos antes de continuar")
            return
        success = self.client_controller.remove_client(id_cliente)
        
        if success:
            self.mostrar_mensaje_success("Cliente eliminado correctamente.")
        else:
            QMessageBox.critical(self, "Error", "Error al eliminar el Cliente.")
            
    def show_new_lay(self):
        """Mostrar el layout oculto"""
        if self.new_client_container.isVisible():
            self.new_client_container.hide()
            # Mostrar tabla de infromación
            self.table.setVisible(True)
            #Mostrar/ocultar botones
            self.container_btn.setVisible(True)
            self.btn_cancelar.setVisible(False)
        else:
            self.new_client_container.show()
            self.edit_container.hide()
            #Ocultar tabla de información
            self.table.setVisible(False)
            #Mostrar/ocultar botones
            self.container_btn.setVisible(False)
            self.btn_cancelar.setVisible(True)
            
    def show_edit_lay(self):
        """ Mostrar el layout editar oculto"""
        if self.edit_container.isVisible():
            self.edit_container.hide()
            # Mostrar tabla de infromación
            self.table.setVisible(True)
            #Mostrar/ocultar botones
            self.container_btn.setVisible(True)
            self.btn_cancelar.setVisible(False)
        else:
            self.edit_container.show()
            self.new_client_container.hide()
            #Ocultar tabla de información
            self.table.setVisible(False)
            #Mostrar/ocultar botones
            self.container_btn.setVisible(False)
            self.btn_cancelar.setVisible(True)
            
            self.cliente_ids()
            
    def show_del_cliente(self):
        """ Mostrar el layout oculto"""
        if self.del_container.isVisible():
            self.del_container.setVisible(False)
            # Mostrar tabla de infromación
            self.table.setVisible(True)
            #Mostrar/ocultar botones
            self.container_btn.setVisible(True)
            self.btn_cancelar.setVisible(False)
        else:
            self.del_container.show()
            self.edit_container.hide()
            self.new_client_container.hide()
            #Ocultar tabla de información
            self.table.setVisible(False)
            #Mostrar/ocultar botones
            self.container_btn.setVisible(False)
            self.btn_cancelar.setVisible(True)
            
            self.cliente_ids()
            
    def cliente_ids(self):
        self.elegir_id.clear()
        self.elegir_id_del.clear()
        cliente = self.client_controller.get_all_clientes()
        for id_cliente, _, _ in cliente:
            self.elegir_id.addItem(str(id_cliente))
            self.elegir_id_del.addItem(str(id_cliente))
        
    def cancelar(self):
        """ Regresar a pantalla principal de Cliente"""
        #ocultar layouts
        self.new_client_container.hide()
        self.edit_container.hide()
        self.del_container.hide()
        
        #Mostrar info
        self.table.setVisible(True)
        self.container_btn.setVisible(True)
        self.btn_cancelar.setVisible(False)
        
        #Limpiar
        self.nombre_cliente.clear()
        self.apellido_cliente.clear()
    
    # Personalizar mensaje de Success 
    def mostrar_mensaje_success(self, msg):
        mensaje = QMessageBox(self)
        mensaje.setWindowTitle("Éxito")
        mensaje.setText(msg)
        mensaje.setIcon(QMessageBox.Icon.Information)
        mensaje.setStandardButtons(QMessageBox.StandardButton.Ok)
        mensaje.buttonClicked.connect(lambda: self.cancelar())
        mensaje.exec()