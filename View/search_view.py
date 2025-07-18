from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QFormLayout, QPushButton, QWidget, QComboBox,
    QTableWidget, QTableWidgetItem, QMainWindow, QLineEdit, QMessageBox
)
from Controller.search_controller import SearchController
class SearchDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.controller = SearchController()
        self.setWindowTitle("Búsqueda de productos -- Ferretería Mónaco")
        self.resize(700, 500)
        self.setup_ui_search()
    
    def setup_ui_search(self):
        main_widget = QWidget()
        filter_widget = QWidget()
        main_layout = QHBoxLayout()
        self.table_result = QTableWidget()

        filters_layout = QFormLayout()
        self.product_name = QLineEdit()
        self.product_category = QComboBox()
        self.product_location = QLineEdit()
        self.search_btn = QPushButton("Buscar")

        filters_layout.addRow("Nombre: ", self.product_name)
        filters_layout.addRow("Categoría: ", self.product_category)
        filters_layout.addRow("Ubicación: ", self.product_location)
        filters_layout.addRow("", self.search_btn)
        filter_widget.setLayout(filters_layout)

        self.table_result.setColumnCount(4)
        self.table_result.setHorizontalHeaderLabels(["ID", "Nombre", "Categoría", "Ubicación"])
        self.table_result.setRowCount(0) 
        self.search_btn.clicked.connect(self.search_product)

        self.product_category.addItem("Todas", None)
        for id, name in self.controller.get_categories():
            self.product_category.addItem(name, id)

        main_layout.addWidget(self.table_result)
        main_layout.addWidget(filter_widget)

        self.setLayout(main_layout)

    def search_product(self):
        name_filter = self.product_name.text().strip()
        category_filter = self.product_category.currentData()
        location_filter = self.product_location.text().strip()

        if not name_filter:
            name_filter = None
        if not category_filter:
            category_filter = None
        if not location_filter:
            location_filter = None

        results = self.controller.search_products(name=name_filter, category=category_filter, location=location_filter)
        if results is None:
            QMessageBox.critical(self, "Error", "No se pudo ejecutar la búsqueda.")
            return
        if not results:
            QMessageBox.information(self, "Sin resultados", "No se encontraron productos que coincidan con los filtros.")
            self.table_result.setRowCount(0)
            return

        self.table_result.setRowCount(len(results))  

        for row, product in enumerate(results):
            self.table_result.setItem(row, 0, QTableWidgetItem(str(product[0])))
            self.table_result.setItem(row, 1, QTableWidgetItem(product[1]))
            self.table_result.setItem(row, 2, QTableWidgetItem(product[2]))
            self.table_result.setItem(row, 3, QTableWidgetItem(product[3]))