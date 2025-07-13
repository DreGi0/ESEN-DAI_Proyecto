from Model import inventory_model
from datetime import datetime

class InventoryController:
    def __init__(self):
        self.movements = []

    def get_all_inventory(self):
        return inventory_model.get_all_inventory()

    def get_all_products(self):
        return inventory_model.get_all_products()

    def add_inventory_movement(self, id_prod, nombre_prod, cantidad, tipo_movimiento):
        self.movements.append({
            'id_prod': id_prod,
            'nombre_prod': nombre_prod,
            'cantidad': cantidad,
            'tipo_movimiento': tipo_movimiento
        })

    def get_current_stock(self, id_prod):
        result = inventory_model.get_stock_by_product(id_prod)
        if result and result[0][0] is not None:
            return result[0][0]
        return 0

    def save_movements(self):
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
        self.movements = []