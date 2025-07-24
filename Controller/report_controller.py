from Model import report_model
from Model import product_model
from datetime import datetime


class ReportController:
    """
    Controlador para manejar el reporte de ventas por mes por producto.
    """
    
    def __init__(self):
        """Inicializa el controlador cargando los datos de ventas."""
        self.data = report_model.get_sales_by_month()

    # ==========================================================================
    # CONSULTA DE REPORTE
    # ==========================================================================
    
    def get_sales_summary(self):
        """
        Obtiene las ventas mensuales por producto.

        Returns:
            dict: Diccionario con nombre_prod como clave y una lista de ventas por mes como valor.
        """
        ventas_por_producto = {}

        for nombre_prod, mes, total_ventas in self.data:
            if nombre_prod not in ventas_por_producto:
                ventas_por_producto[nombre_prod] = [0] * 12
            if 1 <= mes <= 12:
                ventas_por_producto[nombre_prod][mes - 1] += float(total_ventas)
        return ventas_por_producto