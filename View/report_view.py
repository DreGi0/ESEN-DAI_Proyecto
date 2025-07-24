from PyQt6.QtWidgets import QDialog, QVBoxLayout
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from Controller.report_controller import ReportController

class ReportDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Reporte de Ventas")
        self.setMinimumSize(800, 600)
        self.controller = ReportController()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        # Crear figura y canvas
        self.figure = Figure(figsize=(10, 6))
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.plot_sales_chart()

    def plot_sales_chart(self):
        data = self.controller.get_sales_summary()
        meses = ['Ener', 'Feb', 'Mar', 'Abr', 'May', 'Jun',
                 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']

        ax = self.figure.add_subplot(111)
        ax.clear()

        colores = plt.get_cmap('tab10').colors

        for i, (producto, ventas) in enumerate(data.items()):
            ax.plot(meses, ventas, marker='o', label=producto, color=colores[i % len(colores)])

        ax.set_title("Ventas mensuales por producto")
        ax.set_xlabel("Mes")
        ax.set_ylabel("Total en dólares $")
        ax.legend(
        title="Producto",
        loc='center left',
        bbox_to_anchor=(1.0, 0.5),
        borderaxespad=0.0)
        ax.grid(True, linestyle='--', alpha=0.6)
        self.figure.tight_layout() 