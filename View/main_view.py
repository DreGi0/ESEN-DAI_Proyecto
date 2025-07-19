import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                             QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QMenuBar, QStatusBar)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Sistema de Gestión - Ferretería Mónaco")
        self.setGeometry(480, 270, 960, 540)
        
        # Widget central
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # Layout principal
        self.main_layout = QVBoxLayout(self.central_widget)
        
        self.create_menu_bar()
        self.create_main_content()
        self.create_status_bar()
    
    # EXAMPLES
    def create_menu_bar(self):
        """Crear la barra de menús"""
        menubar = self.menuBar()
        
        # Menú Archivo
        file_menu = menubar.addMenu('Archivo')
        
        new_action = QAction('Nuevo', self)
        new_action.setShortcut('Ctrl+N')
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)
        
        open_action = QAction('Abrir', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction('Salir', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Menú Ayuda
        help_menu = menubar.addMenu('Ayuda')
        
        about_action = QAction('Acerca de', self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
    
    def create_main_content(self):
        """Crear el contenido principal de la ventana"""
        # Label de bienvenida
        welcome_label = QLabel('¡Bienvenido a tu aplicación PyQt6!')
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome_label.setStyleSheet("font-size: 18px; font-weight: bold; margin: 20px;")
        
        # Layout horizontal para botones
        button_layout = QHBoxLayout()
        
        # Botones de ejemplo
        btn1 = QPushButton('Botón 1')
        btn1.clicked.connect(self.button1_clicked)
        
        btn2 = QPushButton('Botón 2')
        btn2.clicked.connect(self.button2_clicked)
        
        btn3 = QPushButton('Botón 3')
        btn3.clicked.connect(self.button3_clicked)
        
        button_layout.addWidget(btn1)
        button_layout.addWidget(btn2)
        button_layout.addWidget(btn3)
        
        # Agregar widgets al layout principal
        self.main_layout.addWidget(welcome_label)
        self.main_layout.addLayout(button_layout)
        
        # Espaciador para centrar contenido
        self.main_layout.addStretch()
    
    def create_status_bar(self):
        """Crear la barra de estado"""
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage('Listo')
    
    # Métodos de eventos
    def new_file(self):
        """Crear nuevo archivo"""
        self.status_bar.showMessage('Nuevo archivo creado')
        print("Nuevo archivo")
    
    def open_file(self):
        """Abrir archivo"""
        self.status_bar.showMessage('Abriendo archivo...')
        print("Abrir archivo")
    
    def show_about(self):
        """Mostrar información sobre la aplicación"""
        self.status_bar.showMessage('Mostrando información')
        print("Acerca de la aplicación")
    
    def button1_clicked(self):
        """Evento del botón 1"""
        self.status_bar.showMessage('Botón 1 presionado')
        print("Botón 1 clickeado")
    
    def button2_clicked(self):
        """Evento del botón 2"""
        self.status_bar.showMessage('Botón 2 presionado')
        print("Botón 2 clickeado")
    
    def button3_clicked(self):
        """Evento del botón 3"""
        self.status_bar.showMessage('Botón 3 presionado')
        print("Botón 3 clickeado")