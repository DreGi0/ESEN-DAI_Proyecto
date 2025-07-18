# CRUD de facturación para ventas y compras
from Model.db import db_manager


def create_invoice(tipo_factura, fecha_factura, id_cliente, id_prov, id_administrador, metodo_pago, total):
    """
    Crear una nueva factura
    
    Args:
        tipo_factura (str): Tipo de factura (venta/compra)
        fecha_factura (date): Fecha de la factura
        id_cliente (int): ID del cliente (opcional para compras)
        id_prov (int): ID del proveedor (opcional para ventas)
        id_administrador (int): ID del administrador
        metodo_pago (str): Método de pago
        total (float): Total de la factura
        
    Returns:
        int: Número de filas afectadas o None si hay error
    """
    query = """
        INSERT INTO factura (tipo_factura, fecha_factura, id_cliente, id_prov, id_administrador, metodo_pago, total)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    params = (tipo_factura, fecha_factura, id_cliente, id_prov, id_administrador, metodo_pago, total)
    return db_manager.execute_query(query, params)


def get_all_invoices():
    """
    Obtener todas las facturas
    
    Returns:
        list: Lista de tuplas con información de facturas
    """
    query = """
        SELECT id_factura, tipo_factura, fecha_factura, id_cliente, id_prov, 
               id_administrador, metodo_pago, total
        FROM factura
        ORDER BY fecha_factura DESC
    """
    return db_manager.execute_query(query, fetch=True)


def get_invoice_by_id(invoice_id):
    """
    Obtener una factura por su ID
    
    Args:
        invoice_id (int): ID de la factura
        
    Returns:
        tuple: Información de la factura o None si no existe
    """
    query = """
        SELECT id_factura, tipo_factura, fecha_factura, id_cliente, id_prov, 
               id_administrador, metodo_pago, total
        FROM factura
        WHERE id_factura = %s
    """
    return db_manager.execute_query(query, (invoice_id,), fetchone=True)


def update_invoice(invoice_id, tipo_factura, fecha_factura, id_cliente, id_prov, id_administrador, metodo_pago, total):
    """
    Actualizar información de una factura
    
    Args:
        invoice_id (int): ID de la factura
        tipo_factura (str): Tipo de factura
        fecha_factura (date): Fecha de la factura
        id_cliente (int): ID del cliente
        id_prov (int): ID del proveedor
        id_administrador (int): ID del administrador
        metodo_pago (str): Método de pago
        total (float): Total de la factura
        
    Returns:
        int: Número de filas afectadas o False si hay error
    """
    try:
        query = """
            UPDATE factura 
            SET tipo_factura = %s, fecha_factura = %s, id_cliente = %s, id_prov = %s, 
                id_administrador = %s, metodo_pago = %s, total = %s
            WHERE id_factura = %s
        """
        params = (tipo_factura, fecha_factura, id_cliente, id_prov, id_administrador, metodo_pago, total, invoice_id)
        return db_manager.execute_query(query, params)
    except Exception as e:
        print(f"Error al actualizar factura: {e}")
        return False


def update_invoice_total(id_factura, total):
    """
    Actualizar solo el total de una factura
    
    Args:
        id_factura (int): ID de la factura
        total (float): Nuevo total
        
    Returns:
        int: Número de filas afectadas o False si hay error
    """
    try:
        query = "UPDATE factura SET total = %s WHERE id_factura = %s"
        params = (total, id_factura)
        return db_manager.execute_query(query, params)
    except Exception as e:
        print(f"Error al actualizar total de factura: {e}")
        return False


def delete_invoice(invoice_id):
    """
    Eliminar una factura de la base de datos
    
    Args:
        invoice_id (int): ID de la factura a eliminar
        
    Returns:
        int: Número de filas afectadas o False si hay error
    """
    try:
        query = """
            DELETE FROM factura WHERE id_factura = %s
        """
        params = (invoice_id,)
        return db_manager.execute_query(query, params)
    except Exception as e:
        print(f"Error al eliminar factura: {e}")
        return False


def search_invoices(search_term):
    """
    Buscar facturas por tipo o método de pago
    
    Args:
        search_term (str): Término de búsqueda
        
    Returns:
        list: Lista de facturas que coinciden con la búsqueda
    """
    query = """
        SELECT id_factura, tipo_factura, fecha_factura, id_cliente, id_prov, 
               id_administrador, metodo_pago, total
        FROM factura
        WHERE tipo_factura LIKE %s OR metodo_pago LIKE %s
        ORDER BY fecha_factura DESC
    """
    search_pattern = f"%{search_term}%"
    return db_manager.execute_query(query, (search_pattern, search_pattern), fetch=True)


def get_invoices_by_client(client_id):
    """
    Obtener facturas por cliente
    
    Args:
        client_id (int): ID del cliente
        
    Returns:
        list: Lista de facturas del cliente
    """
    query = """
        SELECT id_factura, tipo_factura, fecha_factura, id_cliente, id_prov, 
               id_administrador, metodo_pago, total
        FROM factura
        WHERE id_cliente = %s
        ORDER BY fecha_factura DESC
    """
    return db_manager.execute_query(query, (client_id,), fetch=True)


def get_invoices_by_provider(provider_id):
    """
    Obtener facturas por proveedor
    
    Args:
        provider_id (int): ID del proveedor
        
    Returns:
        list: Lista de facturas del proveedor
    """
    query = """
        SELECT id_factura, tipo_factura, fecha_factura, id_cliente, id_prov, 
               id_administrador, metodo_pago, total
        FROM factura
        WHERE id_prov = %s
        ORDER BY fecha_factura DESC
    """
    return db_manager.execute_query(query, (provider_id,), fetch=True)


def get_invoices_by_date_range(start_date, end_date):
    """
    Obtener facturas en un rango de fechas
    
    Args:
        start_date (date): Fecha de inicio
        end_date (date): Fecha de fin
        
    Returns:
        list: Lista de facturas en el rango de fechas
    """
    query = """
        SELECT id_factura, tipo_factura, fecha_factura, id_cliente, id_prov, 
               id_administrador, metodo_pago, total
        FROM factura
        WHERE fecha_factura BETWEEN %s AND %s
        ORDER BY fecha_factura DESC
    """
    return db_manager.execute_query(query, (start_date, end_date), fetch=True)


def add_invoice_detail(id_factura, id_producto_proveedor, cantidad_detalle, precio_unitario_detalle):
    """
    Agregar detalle a una factura
    
    Args:
        id_factura (int): ID de la factura
        id_producto_proveedor (int): ID del producto del proveedor
        cantidad_detalle (int): Cantidad del producto
        precio_unitario_detalle (float): Precio unitario del producto
        
    Returns:
        int: Número de filas afectadas o None si hay error
    """
    query = """
        INSERT INTO detalle_factura (id_factura, id_producto_proveedor, cantidad_detalle, precio_unitario_detalle)
        VALUES (%s, %s, %s, %s)
    """
    params = (id_factura, id_producto_proveedor, cantidad_detalle, precio_unitario_detalle)
    return db_manager.execute_query(query, params)


def get_invoice_details(invoice_id):
    """
    Obtener los detalles de una factura
    
    Args:
        invoice_id (int): ID de la factura
        
    Returns:
        list: Lista de detalles de la factura
    """
    query = """
        SELECT id_detalle, id_factura, id_producto_proveedor, cantidad_detalle, precio_unitario_detalle
        FROM detalle_factura
        WHERE id_factura = %s
    """
    return db_manager.execute_query(query, (invoice_id,), fetch=True)


def update_invoice_detail(detail_id, cantidad_detalle, precio_unitario_detalle):
    """
    Actualizar un detalle de factura
    
    Args:
        detail_id (int): ID del detalle
        cantidad_detalle (int): Nueva cantidad
        precio_unitario_detalle (float): Nuevo precio unitario
        
    Returns:
        int: Número de filas afectadas o False si hay error
    """
    try:
        query = """
            UPDATE detalle_factura 
            SET cantidad_detalle = %s, precio_unitario_detalle = %s 
            WHERE id_detalle = %s
        """
        params = (cantidad_detalle, precio_unitario_detalle, detail_id)
        return db_manager.execute_query(query, params)
    except Exception as e:
        print(f"Error al actualizar detalle de factura: {e}")
        return False


def delete_invoice_detail(detail_id):
    """
    Eliminar un detalle de factura
    
    Args:
        detail_id (int): ID del detalle a eliminar
        
    Returns:
        int: Número de filas afectadas o False si hay error
    """
    try:
        query = """
            DELETE FROM detalle_factura WHERE id_detalle = %s
        """
        params = (detail_id,)
        return db_manager.execute_query(query, params)
    except Exception as e:
        print(f"Error al eliminar detalle de factura: {e}")
        return False


def get_all_providers():
    """
    Obtener todos los proveedores
    
    Returns:
        list: Lista de tuplas con información de proveedores
    """
    query = "SELECT id_prov, nombre_prov, apellido_prov FROM proveedor"
    return db_manager.execute_query(query, fetch=True)


def get_all_clients():
    """
    Obtener todos los clientes
    
    Returns:
        list: Lista de tuplas con información de clientes
    """
    query = "SELECT id_cliente, nombre_cliente, apellido_cliente FROM clientes"
    return db_manager.execute_query(query, fetch=True)