from Model.db import db_manager

def create_invoice(tipo_factura, fecha_factura, id_cliente, id_prov, id_administrador, metodo_pago, total):
    """Crear la factura"""
    query = """
    INSERT INTO factura (tipo_factura, fecha_factura, id_cliente, id_prov, id_administrador, metodo_pago, total)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    result = db_manager.execute_query(query, (tipo_factura, fecha_factura, id_cliente, id_prov, id_administrador, metodo_pago, total))
    return result is not None and result > 0

def add_invoice_detail(id_factura, id_producto_proveedor, cantidad_detalle, precio_unitario_detalle):
    """Agregar el detalle de factura"""
    query = """
    INSERT INTO detalle_factura (id_factura, id_producto_proveedor, cantidad_detalle, precio_unitario_detalle)
    VALUES (%s, %s, %s, %s)
    """
    params = (id_factura, id_producto_proveedor, cantidad_detalle, precio_unitario_detalle)
    return db_manager.execute_query(query, params)

def update_invoice_total(id_factura, total):
    """Actualizar el total en la factura"""
    query = "UPDATE factura SET Total = %s WHERE id_factura = %s"
    params = (total, id_factura)
    return db_manager.execute_query(query, params)

def get_all_clients():
    """Obtiener los clientes"""
    query = "SELECT id_cliente, nombre_cliente, apellido_cliente FROM cliente"
    return db_manager.execute_query(query, fetch = True)

def get_all_providers():
    """Obtiene los proveedores"""
    query = "SELECT id_prov, nombre_prov, apellido_prov FROM proveedor"
    return db_manager.execute_query(query, fetch = True)

def get_products_by_provider(id_prov):
    """Obtiener los productos de un proveedor"""
    query = """
    SELECT pp.id_producto_proveedor, p.nombre_prod, pp.precio_compra
    FROM producto_proveedor pp
    JOIN producto p ON pp.id_prod = p.id_prod
    WHERE pp.id_prov = %s
    """
    return db_manager.execute_query(query, (id_prov,), fetch = True)