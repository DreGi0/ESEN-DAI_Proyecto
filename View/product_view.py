from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QPushButton, QTableWidget, QTableWidgetItem, QMessageBox,
    QInputDialog, QComboBox, QLabel, QLineEdit, QDialog,
    QFormLayout, QDialogButtonBox, QTextEdit, QHeaderView, QSizePolicy, QAbstractScrollArea
)
from PyQt6.QtCore import Qt
from Controller.product_controller import ProductController

class ProductDialog(QDialog):
    """Dialog para crear/editar productos"""
    def __init__(self, parent=None, product_data=None):
        super().__init__(parent)

        self.product_controller = ProductController()

        self.product_data = product_data
        self.setup_ui()
        self.load_data()
        
        if product_data:
            self.setWindowTitle("Editar Producto")
            self.fill_form()
        else:
            self.setWindowTitle("Crear Producto")

    def setup_ui(self):
        self.setModal(True)
        self.resize(400, 300)
        
        layout = QFormLayout()
        
        # Campos del formulario
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Ej: Tornillo")
        self.description_input = QTextEdit()
        self.description_input.setMaximumHeight(80)
        self.description_input.setPlaceholderText("Ej: Tornillo de acero inoxidable")
        self.location_input = QLineEdit()
        self.location_input.setPlaceholderText("Ej: Pasillo 1")
        self.price_input = QLineEdit()
        self.price_input.setPlaceholderText("Ej: 12.50")
        self.category_combo = QComboBox()
        self.unit_combo = QComboBox()
        
        # Agregar campos al formulario
        layout.addRow("Nombre:", self.name_input)
        layout.addRow("Descripción:", self.description_input)
        layout.addRow("Ubicación:", self.location_input)
        layout.addRow("Precio:", self.price_input)
        layout.addRow("Categoría:", self.category_combo)
        layout.addRow("Unidad de Medida:", self.unit_combo)
        
        # Botones
        self.button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        
        layout.addRow(self.button_box)
        self.setLayout(layout)

    def load_data(self):
        """Cargar datos de categorías y unidades"""
        # Cargar categorías
        categories = self.product_controller.get_porduct_categories()
        for cat_id, cat_name in categories:
            self.category_combo.addItem(cat_name, cat_id)
        
        # Cargar unidades
        units = self.product_controller.get_units()
        for unit_id, unit_name, unit_abbr in units:
            self.unit_combo.addItem(f"{unit_name} ({unit_abbr})", unit_id)

    def fill_form(self):
        """Llenar formulario con datos del producto"""
        if self.product_data:
            self.name_input.setText(self.product_data[1])
            self.description_input.setText(self.product_data[2])
            self.location_input.setText(self.product_data[4])
            self.price_input.setText(str(self.product_data[3]))
            
            # Seleccionar categoría
            cat_id = self.product_data[5]
            for i in range(self.category_combo.count()):
                if self.category_combo.itemData(i) == cat_id:
                    self.category_combo.setCurrentIndex(i)
                    break
            
            # Seleccionar unidad
            unit_id = self.product_data[6]
            for i in range(self.unit_combo.count()):
                if self.unit_combo.itemData(i) == unit_id:
                    self.unit_combo.setCurrentIndex(i)
                    break

    def get_data(self):
        """Obtener datos del formulario"""
        return {
            'nombre': self.name_input.text().strip(),
            'descripcion': self.description_input.toPlainText().strip(),
            'ubicacion': self.location_input.text().strip(),
            'precio': self.price_input.text().strip(),
            'id_categoria': self.category_combo.currentData(),
            'id_unidad': self.unit_combo.currentData()
        }

