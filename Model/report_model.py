from Model.db import db_manager

def get_sales_by_month():
    """
    Obtener las ventas totales por mes agrupadas por producto.

    Returns:
        list: Lista de tuplas (nombre_prod, mes, total_ventas)
    """
    query = """
        SELECT 
            p.nombre_prod,
            MONTH(f.fecha_factura) AS mes,
            SUM(df.cantidad_detalle * df.precio_unitario_detalle) AS total_ventas
        FROM 
            factura f
        JOIN detalle_factura df ON f.id_factura = df.id_factura
        JOIN producto_proveedor pp ON df.id_producto_proveedor = pp.id_producto_proveedor
        JOIN producto p ON pp.id_prod = p.id_prod
        WHERE 
            f.tipo_factura = 'Venta'
        GROUP BY 
            p.nombre_prod, mes
        ORDER BY 
            mes, p.nombre_prod
    """
    return db_manager.execute_query(query, fetch=True)