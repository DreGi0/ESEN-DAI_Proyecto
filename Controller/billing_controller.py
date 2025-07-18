from Model import billing_model
from datetime import datetime


class BillingController:
    """
    Controlador para manejar todas las operaciones de facturación.
    Gestiona la creación de facturas, productos, y procesamientos de pago.
    """
    
    def __init__(self):
        """Inicializa el controlador con una lista vacía de productos de factura."""
        self.invoice_products = []
    
    # ==========================================================================
    # GESTIÓN DE PRODUCTOS EN FACTURA
    # ==========================================================================
    
    def add_product_to_invoice(self, product_provider_id, product_name, quantity, unit_price):
        """
        Añade un producto a la factura actual en proceso.
        
        Args:
            product_provider_id (int): ID de la relación producto-proveedor
            product_name (str): Nombre del producto
            quantity (int): Cantidad del producto
            unit_price (float): Precio unitario del producto
        """
        self.invoice_products.append({
            'id_producto_proveedor': product_provider_id,
            'nombre_prod': product_name,
            'cantidad_detalle': quantity,
            'precio_unitario_detalle': unit_price
        })
    
    def calculate_total(self):
        """
        Calcula el monto total de la factura actual.
        
        Returns:
            float: Monto total de todos los productos en la factura
        """
        return sum(item['cantidad_detalle'] * item['precio_unitario_detalle'] 
                  for item in self.invoice_products)
    
    def reset_invoice(self):
        """Limpia todos los productos de la factura actual."""
        self.invoice_products = []
    
    # ==========================================================================
    # OPERACIONES DE FACTURACIÓN
    # ==========================================================================
    
    def save_invoice(self, invoice_type, client_id, provider_id, payment_method, admin_id=1):
        """
        Guarda la factura actual en la base de datos con todos sus detalles.
        
        Args:
            invoice_type (str): Tipo de factura ('compra', 'venta', etc.)
            client_id (int): ID del cliente
            provider_id (int): ID del proveedor
            payment_method (str): Método de pago utilizado
            admin_id (int, optional): ID del administrador. Por defecto es 1.
            
        Returns:
            bool: True si la factura fue guardada exitosamente, False en caso contrario
        """
        # Generar fecha y hora actual
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        total_amount = self.calculate_total()
        
        # Crear el registro principal de la factura
        invoice_id = billing_model.create_invoice(
            invoice_type, current_date, client_id, provider_id, admin_id, payment_method, total_amount
        )
        
        if invoice_id is None:
            return False
        
        # Añadir todos los detalles de la factura (productos)
        for item in self.invoice_products:
            billing_model.add_invoice_detail(
                invoice_id,
                item['id_producto_proveedor'],
                item['cantidad_detalle'],
                item['precio_unitario_detalle']
            )
        
        # Actualizar el monto total en la factura
        billing_model.update_invoice_total(invoice_id, total_amount)
        return True
