from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLabel,
    QComboBox, QSpinBox, QPushButton, QTableWidget,
    QTableWidgetItem, QHBoxLayout, QMessageBox
)
from PyQt6.QtCore import Qt
from Model.factura_model import FacturaModel

class FacturaWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Facturas")
        self.setGeometry(200, 200, 800, 600)

        self.model = FacturaModel()
        self.init_ui()

    def init_ui(self):
        """Interfaz gráfica"""
        layout = QVBoxLayout()
        form_layout = QFormLayout()

        # ComboBox para seleccionar cliente
        self.combo_cliente = QComboBox()
        clientes = self.model.obtener_clientes()
        for cliente in clientes:
            self.combo_cliente.addItem(cliente[1], cliente[0])  # Muestra nombre, guarda id

        # ComboBox para seleccionar administrador
        self.combo_admin = QComboBox()
        admins = self.model.obtener_administradores()
        for admin in admins:
            self.combo_admin.addItem(admin[1], admin[0])  # Muestra nombre, guarda id

        # ComboBox para seleccionar producto
        self.combo_producto = QComboBox()
        productos = self.model.obtener_productos()
        for producto in productos:
            self.combo_producto.addItem(producto[1], producto[0])  # Muestra nombre, guarda id

        # SpinBox para cantidad de productos
        self.spin_cantidad = QSpinBox()
        self.spin_cantidad.setMinimum(1)
        self.spin_cantidad.setMaximum(1000)

        # Botón para agregar detalle a la tabla
        self.btn_agregar_detalle = QPushButton("Agregar Detalle")
        self.btn_agregar_detalle.clicked.connect(self.agregar_detalle)

        # Botón para guardar la factura
        self.btn_guardar_factura = QPushButton("Guardar Factura")
        self.btn_guardar_factura.clicked.connect(self.guardar_factura)

        # Tabla para mostrar los detalles de la factura
        self.tabla_detalle = QTableWidget()
        self.tabla_detalle.setColumnCount(4)
        self.tabla_detalle.setHorizontalHeaderLabels(["Producto", "Cantidad", "Precio Unitario", "Subtotal"])
        self.tabla_detalle.horizontalHeader().setStretchLastSection(True)

        # Agrega widgets al formulario
        form_layout.addRow(QLabel("Cliente:"), self.combo_cliente)
        form_layout.addRow(QLabel("Administrador:"), self.combo_admin)
        form_layout.addRow(QLabel("Producto:"), self.combo_producto)
        form_layout.addRow(QLabel("Cantidad:"), self.spin_cantidad)
        form_layout.addRow(self.btn_agregar_detalle)

        # Agrega layouts al contenedor principal
        layout.addLayout(form_layout)
        layout.addWidget(QLabel("Detalles de la Factura:"))
        layout.addWidget(self.tabla_detalle)
        layout.addWidget(self.btn_guardar_factura)

        self.setLayout(layout)

    def agregar_detalle(self):
        """Agrega un producto a la tabla de detalles"""
        # Obtiene la información del producto seleccionado
        id_producto = self.combo_producto.currentData()
        nombre_producto = self.combo_producto.currentText()
        cantidad = self.spin_cantidad.value()
        precio_unitario = self.model.obtener_precio_producto(id_producto)
        subtotal = cantidad * precio_unitario

        # Inserta nueva fila en la tabla
        row_position = self.tabla_detalle.rowCount()
        self.tabla_detalle.insertRow(row_position)

        # QTableWidgetItem para el nombre del producto
        item_producto = QTableWidgetItem(nombre_producto)
        item_producto.setData(Qt.ItemDataRole.UserRole, id_producto)

        # Agrega datos a la fila
        self.tabla_detalle.setItem(row_position, 0, item_producto)
        self.tabla_detalle.setItem(row_position, 1, QTableWidgetItem(str(cantidad)))
        self.tabla_detalle.setItem(row_position, 2, QTableWidgetItem(f"{precio_unitario:.2f}"))
        self.tabla_detalle.setItem(row_position, 3, QTableWidgetItem(f"{subtotal:.2f}"))

    def guardar_factura(self):
        """Guarda la factura en la db"""
        # Obtiene cliente y administrador seleccionados
        id_cliente = self.combo_cliente.currentData()
        id_admin = self.combo_admin.currentData()

        # Valida que haya al menos un detalle agregado
        if self.tabla_detalle.rowCount() == 0:
            QMessageBox.warning(self, "Error", "Agregue al menos un producto a la factura.")
            return

        # Calcula el total de la factura
        total = 0
        detalles = []

        for row in range(self.tabla_detalle.rowCount()):
            # Recuperar id_producto asociado desde el dato oculto
            item_producto = self.tabla_detalle.item(row, 0)
            id_producto = item_producto.data(Qt.ItemDataRole.UserRole)

            cantidad = int(self.tabla_detalle.item(row, 1).text())
            precio_unitario = float(self.tabla_detalle.item(row, 2).text())
            subtotal = float(self.tabla_detalle.item(row, 3).text())

            total += subtotal
            detalles.append((id_producto, cantidad, precio_unitario))

        # Guarda la factura en la base de datos
        success = self.model.guardar_factura(id_cliente, id_admin, total, detalles)

        if success:
            QMessageBox.information(self, "Éxito", "Factura guardada correctamente.")
            self.tabla_detalle.setRowCount(0)  # Limpiar tabla
        else:
            QMessageBox.critical(self, "Error", "No se pudo guardar la factura.")