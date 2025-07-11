from Model import billing_model
from datetime import datetime

class BillingController:
    def __init__(self):
        self.invoice_products = []

    def get_clients(self):
        return billing_model.get_all_clients()

    def get_providers(self):
        return billing_model.get_all_providers()

    def get_products_for_provider(self, id_prov):
        return billing_model.get_products_by_provider(id_prov)

    def add_product_to_invoice(self, id_producto_proveedor, nombre_prod, cantidad_detalle, precio_unitario_detalle):
        self.invoice_products.append({
            'id_producto_proveedor': id_producto_proveedor,
            'nombre_prod': nombre_prod,
            'cantidad_detalle': cantidad_detalle,
            'precio_unitario_detalle': precio_unitario_detalle
        })

    def calculate_total(self):
        return sum(item['cantidad_detalle'] * item['precio_unitario_detalle'] for item in self.invoice_products)

    def save_invoice(self, tipo_factura, id_cliente, id_prov, metodo_pago, id_administrador=1):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        total = self.calculate_total()
        factura_id = billing_model.create_invoice(
            tipo_factura, fecha, id_cliente, id_prov, id_administrador, metodo_pago, total
        )
        if factura_id is None:
            return False

        for item in self.invoice_products:
            billing_model.add_invoice_detail(
                factura_id,
                item['id_producto_proveedor'],
                item['cantidad_detalle'],
                item['precio_unitario_detalle']
            )
        billing_model.update_invoice_total(factura_id, total)
        return True

    def reset_invoice(self):
        self.invoice_products = []