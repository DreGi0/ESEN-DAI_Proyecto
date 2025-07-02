import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Super Duper App")
        self.setGeometry(100, 100, 1000, 700)
    
    # =====================================
    # GESTION DE PRODUCTOS
    # =====================================
    
    def create_product(self):
        pass
    
    def get_products(self):
        pass
    
    def get_product_by_id(self, product_id):
        pass
    
    def update_product(self, product_id):
        pass
    
    def delete_product(self, product_id):
        pass
    
    def associate_product_category(self, product_id, category_id):
        pass
    
    def associate_product_unit_measure(self, product_id, unit_id):
        pass
    
    def associate_product_location(self, product_id, location_id):
        pass
    
    def assign_supplier_to_product(self, product_id, supplier_id):
        pass
    
    def remove_supplier_from_product(self, product_id, supplier_id):
        pass
    
    def get_product_suppliers(self, product_id):
        pass
    
    def view_product_details(self, product_id):
        pass

    # =====================================
    # GESTION DE INVENTARIO
    # =====================================

    # =====================================
    # GESTION DE FACTURACION
    # =====================================

    # =====================================
    # BUSQUEDA Y CONSULTA
    # =====================================

def main():
    """Función principal"""
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    app.exec()

if __name__ == "__main__":
    main()