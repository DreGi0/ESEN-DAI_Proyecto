from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QMessageBox, QHBoxLayout, QLabel, QTableWidget, QTableWidgetItem
)
from Controller.billing_controller import BillingController


class InvoiceViewerDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.billing_controller = BillingController()
        self.setWindowTitle("Facturas Registradas")
        self.resize(800, 600)
        self.setup_ui()
        self.load_invoices()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Tabla de facturas
        self.invoice_table = QTableWidget(0, 5)
        self.invoice_table.setHorizontalHeaderLabels(["ID", "Tipo", "Fecha", "Método de Pago", "Total"])
        layout.addWidget(QLabel("Facturas:"))
        layout.addWidget(self.invoice_table)

        # Tabla de detalles de la factura seleccionada
        self.details_table = QTableWidget(0, 4)
        self.details_table.setHorizontalHeaderLabels(["ID Detalle", "ProductoProveedor ID", "Cantidad", "Precio Unitario"])
        layout.addWidget(QLabel("Detalles de Factura Seleccionada:"))
        layout.addWidget(self.details_table)

        self.setLayout(layout)

        # Conexión al hacer clic en una factura
        self.invoice_table.cellClicked.connect(self.load_invoice_details)

    def load_invoices(self):
        invoices = self.billing_controller.get_all_invoices()
        self.invoice_table.setRowCount(len(invoices))
        
        for row, inv in enumerate(invoices):
            self.invoice_table.setItem(row, 0, QTableWidgetItem(str(inv[0])))  # id_factura
            self.invoice_table.setItem(row, 1, QTableWidgetItem(inv[1]))        # tipo_factura
            self.invoice_table.setItem(row, 2, QTableWidgetItem(str(inv[2])))  # fecha
            self.invoice_table.setItem(row, 3, QTableWidgetItem(inv[6]))        # metodo_pago

            try:
                total = float(inv[7])
                total_str = f"${total:.2f}"
            except (ValueError, TypeError):
                total_str = "Error"

            self.invoice_table.setItem(row, 4, QTableWidgetItem(total_str))
                        
    def load_invoice_details(self, row, column):
        invoice_id = int(self.invoice_table.item(row, 0).text())
        details = self.billing_controller.get_invoice_details(invoice_id)
        self.details_table.setRowCount(len(details))
        for r, d in enumerate(details):
            self.details_table.setItem(r, 0, QTableWidgetItem(str(d[0])))  # id_detalle
            self.details_table.setItem(r, 1, QTableWidgetItem(str(d[2])))  # id_producto_proveedor
            self.details_table.setItem(r, 2, QTableWidgetItem(str(d[3])))  # cantidad
            self.details_table.setItem(r, 3, QTableWidgetItem(f"${d[4]:.2f}"))  # precio
        