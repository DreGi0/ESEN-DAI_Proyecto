from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox,
    QTableWidget, QTableWidgetItem, QSpinBox, QLineEdit, QMessageBox,
    QHeaderView
)
from Controller.inventory_controller import InventoryController
from Controller.product_controller import ProductController
from PyQt6.QtCore import Qt

class InventoryDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.inventory_controller = InventoryController()
        self.product_controller = ProductController()
        self.setWindowTitle("Gestión de Inventario -- Ferretería Mónaco")
        self.resize(900, 600)  # Más ancho y alto
        self.setup_interface()
        self.load_product_options()

    def setup_interface(self):
        """Construye la interfaz gráfica"""
        layout = QVBoxLayout()

        # Descripción
        desc_label = QLabel("Registra entradas y salidas de productos en el inventario. "
                            "Selecciona el producto, la cantidad y el tipo de movimiento, luego haz clic en 'Agregar'. "
                            "Guarda los cambios para registrar los movimientos.")
        desc_label.setWordWrap(True)
        desc_label.setStyleSheet("font-size: 15px; color: #555; margin-bottom: 10px;")
        layout.addWidget(desc_label)

        # Selección de producto, cantidad y tipo de movimiento
        form_layout = QHBoxLayout()
        form_layout.addWidget(QLabel("Producto:"))

        self.product_combo = QComboBox()
        self.product_combo.setMinimumWidth(200)
        self.product_combo.currentIndexChanged.connect(self.update_stock_label)
        form_layout.addWidget(self.product_combo)

        self.stock_label = QLabel("Stock actual: -")
        form_layout.addWidget(self.stock_label)

        form_layout.addWidget(QLabel("Cantidad:"))
        self.qty_input = QSpinBox()
        self.qty_input.setMinimum(1)
        self.qty_input.setMaximum(1000)
        form_layout.addWidget(self.qty_input)

        form_layout.addWidget(QLabel("Movimiento:"))
        self.movement_type_combo = QComboBox()
        self.movement_type_combo.addItems(["Entrada", "Salida"])
        form_layout.addWidget(self.movement_type_combo)

        self.add_movement_btn = QPushButton("Agregar")
        self.add_movement_btn.clicked.connect(self.register_movement)
        self.add_movement_btn.setMinimumWidth(120)
        form_layout.addWidget(self.add_movement_btn)

        layout.addLayout(form_layout)

        # Tabla de movimientos
        self.movements_table = QTableWidget(0, 4)
        self.movements_table.setMinimumWidth(850)
        self.movements_table.setMinimumHeight(300)
        self.movements_table.setHorizontalHeaderLabels(["ID Producto", "Nombre Producto", "Cantidad", "Tipo Movimiento"])
        self.movements_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.movements_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.movements_table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        layout.addWidget(self.movements_table)

        # Botones finales
        btn_layout = QHBoxLayout()
        self.save_btn = QPushButton("Guardar Cambios")
        self.save_btn.clicked.connect(self.confirm_and_save_movements)
        self.cancel_btn = QPushButton("Cancelar")
        self.cancel_btn.clicked.connect(self.reject)
        self.save_btn.setMinimumWidth(250)
        self.cancel_btn.setMinimumWidth(250)
        btn_layout.addWidget(self.save_btn)
        btn_layout.addWidget(self.cancel_btn)
        layout.addLayout(btn_layout)

        self.setLayout(layout)
        

    def load_product_options(self):
        """Cargar productos en el combo"""
        products = self.product_controller.get_products()
        self.product_combo.clear()

        for prod in products:
            id_prod = prod[0]      # id_prod
            nombre = prod[1]       # nombre_prod
            self.product_combo.addItem(nombre, id_prod)

        if products:
            self.product_combo.setCurrentIndex(0)
            self.update_stock_label()

    def register_movement(self):
        """Añadir movimiento a la lista interna"""
        id_prod = self.product_combo.currentData()
        nombre = self.product_combo.currentText()
        cantidad = self.qty_input.value()
        tipo = self.movement_type_combo.currentText()

        if tipo == "Salida":
            stock = self.inventory_controller.get_current_stock(id_prod)
            if cantidad > stock:
                QMessageBox.warning(self, "Stock insuficiente", f"Stock actual: {stock}")
                return

        self.inventory_controller.add_inventory_movement(id_prod, nombre, cantidad, tipo)
        self.update_movements_table()

    def update_movements_table(self):
        """Refrescar tabla con los movimientos actuales"""
        movimientos = self.inventory_controller.movements
        self.movements_table.setRowCount(len(movimientos))
        for row, item in enumerate(movimientos):
            self.movements_table.setItem(row, 0, QTableWidgetItem(str(item['id_prod'])))
            self.movements_table.setItem(row, 1, QTableWidgetItem(item['nombre_prod']))
            self.movements_table.setItem(row, 2, QTableWidgetItem(str(item['cantidad'])))
            self.movements_table.setItem(row, 3, QTableWidgetItem(item['tipo_movimiento']))
        self.movements_table.resizeColumnsToContents()
        header = self.movements_table.horizontalHeader()
        for col in range(self.movements_table.columnCount()):
            header.setSectionResizeMode(col, QHeaderView.ResizeMode.Stretch)
        # Centrar texto en encabezados y celdas
        for col in range(self.movements_table.columnCount()):
            item = self.movements_table.horizontalHeaderItem(col)
            if item:
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        for row in range(self.movements_table.rowCount()):
            for col in range(self.movements_table.columnCount()):
                cell = self.movements_table.item(row, col)
                if cell:
                    cell.setTextAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
        # Mostrar el número de filas correctamente en el encabezado vertical
        self.movements_table.setVerticalHeaderLabels([str(i+1) for i in range(len(movimientos))])

    def confirm_and_save_movements(self):
        """Guardar todos los movimientos en la base de datos"""
        if not self.inventory_controller.movements:
            QMessageBox.warning(self, "Sin movimientos", "No hay movimientos para guardar.")
            return
        
        self.inventory_controller.save_movements()
        QMessageBox.information(self, "Éxito", "Movimientos registrados.")
        self.inventory_controller.reset_movements()
        self.accept()
    
    def update_stock_label(self):
        """Actualizar la etiqueta de stock actual"""
        id_prod = self.product_combo.currentData()
        if id_prod:
            stock = self.inventory_controller.get_current_stock(id_prod)
            self.stock_label.setText(f"Stock actual: {stock}")
        else:
            self.stock_label.setText("Stock actual: -")
