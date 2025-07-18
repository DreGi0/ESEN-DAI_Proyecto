from Model.db import db_manager

def insert_inventory_movement(product_id, quantity, update_date, movement_type):
    """
    Registrar un nuevo movimiento de inventario
    
    Args:
        product_id (int): ID del producto
        quantity (int): Cantidad del movimiento
        update_date (str): Fecha de actualización
        movement_type (str): Tipo de movimiento ('Entrada' o 'Salida')
        
    Returns:
        int: Número de filas afectadas o None si hay error
    """
    query = """
        INSERT INTO inventario (id_prod, cantidad_disponible, fecha_actualizacion, tipo_movimiento)
        VALUES (%s, %s, %s, %s)
    """
    params = (product_id, quantity, update_date, movement_type)
    return db_manager.execute_query(query, params)


def get_inventory_history():
    """
    Obtener historial completo de movimientos de inventario con información de producto
    
    Returns:
        list: Lista de tuplas con historial de movimientos
    """
    query = """
        SELECT 
            p.id_prod, p.nombre_prod, p.descripcion_prod,
            p.ubicacion_prod, p.precio_unitario_prod,
            i.cantidad_disponible, i.fecha_actualizacion, i.tipo_movimiento
        FROM producto p
        JOIN inventario i ON p.id_prod = i.id_prod
        ORDER BY i.fecha_actualizacion DESC
    """
    return db_manager.execute_query(query, fetch=True)


def get_inventory_by_product(product_id):
    """
    Obtener historial de movimientos de un producto específico
    
    Args:
        product_id (int): ID del producto
        
    Returns:
        list: Lista de movimientos del producto
    """
    query = """
        SELECT 
            p.id_prod, p.nombre_prod, p.descripcion_prod,
            p.ubicacion_prod, p.precio_unitario_prod,
            i.cantidad_disponible, i.fecha_actualizacion, i.tipo_movimiento
        FROM producto p
        JOIN inventario i ON p.id_prod = i.id_prod
        WHERE p.id_prod = %s
        ORDER BY i.fecha_actualizacion DESC
    """
    return db_manager.execute_query(query, (product_id,), fetch=True)

def get_product_current_stock(product_id):
    """
    Obtener el stock actual de un producto (entradas - salidas)
    
    Args:
        product_id (int): ID del producto
        
    Returns:
        int: Stock actual del producto
    """
    query = """
        SELECT SUM(
            CASE tipo_movimiento
                WHEN 'Entrada' THEN cantidad_disponible
                WHEN 'Salida' THEN -cantidad_disponible
                ELSE 0
            END
        ) AS stock_actual
        FROM inventario
        WHERE id_prod = %s
    """
    result = db_manager.execute_query(query, (product_id,), fetchone=True)
    return result[0] if result and result[0] is not None else 0


def get_all_products_current_stock():
    """
    Obtener el stock actual de todos los productos
    
    Returns:
        list: Lista de tuplas con información de stock por producto
    """
    query = """
        SELECT 
            p.id_prod,
            p.nombre_prod,
            p.descripcion_prod,
            p.ubicacion_prod,
            COALESCE(SUM(
                CASE i.tipo_movimiento
                    WHEN 'Entrada' THEN i.cantidad_disponible
                    WHEN 'Salida' THEN -i.cantidad_disponible
                    ELSE 0
                END
            ), 0) AS stock_actual
        FROM producto p
        LEFT JOIN inventario i ON p.id_prod = i.id_prod
        GROUP BY p.id_prod, p.nombre_prod, p.descripcion_prod, p.ubicacion_prod
        ORDER BY p.nombre_prod
    """
    return db_manager.execute_query(query, fetch=True)


def get_low_stock_products(minimum_stock=5):
    """
    Obtener productos con stock bajo
    
    Args:
        minimum_stock (int): Cantidad mínima de stock considerada baja
        
    Returns:
        list: Lista de productos con stock bajo
    """
    query = """
        SELECT 
            p.id_prod,
            p.nombre_prod,
            p.descripcion_prod,
            p.ubicacion_prod,
            COALESCE(SUM(
                CASE i.tipo_movimiento
                    WHEN 'Entrada' THEN i.cantidad_disponible
                    WHEN 'Salida' THEN -i.cantidad_disponible
                    ELSE 0
                END
            ), 0) AS stock_actual
        FROM producto p
        LEFT JOIN inventario i ON p.id_prod = i.id_prod
        GROUP BY p.id_prod, p.nombre_prod, p.descripcion_prod, p.ubicacion_prod
        HAVING stock_actual < %s
        ORDER BY stock_actual ASC, p.nombre_prod
    """
    return db_manager.execute_query(query, (minimum_stock,), fetch=True)


def get_movements_by_date_range(start_date, end_date):
    """
    Obtener movimientos de inventario en un rango de fechas
    
    Args:
        start_date (str): Fecha de inicio (formato: YYYY-MM-DD)
        end_date (str): Fecha de fin (formato: YYYY-MM-DD)
        
    Returns:
        list: Lista de movimientos en el rango de fechas
    """
    query = """
        SELECT 
            p.id_prod, p.nombre_prod, p.descripcion_prod,
            i.cantidad_disponible, i.fecha_actualizacion, i.tipo_movimiento
        FROM producto p
        JOIN inventario i ON p.id_prod = i.id_prod
        WHERE i.fecha_actualizacion BETWEEN %s AND %s
        ORDER BY i.fecha_actualizacion DESC
    """
    return db_manager.execute_query(query, (start_date, end_date), fetch=True)