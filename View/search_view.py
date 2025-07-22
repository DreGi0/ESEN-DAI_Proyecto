from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QFormLayout, QPushButton, QWidget, QComboBox,
    QTableWidget, QTableWidgetItem, QLabel, QLineEdit, QMessageBox, QHeaderView
)
from Controller.search_controller import SearchController
from PyQt6.QtCore import Qt

class SearchDialog(QDialog):
    """
    Diálogo para buscar productos por nombre, categoría y ubicación.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.controller = SearchController()
        self.setWindowTitle("Búsqueda de productos -- Ferretería Mónaco")
        self.resize(900, 500)
        self.setup_ui_search()

    def setup_ui_search(self):
        """
        Configura la interfaz de búsqueda con filtros a la izquierda y resultados a la derecha.
        """
        main_layout = QHBoxLayout(self)

        # --- Filtros de búsqueda (lado izquierdo) ---
        filter_panel = QWidget()
        filter_layout = QVBoxLayout()
        filter_panel.setLayout(filter_layout)

        # Título y subtítulo
        title = QLabel("Buscar productos")
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        subtitle = QLabel("Filtra por nombre, categoría o ubicación. Deja un campo vacío para ignorar ese filtro.")
        subtitle.setWordWrap(True)
        filter_layout.addWidget(title)
        filter_layout.addWidget(subtitle)

        # Formulario de filtros
        filters_form = QFormLayout()
        self.product_name = QLineEdit()
        self.product_name.setPlaceholderText("Ej: Tornillo")
        self.product_category = QComboBox()
        self.product_location = QLineEdit()
        self.product_location.setPlaceholderText("Ej: Pasillo 2")
        self.search_btn = QPushButton("Buscar")

        filters_form.addRow("Nombre:", self.product_name)
        filters_form.addRow("Categoría:", self.product_category)
        filters_form.addRow("Ubicación:", self.product_location)
        filter_layout.addLayout(filters_form)
        filter_layout.addWidget(self.search_btn)
        filter_layout.addStretch()

        # Llenar categorías
        self.product_category.addItem("Todas", None)
        for id, name in self.controller.get_categories():
            self.product_category.addItem(name, id)

        # --- Tabla de resultados (lado derecho) ---
        self.table_result = QTableWidget()
        self.table_result.setMinimumWidth(700)
        self.table_result.setMinimumHeight(250)
        self.table_result.setColumnCount(4)
        self.table_result.setHorizontalHeaderLabels(["ID", "Nombre", "Categoría", "Ubicación"])
        self.table_result.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table_result.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table_result.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.table_result.setRowCount(0)

        # Layout principal: filtros a la izquierda, tabla a la derecha
        main_layout.addWidget(filter_panel, 1)
        main_layout.addWidget(self.table_result, 3)

        # Conectar botón de búsqueda
        self.search_btn.clicked.connect(self.search_product)

    def search_product(self):
        """
        Realiza la búsqueda de productos según los filtros y muestra los resultados en la tabla.
        """
        name_filter = self.product_name.text().strip() or None
        category_filter = self.product_category.currentData()
        location_filter = self.product_location.text().strip() or None

        # Si la categoría es "Todas", ignora el filtro
        if not category_filter:
            category_filter = None

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
        header = self.table_result.horizontalHeader()
        for col in range(self.table_result.columnCount()):
            header.setSectionResizeMode(col, QHeaderView.ResizeMode.Stretch)
        # Centrar texto en encabezados y celdas
        for col in range(self.table_result.columnCount()):
            item = self.table_result.horizontalHeaderItem(col)
            if item:
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        for row in range(self.table_result.rowCount()):
            for col in range(self.table_result.columnCount()):
                cell = self.table_result.item(row, col)
                if cell:
                    cell.setTextAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
        # Mostrar el número de filas correctamente en el encabezado vertical
        self.table_result.setVerticalHeaderLabels([str(i+1) for i in range(len(results))])