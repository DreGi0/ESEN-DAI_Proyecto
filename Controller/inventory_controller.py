from Model import inventory_model
from Model import product_model
from datetime import datetime


class InventoryController:
    """
    Controlador para manejar todas las operaciones de inventario.
    """
    
    def __init__(self):
        """Inicializa el controlador con una lista vacía de movimientos."""
        self.movements = []
    
    # ==========================================================================
    # CONSULTAS DE INVENTARIO
    # ==========================================================================
    
    def get_iventory(self):
        """
        Obtiene todo el inventario disponible.
        
        Returns:
            list: Lista completa del inventario
        """
        return inventory_model.get_inventory_history()
    
    def get_all_products(self):
        """
        Obtiene todos los productos registrados.
        
        Returns:
            list: Lista de todos los productos
        """
        return product_model.get_products() ###asdjalksajldjdkasjlsdjljds
    
    def get_current_stock(self, id_prod):
        """
        Obtiene el stock actual de un producto específico.
        
        Args:
            id_prod (int): ID del producto
            
        Returns:
            int: Cantidad actual en stock, 0 si no existe
        """
        result = inventory_model.get_product_current_stock(id_prod)
        if result is not None:
            return int(result)
        return 0
    
    # ==========================================================================
    # GESTIÓN DE MOVIMIENTOS
    # ==========================================================================
    
    def add_inventory_movement(self, id_prod, nombre_prod, cantidad, tipo_movimiento):
        """
        Añade un movimiento de inventario a la lista temporal.
        
        Args:
            id_prod (int): ID del producto
            nombre_prod (str): Nombre del producto
            cantidad (int): Cantidad del movimiento
            tipo_movimiento (str): Tipo de movimiento ('entrada' o 'salida')
        """
        self.movements.append({
            'id_prod': id_prod,
            'nombre_prod': nombre_prod,
            'cantidad': cantidad,
            'tipo_movimiento': tipo_movimiento
        })
    
    def save_movements(self):
        """
        Guarda todos los movimientos temporales en la base de datos.
        
        Returns:
            bool: True si todos los movimientos fueron guardados exitosamente
        """
        fecha = datetime.now().strftime("%Y-%m-%d")
        for item in self.movements:
            inventory_model.insert_inventory_movement(
                item['id_prod'],
                item['cantidad'],
                fecha,
                item['tipo_movimiento']
            )
        return True
    
    def reset_movements(self):
        """Limpia la lista temporal de movimientos."""
        self.movements = []
