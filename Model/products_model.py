from Model.db import db_manager

def get_all_products():
    """Obtener todos los productos con sus relaciones"""
    query = """
        SELECT p.id_prod, p.nombre_prod, p.descripcion_prod, 
               p.precio_unitario_prod, p.ubicacion_prod,
               c.nombre_categoria, u.nombre_unidad, u.abreviatura_unidad
        FROM producto p
        LEFT JOIN categoria c ON p.id_categoria = c.id_categoria
        LEFT JOIN unidad_medida u ON p.id_unidad_medida = u.id_unidad_medida
        ORDER BY p.nombre_prod
    """
    result = db_manager.execute_query(query, fetch=True)
    return result if result is not None else []

def create_product(nombre, descripcion, ubicacion, precio, id_categoria, id_unidad):
    """Crear un nuevo producto"""
    query = """
        INSERT INTO producto (nombre_prod, descripcion_prod, ubicacion_prod, 
                            precio_unitario_prod, id_categoria, id_unidad_medida)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    result = db_manager.execute_query(query, (nombre, descripcion, ubicacion, precio, id_categoria, id_unidad))
    return result is not None and result > 0

def update_product(id_prod, nombre, descripcion, ubicacion, precio, id_categoria, id_unidad):
    """Actualizar un producto existente"""
    query = """
        UPDATE producto 
        SET nombre_prod = %s, descripcion_prod = %s, ubicacion_prod = %s,
            precio_unitario_prod = %s, id_categoria = %s, id_unidad_medida = %s
        WHERE id_prod = %s
    """
    result = db_manager.execute_query(query, (nombre, descripcion, ubicacion, precio, id_categoria, id_unidad, id_prod))
    return result is not None and result > 0

def delete_product(id_prod):
    """Eliminar un producto"""
    # Verificar dependencias
    check_query = "SELECT COUNT(*) FROM producto_proveedor WHERE id_prod = %s"
    check_result = db_manager.execute_query(check_query, (id_prod,), fetchone=True)
    
    if check_result and check_result[0] > 0:
        print("No se puede eliminar: el producto tiene proveedores asociados")
        return False
    
    # Eliminar el producto
    delete_query = "DELETE FROM producto WHERE id_prod = %s"
    result = db_manager.execute_query(delete_query, (id_prod,))
    return result is not None and result > 0

def get_product_by_id(id_prod):
    """Obtener un producto por su ID"""
    query = """
        SELECT p.id_prod, p.nombre_prod, p.descripcion_prod, 
               p.precio_unitario_prod, p.ubicacion_prod,
               p.id_categoria, p.id_unidad_medida,
               c.nombre_categoria, u.nombre_unidad
        FROM producto p
        LEFT JOIN categoria c ON p.id_categoria = c.id_categoria
        LEFT JOIN unidad_medida u ON p.id_unidad_medida = u.id_unidad_medida
        WHERE p.id_prod = %s
    """
    return db_manager.execute_query(query, (id_prod,), fetchone=True)

def get_product_suppliers(id_prod):
    """Obtener proveedores de un producto específico"""
    query = """
        SELECT pp.id_producto_proveedor, pp.precio_compra,
               prov.id_prov, prov.nombre_prov, prov.apellido_prov
        FROM producto_proveedor pp
        INNER JOIN proveedor prov ON pp.id_prov = prov.id_prov
        WHERE pp.id_prod = %s
    """
    result = db_manager.execute_query(query, (id_prod,), fetch=True)
    return result if result is not None else []

def assign_supplier_to_product(id_prod, id_prov, precio_compra):
    """Asignar un proveedor a un producto"""
    query = """
        INSERT INTO producto_proveedor (id_prod, id_prov, precio_compra)
        VALUES (%s, %s, %s)
    """
    result = db_manager.execute_query(query, (id_prod, id_prov, precio_compra))
    return result is not None and result > 0

def get_categories():
    """Obtener todas las categorías"""
    query = "SELECT id_categoria, nombre_categoria FROM categoria ORDER BY nombre_categoria"
    result = db_manager.execute_query(query, fetch=True)
    return result if result is not None else []

def get_units():
    """Obtener todas las unidades de medida"""
    query = "SELECT id_unidad_medida, nombre_unidad, abreviatura_unidad FROM unidad_medida ORDER BY nombre_unidad"
    result = db_manager.execute_query(query, fetch=True)
    return result if result is not None else []

def get_suppliers():
    """Obtener todos los proveedores"""
    query = "SELECT id_prov, nombre_prov, apellido_prov FROM proveedor ORDER BY nombre_prov"
    result = db_manager.execute_query(query, fetch=True)
    return result if result is not None else []
