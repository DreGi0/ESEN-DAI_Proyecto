from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox,
    QTableWidget, QTableWidgetItem, QLineEdit, QMessageBox,
    QFormLayout, QTableWidget, QTableWidgetItem, QHeaderView, QWidget
)
from Controller.client_controller import ClientController

class ClientDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.client_controller = ClientController()
        self.setWindowTitle("Gestión de clientes -- Ferretería Mónaco")
        self.resize(700, 500)
        self.setup_interface()
        self.load_cliente()
        
    def setup_interface(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(5)
                
        """ Sección de visualización (Read)""" 
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Nombre", "Apellido"]) 
        self.table.setMinimumHeight(300) 
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)      
        self.setVisible(True)
        
        """ Sección de creación de cliente (Create)"""  
        new_client_lay = QFormLayout()
        self.new_client_container = QWidget()
        self.new_client_container.setLayout(new_client_lay)
        self.new_client_container.setVisible(False)
        
        self.text_nombre = QLabel("Nombre:")
        self.nombre_cliente = QLineEdit()
        
        self.text_apellido = QLabel("Apellido:")
        self.apellido_cliente = QLineEdit()
        
        self.btn_crear_cliente = QPushButton("Agregar cliente")
        self.btn_cancelar = QPushButton("Cancelar")
        
        # agregar al layout new para poder ocultarlo:
        new_client_lay.addWidget(QLabel("Agregue un nuevo cliente"))
        new_client_lay.addRow(self.text_nombre, self.nombre_cliente)
        new_client_lay.addRow(self.text_apellido, self.apellido_cliente)
        new_client_lay.addWidget(self.btn_crear_cliente)
        
        # Agregar un botón para agregar un cliente y mostrar el layout.
        self.btn_new = QPushButton("Nuevo cliente")
        self.btn_new.setFixedWidth(180)
        self.btn_cancelar.setVisible(False)
        self.btn_cancelar.setFixedWidth(150)
        self.btn_cancelar.setStyleSheet("background-color: red; color: white")
                
        """ Sección actualizar (Update)"""
        
        self.btn_edit = QPushButton("Editar")
        self.btn_edit.setFixedWidth(150)        
        
        # Crear layout edit para poder ocultarlo
        self.edit_lay = QFormLayout()
        self.edit_container = QWidget()
        self.edit_container.setLayout(self.edit_lay)
        self.edit_container.setVisible(False)
        
        self.elegir_id = QComboBox()
        self.nombre_edit = QLineEdit()
        self.apellido_edit = QLineEdit()
        self.btn_actualizar = QPushButton("Actualizar")
        self.btn_actualizar.setFixedWidth(150)
        
        # agregar al contenedor edit
        self.edit_lay.addWidget(QLabel("Elige el cliente que deseas editar"))
        self.edit_lay.addRow(QLabel("ID:"),self.elegir_id )
        self.edit_lay.addRow(QLabel("Nombre:"), self.nombre_edit)
        self.edit_lay.addRow(QLabel("Apellido:"), self.apellido_edit)
        self.edit_lay.addWidget(self.btn_actualizar)
                        
        """ Sección Eliminar (Delete)"""
        
        self.btn_del = QPushButton("Eliminar")
        self.btn_del.setFixedWidth(150)
        
        # Crear layout Delete para poder ocultarlo
        self.del_lay = QFormLayout()
        self.del_container = QWidget()
        self.del_container.setLayout(self.del_lay)
        self.del_container.setVisible(False)
        
        self.del_lay.addWidget(QLabel("Elige el cliente que deseas eliminar"))
        self.elegir_id_del = QComboBox()
        self.btn_eliminar = QPushButton("Eliminar registro")
        self.btn_eliminar.setFixedWidth(150)  
        
        # agregar al layout delete
        self.del_lay.addRow(QLabel("ID:"), self.elegir_id_del)   
        self.del_lay.addWidget(self.btn_eliminar)  
        
        # Agregar botones al layout
        self.lay_btn = QHBoxLayout()
        self.container_btn = QWidget()
        self.container_btn.setLayout(self.lay_btn)
        
        self.lay_btn.addWidget(self.btn_new)
        self.lay_btn.addWidget(self.btn_edit)
        self.lay_btn.addWidget(self.btn_del)
        
        # Agregar al layout principal
        layout.addWidget(self.new_client_container)
        layout.addWidget(self.table)
        layout.addWidget(self.container_btn)
        layout.addWidget(self.edit_container)
        layout.addWidget(self.del_container)
        layout.addWidget(self.btn_cancelar)

        self.setLayout(layout)
        
        # conectar señales de botones
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
        self.table.setRowCount(len(cliente))
        for row, (id_cliente, nombre_cliente, apellido_cliente) in enumerate(cliente):
            self.table.setItem(row, 0, QTableWidgetItem(str(id_cliente)))
            self.table.setItem(row, 1, QTableWidgetItem(str(nombre_cliente)))
            self.table.setItem(row, 2, QTableWidgetItem(str(apellido_cliente)))
    
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