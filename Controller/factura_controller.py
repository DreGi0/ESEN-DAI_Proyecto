from Model.factura_model import FacturaModel
from PyQt6.QtWidgets import QMessageBox

class FacturaController:
    def __init__(self, view, user_id):
        # Vista FacturaWindow y id de usuario
        self.view = view
        self.user_id = user_id
        self.model = FacturaModel()

        self.cargar_products()

    def cargar_products(self):
        """Obtiene los productos de la db"""
        productos = self.model.get_productos()
        self.view.set_productos(productos) # Pasa productos al combo box

    def agregar_producto(self, producto_id, cantidad):
        """Busca el producto seleccionado para agregarlo a la tabla detalle"""
        producto = self.model.get_producto_por_id(producto_id)
        if producto:
            self.view.agregar_detalle(producto, cantidad) # Agrega el producto y la cantidad
        else:
            QMessageBox.warning(self.view, "Error", "Producto no encontrado")

    def guardar_factura(self, cliente_nombre, detalles):
        if not cliente_nombre:
            QMessageBox.warning(self.view, "Error", "Debe ingresar el nombre del cliente")
            return
        if not detalles:
            QMessageBox.warning(self.view, "Error", "Debe agregar productos a la factura")
            return

        try:
            self.model.guardar_factura(cliente_nombre, self.user_id, detalles)
            QMessageBox.information(self.view, "Éxito", "Factura guardada correctamente")
            self.view.limpiar_form()
        except Exception as e:
            QMessageBox.critical(self.view, "Error", f"No se pudo guardar la factura: {e}")
