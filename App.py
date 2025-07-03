import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLabel, QLineEdit, QPushButton
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QCursor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
        self.contenedor = QWidget()
        self.layout_contenedor = QVBoxLayout()
        self.cont_sesion = QWidget()
        self.lay_sesion = QFormLayout()
        self.cont_sesion.setLayout(self.lay_sesion)
        
        # imagen del logo
        self.logo = QLabel()
        self.logo_img = QPixmap(r"img\logo.png")
        self.logo.setFixedSize(420, 200)
        self.logo.setScaledContents(True)
        self.logo.setPixmap(self.logo_img)
        self.lay_img = QHBoxLayout()
        self.lay_img.addStretch()
        self.lay_img.addWidget(self.logo)
        self.lay_img.addStretch()
        
        # datos
        self.bienvenida = QLabel("Inicio de sesión")
        self.txt_usuario = QLabel("      Usuario")
        self.box_usuario = QLineEdit()
        self.txt_pass = QLabel("Contraseña")
        self.box_pass = QLineEdit()
        self.feedback = QLabel("Esta es una prueba de feedback")
        self.feedback.setObjectName("feedback")
        self.btn_ingresar = QPushButton("Ingresar")
        
        self.bienvenida.setStyleSheet("font-size: 25px")
        self.box_usuario.setFixedWidth(150)
        self.box_pass.setFixedWidth(150)
        self.btn_ingresar.setFixedSize(150, 40)
        self.btn_ingresar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.box_pass.setEchoMode(QLineEdit.EchoMode.Password)
        self.espaciado = QLabel()
        self.espaciado.setFixedHeight(30)
        
        # Centra el título
        self.lay_titulo = QHBoxLayout()
        self.lay_titulo.addStretch()
        self.lay_titulo.addWidget(self.bienvenida)
        self.lay_titulo.addStretch()
        
        # Centra label y caja de usuario
        self.lay_usuario = QHBoxLayout()
        self.lay_usuario.addStretch()
        self.lay_usuario.addWidget(self.txt_usuario)
        self.lay_usuario.addWidget(self.box_usuario)
        self.lay_usuario.addStretch()
        
        # Centra label y caja de contraseña
        self.lay_pass = QHBoxLayout()
        self.lay_pass.addStretch()
        self.lay_pass.addWidget(self.txt_pass)
        self.lay_pass.addWidget(self.box_pass)
        self.lay_pass.addStretch()
        
        # Centra label de feedback
        self.lay_feedback = QHBoxLayout()
        self.lay_feedback.addStretch()
        self.lay_feedback.addWidget(self.feedback)
        self.lay_feedback.addStretch()
        # Centra botón
        self.lay_btn_ingresar = QHBoxLayout()
        self.lay_btn_ingresar.addStretch()
        self.lay_btn_ingresar.addWidget(self.btn_ingresar)
        self.lay_btn_ingresar.addStretch()
        
            # Agrega al contendor del Log in
        self.lay_sesion.addRow(self.lay_img)
        self.lay_sesion.addRow(self.lay_titulo)
        self.lay_sesion.addRow(self.espaciado)
        self.lay_sesion.addRow(self.lay_usuario)
        self.lay_sesion.addRow(self.lay_pass)
        self.lay_sesion.addRow(self.lay_feedback)
        self.lay_sesion.addRow(QLabel())
        self.lay_sesion.addRow(self.lay_btn_ingresar)
        
            # Agrega elementos al contenedor general
        self.layout_contenedor.addWidget(self.cont_sesion)
        self.contenedor.setLayout(self.layout_contenedor)
        self.setCentralWidget(self.contenedor)
    
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
    with open(r"style.qss") as archivo_estilo:
        style = archivo_estilo.read()
        app.setStyleSheet(style)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()