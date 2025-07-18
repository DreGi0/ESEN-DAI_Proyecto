from Model.db import db_manager

def insert_inventory_movement(id_prod, cantidad, fecha_actualizacion, tipo_movimiento):
    """Registrar un nuevo movimiento de inventario"""
    query = """
    INSERT INTO inventario (id_prod, cantidad_disponible, fecha_actualizacion, tipo_movimiento)
    VALUES (%s, %s, %s, %s)
    """
    params = (id_prod, cantidad, fecha_actualizacion, tipo_movimiento)
    return db_manager.execute_query(query, params)

def get_inventory():
    """Obtener todos los movimientos de inventario con información de producto"""
    query = """
    SELECT 
        p.id_prod,p.nombre_prod,p.descripcion_prod,
        p.ubicacion_prod,p.precio_unitario_prod,
        i.cantidad_disponible,i.fecha_actualizacion,i.tipo_movimiento
    FROM producto p
    JOIN inventario i ON p.id_prod = i.id_prod
    ORDER BY i.fecha_actualizacion DESC
    """
    return db_manager.execute_query(query, fetch=True)

def get_all_products():
    """Obtener todos los productos"""
    query = "SELECT id_prod, nombre_prod FROM producto"
    return db_manager.execute_query(query, fetch=True)

def get_stock_by_product(id_prod):
    """Obtener el stock actual de un producto (entradas - salidas)"""
    query = """
    SELECT SUM(
        CASE tipo_movimiento
            WHEN 'Entrada' THEN cantidad_disponible
            WHEN 'Salida' THEN -cantidad_disponible
            ELSE 0
        END
    ) AS stock
    FROM inventario
    WHERE id_prod = %s
    """
    return db_manager.execute_query(query, (id_prod,), fetch=True)