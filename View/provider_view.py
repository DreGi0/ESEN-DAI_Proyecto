from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox,
    QTableWidget, QTableWidgetItem, QLineEdit, QMessageBox,
    QFormLayout, QTableWidget, QTableWidgetItem, QHeaderView, QWidget
)
from Controller.provider_controller import ProviderController

class ProviderDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.controller = ProviderController()
        self.setWindowTitle("Gestión de proveedores -- Ferretería Mónaco")
        self.resize(700, 500)
        self.setup_interface()
        self.load_provider()
        
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
        
        """ Sección de creación de proveedor (Create)"""  
        new_prov_layout = QFormLayout()
        self.new_prov_container = QWidget()
        self.new_prov_container.setLayout(new_prov_layout)
        self.new_prov_container.setVisible(False)
        
        self.text_nombre = QLabel("Nombre:")
        self.nombre_prov = QLineEdit()
        
        self.text_apellido = QLabel("Apellido:")
        self.apellido_prov = QLineEdit()
        
        self.btn_crear_prov = QPushButton("Agregar proveedor")
        self.btn_cancelar = QPushButton("Cancelar")
        
        # agregar al layout new para poder ocultarlo:
        new_prov_layout.addWidget(QLabel("Agregue un nuevo Proveedor"))
        new_prov_layout.addRow(self.text_nombre, self.nombre_prov)
        new_prov_layout.addRow(self.text_apellido, self.apellido_prov)
        new_prov_layout.addWidget(self.btn_crear_prov)
        
        # Agregar un botón para agregar un proveedor y mostrar el layout.
        self.btn_new = QPushButton("Nuevo proveedor")
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
        self.edit_lay.addWidget(QLabel("Elige el proveedor que quieres editar"))
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
        layout.addWidget(self.new_prov_container)
        layout.addWidget(self.table)
        layout.addWidget(self.container_btn)
        layout.addWidget(self.edit_container)
        layout.addWidget(self.del_container)
        layout.addWidget(self.btn_cancelar)

        self.setLayout(layout)
        
        # conectar señales de botones
        self.btn_crear_prov.clicked.connect(self.create_provider)
        self.btn_new.clicked.connect(self.show_new_lay)
        self.btn_cancelar.clicked.connect(self.cancelar)
        self.btn_edit.clicked.connect(self.show_edit_lay)
        self.btn_actualizar.clicked.connect(self.update_provider)
        self.btn_del.clicked.connect(self.show_del_provider)
        self.btn_eliminar.clicked.connect(self.delete_provider)

    def create_provider(self):
        nombre_prov = self.nombre_prov.text().strip()
        apellido_prov = self.apellido_prov.text().strip()
        
        if not nombre_prov or not apellido_prov:
            QMessageBox.warning(self, "Error", "Debe completar los datos antes de continuar")
            return
        
        success = self.controller.create_provider(nombre_prov, apellido_prov)
        
        if success:
            QMessageBox.information(self, "Éxito", "Proveedor agregado correctamente.")
            self.load_provider()  # Refresca la tabla
            self.nombre_prov.clear()
            self.apellido_prov.clear()
        else:
            QMessageBox.critical(self, "Error", "Error al guardar el proveedor.")
    
    
    def load_provider(self):
        """Cargar proveedores desde la base de datos"""    
        provider = self.controller.load_provider()
        self.table.setRowCount(len(provider))
        for row, (id_prov, nombre_prov, apellido_prov) in enumerate(provider):
            self.table.setItem(row, 0, QTableWidgetItem(str(id_prov)))
            self.table.setItem(row, 1, QTableWidgetItem(str(nombre_prov)))
            self.table.setItem(row, 2, QTableWidgetItem(str(apellido_prov)))
    
    def update_provider(self):
        nombre = self.nombre_edit.text().strip()
        apellido = self.apellido_edit.text().strip()
        id_prov = int(self.elegir_id.currentText())
        
        if not apellido or not nombre or not id_prov:
            QMessageBox.critical(self,"Error", "Debe completar los datos antes de continuar")
            return
        success = self.controller.update_provider(id_prov, nombre, apellido)
        
        if success:
            QMessageBox.information(self, "Éxito", "Proveedor actualizado correctamente.")
        else:
            QMessageBox.critical(self, "Error", "Error al actualizar el proveedor.")

    def delete_provider(self):
        id_prov = int(self.elegir_id_del.currentText().strip())
        
        if not id_prov:
            QMessageBox.critical(self,"Error", "Debe completar los datos antes de continuar")
            return
        success = self.controller.remove_provider(id_prov)
        
        if success:
            QMessageBox.information(self, "Éxito", "Proveedor eliminado correctamente.")
        else:
            QMessageBox.critical(self, "Error", "Error al eliminar el proveedor.")
            
    def show_new_lay(self):
        """Mostrar el layout oculto"""
        if self.new_prov_container.isVisible():
            self.new_prov_container.hide()
            # Mostrar tabla de infromación
            self.table.setVisible(True)
            #Mostrar/ocultar botones
            self.container_btn.setVisible(True)
            self.btn_cancelar.setVisible(False)
        else:
            self.new_prov_container.show()
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
            self.new_prov_container.hide()
            #Ocultar tabla de información
            self.table.setVisible(False)
            #Mostrar/ocultar botones
            self.container_btn.setVisible(False)
            self.btn_cancelar.setVisible(True)
            
            self.prov_ids()
            
    def show_del_provider(self):
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
            self.new_prov_container.hide()
            #Ocultar tabla de información
            self.table.setVisible(False)
            #Mostrar/ocultar botones
            self.container_btn.setVisible(False)
            self.btn_cancelar.setVisible(True)
            
            self.prov_ids()
            
    def prov_ids(self):
        self.elegir_id.clear()
        self.elegir_id_del.clear()
        prov = self.controller.get_providers()
        for id_prov, _, _ in prov:
            self.elegir_id.addItem(str(id_prov))
            self.elegir_id_del.addItem(str(id_prov))
        
    def cancelar(self):
        """ Regresar a pantalla principal de Proveedor"""
        #ocultar layouts
        self.new_prov_container.hide()
        self.edit_container.hide()
        self.del_container.hide()
        
        #Mostrar info
        self.table.setVisible(True)
        self.container_btn.setVisible(True)
        self.btn_cancelar.setVisible(False)
        
        #Limpiar
        self.nombre_prov.clear()
        self.apellido_prov.clear()