from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox,
    QTableWidget, QTableWidgetItem, QSpinBox, QLineEdit, QMessageBox
)
from Controller.billing_controller import BillingController
from Controller.client_controller import ClientController
from Controller.product_controller import ProductController
from Controller.provider_controller import ProviderController

class BillingDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.billing_controller = BillingController()
        self.client_controller = ClientController()
        self.product_controller = ProductController()
        self.provider_controller = ProviderController()
        self.setWindowTitle("Gestión de Facturación")
        self.resize(700, 500)
        self.setup_ui()
        self.load_initial_data()

    def setup_ui(self):
        """Configura la interfaz gráfica"""
        layout = QVBoxLayout()

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
        self.products_table.setHorizontalHeaderLabels(["ID", "Producto", "Cantidad", "Precio Unitario"])
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
        btn_layout.addWidget(self.save_btn)
        btn_layout.addWidget(self.cancel_btn)
        layout.addLayout(btn_layout)

        self.setLayout(layout)

        self.tipo_combo.currentTextChanged.connect(self.on_tipo_changed)
        self.prov_combo.currentIndexChanged.connect(self.on_provider_changed)
        self.add_product_btn.clicked.connect(self.add_product)
        self.save_btn.clicked.connect(self.save_invoice)
        self.cancel_btn.clicked.connect(self.reject)

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
        success = self.billing_controller.save_invoice(tipo, id_cliente, id_prov, metodo_pago)
        if success:
            QMessageBox.information(self, "Éxito", "Factura guardada correctamente.")
            self.billing_controller.reset_invoice()
            self.accept()
        else:
            QMessageBox.critical(self, "Error", "Error al guardar la factura.")