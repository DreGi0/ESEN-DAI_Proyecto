from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox,
    QTableWidget, QTableWidgetItem, QSpinBox, QLineEdit, QMessageBox,
    QHeaderView
)
from PyQt6.QtCore import Qt
from Controller.billing_controller import BillingController
from Controller.client_controller import ClientController
from Controller.product_controller import ProductController
from Controller.provider_controller import ProviderController
from View.Invoice_view import InvoiceViewerDialog

class BillingDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.billing_controller = BillingController()
        self.client_controller = ClientController()
        self.product_controller = ProductController()
        self.provider_controller = ProviderController()
        self.setWindowTitle("Gestión de Facturación")
        self.resize(950, 650)  # Más ancho y alto
        self.setup_ui()
        self.load_initial_data()

    def setup_ui(self):
        """Configura la interfaz gráfica"""
        layout = QVBoxLayout()

        # Descripción
        title = QLabel("Gestión de Facturación")
        title.setProperty("cssClass", "title")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        desc_label = QLabel("Registra compras y ventas. Selecciona el tipo de factura, "
                            "la entidad (cliente o proveedor), agrega productos y guarda la factura.")
        desc_label.setProperty("cssClass", "subtitle")
        desc_label.setWordWrap(True)
        layout.addWidget(desc_label)

        # Tipo de factura (Compra o Venta) y entidad (Cliente o Proveedor)
        tipo_layout = QHBoxLayout()
        tipo_layout.addWidget(QLabel("Tipo Factura:"))
        self.tipo_combo = QComboBox()
        self.tipo_combo.addItems(["Compra", "Venta"])
        tipo_layout.addWidget(self.tipo_combo)

        self.entity_label = QLabel("Cliente:")
        tipo_layout.addWidget(self.entity_label)
        self.entity_combo = QComboBox()
        tipo_layout.addWidget(self.entity_combo)

        layout.addLayout(tipo_layout)

        # Método de pago
        pago_layout = QHBoxLayout()
        pago_layout.addWidget(QLabel("Método de Pago:"))
        self.metodo_pago_input = QLineEdit()
        self.metodo_pago_input.setPlaceholderText("Ej: Efectivo, Tarjeta, Transferencia")
        pago_layout.addWidget(self.metodo_pago_input)
        layout.addLayout(pago_layout)

        # Selección de productos
        prod_layout = QHBoxLayout()
        self.prov_combo = QComboBox()
        self.prod_combo = QComboBox()
        self.qty_spin = QSpinBox()
        self.qty_spin.setMinimum(1)
        self.qty_spin.setMaximum(1000)
        self.add_product_btn = QPushButton("Agregar Producto")
        self.add_product_btn.setMinimumWidth(150)
        prod_layout.addWidget(QLabel("Proveedor:"))
        prod_layout.addWidget(self.prov_combo)
        prod_layout.addWidget(QLabel("Producto:"))
        prod_layout.addWidget(self.prod_combo)
        prod_layout.addWidget(QLabel("Cantidad:"))
        prod_layout.addWidget(self.qty_spin)
        prod_layout.addWidget(self.add_product_btn)
        layout.addLayout(prod_layout)

        # Tabla para mostrar los productos añadidos a la factura
        self.products_table = QTableWidget(0, 4)
        self.products_table.setMinimumWidth(900)
        self.products_table.setMinimumHeight(300)
        self.products_table.setHorizontalHeaderLabels(["ID ProductoProveedor", "Producto", "Cantidad", "Precio Unitario"])
        self.products_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.products_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.products_table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        layout.addWidget(self.products_table)

        # Mostrar total de la factura
        total_layout = QHBoxLayout()
        total_layout.addWidget(QLabel("Total:"))
        self.total_label = QLabel("$0.00")
        total_layout.addWidget(self.total_label)
        layout.addLayout(total_layout)

        # Botones
        btn_layout = QHBoxLayout()
        self.save_btn = QPushButton("Guardar Factura")
        self.cancel_btn = QPushButton("Cancelar")
        self.view_btn = QPushButton("Consultar Facturas")
        self.save_btn.setMinimumWidth(200)
        self.cancel_btn.setMinimumWidth(200)
        self.view_btn.setMinimumWidth(200)
        btn_layout.addWidget(self.save_btn)
        btn_layout.addWidget(self.cancel_btn)
        btn_layout.addWidget(self.view_btn)
        layout.addLayout(btn_layout)

        # Botón regresar/cancelar (estilo consistente y más pequeño)
        self.btn_regresar = QPushButton("Regresar al Menú Principal")
        self.btn_regresar.setObjectName("btnRegresar")
        self.btn_regresar.clicked.connect(self.reject)
        layout.addWidget(self.btn_regresar)

        self.setLayout(layout)

        self.tipo_combo.currentTextChanged.connect(self.on_tipo_changed)
        self.prov_combo.currentIndexChanged.connect(self.on_provider_changed)
        self.add_product_btn.clicked.connect(self.add_product)
        self.save_btn.clicked.connect(self.save_invoice)
        self.cancel_btn.clicked.connect(self.reject)
        self.view_btn.clicked.connect(self.view_invoices)

    def load_initial_data(self):
        """Cargar clientes y proveedores desde la base"""
        self.clients = self.client_controller.get_clients()
        self.providers = self.provider_controller.get_providers()
        self.on_tipo_changed(self.tipo_combo.currentText())

    def on_tipo_changed(self, tipo):
        """
        Cambia entre clientes o proveedores dependiendo del tipo de factura.
        Si es venta, carga clientes. Si es compra, carga proveedores.
        """
        self.entity_combo.clear()
        if tipo == "Venta":
            self.entity_label.setText("Cliente:")
            for c in self.clients:
                self.entity_combo.addItem(f"{c[1]} {c[2]}", c[0])
            self.prov_combo.setEnabled(False)
        else:
            self.entity_label.setText("Proveedor:")
            for p in self.providers:
                self.entity_combo.addItem(f"{p[1]} {p[2]}", p[0])
            self.prov_combo.setEnabled(True)
            self.prov_combo.clear()
            for p in self.providers:
                self.prov_combo.addItem(f"{p[1]} {p[2]}", p[0])
            self.on_provider_changed()

    def on_provider_changed(self):
        """Actualizar la lista de productos cuando cambia el proveedor"""
        id_prov = self.prov_combo.currentData()
        self.prod_combo.clear()
        if id_prov:
            products = self.product_controller.get_products_by_provider(id_prov)
            for prod in products:
                self.prod_combo.addItem(f"{prod[1]} - ${prod[2]:.2f}", (prod[0], prod[2]))

    def add_product(self):
        """Agregar un producto seleccionado con su cantidad a la factura"""
        id_pp, precio_unitario_detalle = self.prod_combo.currentData()
        nombre_prod = self.prod_combo.currentText()
        cantidad_detalle = self.qty_spin.value()
        self.billing_controller.add_product_to_invoice(id_pp, nombre_prod, cantidad_detalle, precio_unitario_detalle)
        self.refresh_products_table()
        self.update_total()

    def refresh_products_table(self):
        """Actualizar la tabla que muestra los productos añadidos a la factura"""
        items = self.billing_controller.invoice_products
        self.products_table.setRowCount(len(items))
        for row, item in enumerate(items):
            self.products_table.setItem(row, 0, QTableWidgetItem(str(item['id_producto_proveedor'])))
            self.products_table.setItem(row, 1, QTableWidgetItem(item['nombre_prod']))
            self.products_table.setItem(row, 2, QTableWidgetItem(str(item['cantidad_detalle'])))
            self.products_table.setItem(row, 3, QTableWidgetItem(f"${item['precio_unitario_detalle']:.2f}"))
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
        self.products_table.setVerticalHeaderLabels([str(i+1) for i in range(len(items))])

    def update_total(self):
        """Calcular y mostrar el total de la factura"""
        total = self.billing_controller.calculate_total()
        self.total_label.setText(f"${total:.2f}")

    def save_invoice(self):
        """Guardar la factura y sus detalles en la base"""
        tipo = self.tipo_combo.currentText().lower()
        id_cliente = self.entity_combo.currentData() if tipo == "venta" else None
        id_prov = self.entity_combo.currentData() if tipo == "compra" else None
        metodo_pago = self.metodo_pago_input.text().strip()
        if not metodo_pago:
            QMessageBox.warning(self, "Error", "Ingrese método de pago.")
            return
    def view_invoices(self):
        viewer = InvoiceViewerDialog(self)
        viewer.exec()
        self.total_label.setText(f"${total:.2f}")

    def save_invoice(self):
        """Guardar la factura y sus detalles en la base"""
        tipo = self.tipo_combo.currentText().lower()
        id_cliente = self.entity_combo.currentData() if tipo == "venta" else None
        id_prov = self.entity_combo.currentData() if tipo == "compra" else None
        metodo_pago = self.metodo_pago_input.text().strip()
        if not metodo_pago:
            QMessageBox.warning(self, "Error", "Ingrese método de pago.")
            return
    def view_invoices(self):
        viewer = InvoiceViewerDialog(self)
        viewer.exec()