class ProductWindow(QMainWindow):
    """Ventana principal para la gestión de productos"""
    def __init__(self, parent=None):
        super().__init__(parent)

        self.product_controller = ProductController()

        self.setup_ui()
        self.load_products()

    def setup_ui(self):
        self.setWindowTitle("Gestión de Productos - Ferretería Mónaco")
        self.setGeometry(100, 100, 1200, 800)
        
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal con márgenes y espaciado
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(20)
        central_widget.setLayout(main_layout)
        
        # Título
        title = QLabel("Gestión de Productos")
        title.setProperty("cssClass", "title")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)

        # Descripción
        desc_label = QLabel("Administra los productos de la ferretería. "
                            "Puedes crear, editar, eliminar productos y gestionar sus proveedores.")
        desc_label.setProperty("cssClass", "subtitle")
        desc_label.setWordWrap(True)
        main_layout.addWidget(desc_label)
        
        # Botones de acción
        button_layout = QHBoxLayout()
        button_layout.setSpacing(18)
        
        self.create_btn = QPushButton("Crear Producto")
        self.edit_btn = QPushButton("Editar")
        self.delete_btn = QPushButton("Eliminar")
        self.view_btn = QPushButton("Detalles")
        self.suppliers_btn = QPushButton("Proveedores")
        self.refresh_btn = QPushButton("Actualizar")
        self.back_btn = QPushButton("Volver")
        
        # Ajustar tamaño mínimo solo para estos botones
        for btn in [
            self.create_btn, self.edit_btn, self.delete_btn, self.view_btn,
            self.suppliers_btn, self.refresh_btn, self.back_btn
        ]:
            btn.setMinimumWidth(120)
            btn.setMaximumWidth(180)
            btn.setMinimumHeight(36)
            btn.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        
        button_layout.addWidget(self.create_btn)
        button_layout.addWidget(self.edit_btn)
        button_layout.addWidget(self.delete_btn)
        button_layout.addWidget(self.view_btn)
        button_layout.addWidget(self.suppliers_btn)
        button_layout.addWidget(self.refresh_btn)
        button_layout.addWidget(self.back_btn)
        
        main_layout.addLayout(button_layout)
        
        # Tabla de productos
        self.products_table = QTableWidget()
        self.products_table.setMinimumWidth(1100)
        self.products_table.setMinimumHeight(400)
        self.products_table.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.products_table.setShowGrid(True)
        # Selección por fila completa y solo una fila a la vez
        self.products_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.products_table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        main_layout.addWidget(self.products_table)
        
        # Conectar señales
        self.connect_signals()

    def connect_signals(self):
        """Conectar señales de botones"""
        self.create_btn.clicked.connect(self.create_product)
        self.edit_btn.clicked.connect(self.edit_product)
        self.delete_btn.clicked.connect(self.delete_product)
        self.view_btn.clicked.connect(self.view_product_details)
        self.suppliers_btn.clicked.connect(self.manage_suppliers)
        self.refresh_btn.clicked.connect(self.load_products)
        self.back_btn.clicked.connect(self.close)

    def load_products(self):
        """Cargar productos en la tabla"""
        products = self.product_controller.get_products()
        self.products_table.clearContents()
        self.products_table.setRowCount(len(products))
        self.products_table.setColumnCount(6)
        self.products_table.setHorizontalHeaderLabels([
            "ID", "Nombre", "Descripción", "Precio", "Ubicación", "Categoría"
        ])
        for row, product in enumerate(products):
            self.products_table.setItem(row, 0, QTableWidgetItem(str(product[0])))
            self.products_table.setItem(row, 1, QTableWidgetItem(product[1]))
            self.products_table.setItem(row, 2, QTableWidgetItem(product[2]))
            self.products_table.setItem(row, 3, QTableWidgetItem(f"${product[3]:.2f}"))
            self.products_table.setItem(row, 4, QTableWidgetItem(product[4]))
            self.products_table.setItem(row, 5, QTableWidgetItem(product[5] or "Sin categoría"))
        # Ajustar columnas: expandir todas proporcionalmente
        header = self.products_table.horizontalHeader()
        for col in range(self.products_table.columnCount()):
            header.setSectionResizeMode(col, QHeaderView.ResizeMode.Stretch)
        # Centrar texto en encabezados y celdas
        for col in range(self.products_table.columnCount()):
            item = self.products_table.horizontalHeaderItem(col)
            if item:
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        for row in range(self.products_table.rowCount()):
            for col in range(self.products_table.columnCount()):
                cell = self.products_table.item(row, col)
                if cell:
                    cell.setTextAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
        # Mostrar el número de filas correctamente en el encabezado vertical
        self.products_table.setVerticalHeaderLabels([str(i+1) for i in range(len(products))])

    def create_product(self):
        """Crear nuevo producto"""
        dialog = ProductDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            data = dialog.get_data()
            
            # Validar datos
            if not all([data['nombre'], data['descripcion'], data['precio']]):
                QMessageBox.warning(self, "Error", "Todos los campos son obligatorios")
                return
            
            try:
                precio = float(data['precio'])
                if precio <= 0:
                    raise ValueError("El precio debe ser mayor a 0")
            except ValueError:
                QMessageBox.warning(self, "Error", "El precio debe ser un número válido mayor a 0")
                return
            
            # Crear producto
            if self.product_controller.create_product(data['nombre'], data['descripcion'], data['ubicacion'], 
                            precio, data['id_categoria'], data['id_unidad']):
                QMessageBox.information(self, "Éxito", "Producto creado exitosamente")
                self.load_products()
            else:
                QMessageBox.critical(self, "Error", "No se pudo crear el producto")

    def edit_product(self):
        """Editar producto seleccionado"""
        current_row = self.products_table.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Advertencia", "Seleccione un producto para editar")
            return
        
        product_id = int(self.products_table.item(current_row, 0).text())
        product_data = self.product_controller.get_product_by_id(product_id)
        
        if not product_data:
            QMessageBox.critical(self, "Error", "No se pudo obtener los datos del producto")
            return
        
        dialog = ProductDialog(self, product_data)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            data = dialog.get_data()
            
            # Validar datos
            if not all([data['nombre'], data['descripcion'], data['precio']]):
                QMessageBox.warning(self, "Error", "Todos los campos son obligatorios")
                return
            
            try:
                precio = float(data['precio'])
                if precio <= 0:
                    raise ValueError("El precio debe ser mayor a 0")
            except ValueError:
                QMessageBox.warning(self, "Error", "El precio debe ser un número válido mayor a 0")
                return
            
            # Actualizar producto
            if self.product_controller.update_product(product_id, data['nombre'], data['descripcion'], 
                            data['ubicacion'], precio, data['id_categoria'], data['id_unidad']):
                QMessageBox.information(self, "Éxito", "Producto actualizado exitosamente")
                self.load_products()
            else:
                QMessageBox.critical(self, "Error", "No se pudo actualizar el producto")

    def delete_product(self):
        """Eliminar producto seleccionado"""
        current_row = self.products_table.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Advertencia", "Seleccione un producto para eliminar")
            return
        
        product_id = int(self.products_table.item(current_row, 0).text())
        product_name = self.products_table.item(current_row, 1).text()
        
        # Confirmar eliminación
        reply = QMessageBox.question(self, "Confirmar", 
                                   f"¿Está seguro de eliminar el producto '{product_name}'?",
                                   QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            if self.product_controller.delete_product(product_id):
                QMessageBox.information(self, "Éxito", "Producto eliminado exitosamente")
                self.load_products()
            else:
                QMessageBox.critical(self, "Error", "No se pudo eliminar el producto")

    def view_product_details(self):
        """Ver detalles del producto seleccionado"""
        current_row = self.products_table.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Advertencia", "Seleccione un producto para ver detalles")
            return
        
        product_id = int(self.products_table.item(current_row, 0).text())
        product_data = self.product_controller.get_product_by_id(product_id)
        
        if not product_data:
            QMessageBox.critical(self, "Error", "No se pudo obtener los datos del producto")
            return
        
        # Obtener proveedores
        suppliers = self.product_controller.get_product_suppliers(product_id)
        suppliers_text = "\n".join([f"• {sup[3]} {sup[4]} - Precio: ${sup[1]:.2f}" 
                                   for sup in suppliers]) if suppliers else "Sin proveedores asignados"
        
        details = f"""
DETALLES DEL PRODUCTO

ID: {product_data[0]}
Nombre: {product_data[1]}
Descripción: {product_data[2]}
Precio Unitario: ${product_data[3]:.2f}
Ubicación: {product_data[4]}
Categoría: {product_data[7] or 'Sin categoría'}
Unidad de Medida: {product_data[8] or 'Sin unidad'}

PROVEEDORES:
{suppliers_text}
        """
        
        QMessageBox.information(self, "Detalles del Producto", details)

    def manage_suppliers(self):
        """Gestionar proveedores del producto seleccionado"""
        current_row = self.products_table.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Advertencia", "Seleccione un producto para gestionar proveedores")
            return
        
        product_id = int(self.products_table.item(current_row, 0).text())
        product_name = self.products_table.item(current_row, 1).text()
        
        # Obtener proveedores disponibles
        suppliers = self.product_controller.get_suppliers()
        if not suppliers:
            QMessageBox.information(self, "Info", "No hay proveedores registrados")
            return
        
        # Crear lista de proveedores
        supplier_names = [f"{sup[1]} {sup[2]}" for sup in suppliers]
        
        # Diálogo para seleccionar proveedor
        supplier_name, ok = QInputDialog.getItem(self, "Asignar Proveedor", 
                                               f"Seleccione un proveedor para '{product_name}':",
                                               supplier_names, 0, False)
        
        if ok and supplier_name:
            # Obtener ID del proveedor seleccionado
            supplier_id = suppliers[supplier_names.index(supplier_name)][0]
            
            # Obtener precio de compra
            price, ok = QInputDialog.getDouble(self, "Precio de Compra", 
                                             f"Ingrese el precio de compra para '{supplier_name}':",
                                             0.0, 0.0, 9999.99, 2)
            
            if ok:
                if self.product_controller.assign_supplier_to_product(product_id, supplier_id, price):
                    QMessageBox.information(self, "Éxito", "Proveedor asignado exitosamente")
                else:
                    QMessageBox.critical(self, "Error", "No se pudo asignar el proveedor")