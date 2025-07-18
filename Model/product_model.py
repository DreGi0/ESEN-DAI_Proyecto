from Model.db import db_manager


def get_products():
    """
    Obtener todos los productos con sus relaciones
    
    Returns:
        list: Lista de tuplas con información completa de productos
    """
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


def get_product_by_id(product_id):
    """
    Obtener un producto por su ID con información completa
    
    Args:
        product_id (int): ID del producto
        
    Returns:
        tuple: Información completa del producto o None si no existe
    """
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
    return db_manager.execute_query(query, (product_id,), fetchone=True)


def create_product(name, description, location, unit_price, category_id, unit_id):
    """
    Crear un nuevo producto
    
    Args:
        name (str): Nombre del producto
        description (str): Descripción del producto
        location (str): Ubicación del producto
        unit_price (float): Precio unitario del producto
        category_id (int): ID de la categoría
        unit_id (int): ID de la unidad de medida
        
    Returns:
        bool: True si se creó exitosamente, False en caso contrario
    """
    query = """
        INSERT INTO producto (nombre_prod, descripcion_prod, ubicacion_prod, 
                            precio_unitario_prod, id_categoria, id_unidad_medida)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    result = db_manager.execute_query(query, (name, description, location, unit_price, category_id, unit_id))
    return result is not None and result > 0


def update_product(product_id, name, description, location, unit_price, category_id, unit_id):
    """
    Actualizar un producto existente
    
    Args:
        product_id (int): ID del producto
        name (str): Nuevo nombre del producto
        description (str): Nueva descripción del producto
        location (str): Nueva ubicación del producto
        unit_price (float): Nuevo precio unitario del producto
        category_id (int): ID de la nueva categoría
        unit_id (int): ID de la nueva unidad de medida
        
    Returns:
        bool: True si se actualizó exitosamente, False en caso contrario
    """
    query = """
        UPDATE producto 
        SET nombre_prod = %s, descripcion_prod = %s, ubicacion_prod = %s,
            precio_unitario_prod = %s, id_categoria = %s, id_unidad_medida = %s
        WHERE id_prod = %s
    """
    result = db_manager.execute_query(query, (name, description, location, unit_price, category_id, unit_id, product_id))
    return result is not None and result > 0


def delete_product(product_id):
    """
    Eliminar un producto (verificando dependencias)
    
    Args:
        product_id (int): ID del producto a eliminar
        
    Returns:
        bool: True si se eliminó exitosamente, False en caso contrario
    """
    # Verificar dependencias con proveedores
    check_query = "SELECT COUNT(*) FROM producto_proveedor WHERE id_prod = %s"
    check_result = db_manager.execute_query(check_query, (product_id,), fetchone=True)
    
    if check_result and check_result[0] > 0:
        print("No se puede eliminar: el producto tiene proveedores asociados")
        return False
    
    # Eliminar el producto
    delete_query = "DELETE FROM producto WHERE id_prod = %s"
    result = db_manager.execute_query(delete_query, (product_id,))
    return result is not None and result > 0


def get_products_by_provider(provider_id):
    """
    Obtener productos de un proveedor específico
    
    Args:
        provider_id (int): ID del proveedor
        
    Returns:
        list: Lista de productos del proveedor con precios de compra
    """
    query = """
        SELECT pp.id_producto_proveedor, p.nombre_prod, pp.precio_compra
        FROM producto_proveedor pp
        JOIN producto p ON pp.id_prod = p.id_prod
        WHERE pp.id_prov = %s
        ORDER BY p.nombre_prod
    """
    return db_manager.execute_query(query, (provider_id,), fetch=True)


def get_product_suppliers(product_id):
    """
    Obtener proveedores de un producto específico
    
    Args:
        product_id (int): ID del producto
        
    Returns:
        list: Lista de proveedores del producto con precios de compra
    """
    query = """
        SELECT pp.id_producto_proveedor, pp.precio_compra,
               prov.id_prov, prov.nombre_prov, prov.apellido_prov
        FROM producto_proveedor pp
        INNER JOIN proveedor prov ON pp.id_prov = prov.id_prov
        WHERE pp.id_prod = %s
        ORDER BY prov.nombre_prov, prov.apellido_prov
    """
    result = db_manager.execute_query(query, (product_id,), fetch=True)
    return result if result is not None else []


def assign_supplier_to_product(product_id, provider_id, purchase_price):
    """
    Asignar un proveedor a un producto
    
    Args:
        product_id (int): ID del producto
        provider_id (int): ID del proveedor
        purchase_price (float): Precio de compra del producto
        
    Returns:
        bool: True si se asignó exitosamente, False en caso contrario
    """
    query = """
        INSERT INTO producto_proveedor (id_prod, id_prov, precio_compra)
        VALUES (%s, %s, %s)
    """
    result = db_manager.execute_query(query, (product_id, provider_id, purchase_price))
    return result is not None and result > 0


def get_categories():
    """
    Obtener todas las categorías
    
    Returns:
        list: Lista de tuplas con información de categorías
    """
    query = "SELECT id_categoria, nombre_categoria FROM categoria ORDER BY nombre_categoria"
    result = db_manager.execute_query(query, fetch=True)
    return result if result is not None else []


def get_units():
    """
    Obtener todas las unidades de medida
    
    Returns:
        list: Lista de tuplas con información de unidades de medida
    """
    query = "SELECT id_unidad_medida, nombre_unidad, abreviatura_unidad FROM unidad_medida ORDER BY nombre_unidad"
    result = db_manager.execute_query(query, fetch=True)
    return result if result is not None else []


def get_suppliers():
    """
    Obtener todos los proveedores
    
    Returns:
        list: Lista de tuplas con información de proveedores
    """
    query = "SELECT id_prov, nombre_prov, apellido_prov FROM proveedor ORDER BY nombre_prov"
    result = db_manager.execute_query(query, fetch=True)
    return result if result is not None else []


def search_products(search_term):
    """
    Buscar productos por nombre o descripción
    
    Args:
        search_term (str): Término de búsqueda
        
    Returns:
        list: Lista de productos que coinciden con la búsqueda
    """
    query = """
        SELECT p.id_prod, p.nombre_prod, p.descripcion_prod, 
               p.precio_unitario_prod, p.ubicacion_prod,
               c.nombre_categoria, u.nombre_unidad, u.abreviatura_unidad
        FROM producto p
        LEFT JOIN categoria c ON p.id_categoria = c.id_categoria
        LEFT JOIN unidad_medida u ON p.id_unidad_medida = u.id_unidad_medida
        WHERE p.nombre_prod LIKE %s OR p.descripcion_prod LIKE %s
        ORDER BY p.nombre_prod
    """
    search_pattern = f"%{search_term}%"
    result = db_manager.execute_query(query, (search_pattern, search_pattern), fetch=True)
    return result if result is not None else []