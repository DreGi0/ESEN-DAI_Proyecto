# CRUD de proveedores para compras
from Model.db import db_manager


def create_provider(first_name, last_name):
    """
    Crear un nuevo proveedor
    
    Args:
        first_name (str): Nombre del proveedor
        last_name (str): Apellido del proveedor
        
    Returns:
        int: Número de filas afectadas o None si hay error
    """
    query = """
        INSERT INTO proveedor (nombre_prov, apellido_prov)
        VALUES (%s, %s)
    """
    params = (first_name, last_name)
    return db_manager.execute_query(query, params)


def get_all_providers():
    """
    Obtener todos los proveedores
    
    Returns:
        list: Lista de tuplas con información de proveedores
    """
    query = """
        SELECT id_prov, nombre_prov, apellido_prov 
        FROM proveedor
        ORDER BY nombre_prov, apellido_prov
    """
    return db_manager.execute_query(query, fetch=True)


def get_provider_by_id(provider_id):
    """
    Obtener un proveedor por su ID
    
    Args:
        provider_id (int): ID del proveedor
        
    Returns:
        tuple: Información del proveedor o None si no existe
    """
    query = """
        SELECT id_prov, nombre_prov, apellido_prov 
        FROM proveedor
        WHERE id_prov = %s
    """
    return db_manager.execute_query(query, (provider_id,), fetchone=True)


def update_provider(provider_id, first_name, last_name):
    """
    Actualizar información de un proveedor
    
    Args:
        provider_id (int): ID del proveedor
        first_name (str): Nuevo nombre del proveedor
        last_name (str): Nuevo apellido del proveedor
        
    Returns:
        int: Número de filas afectadas o False si hay error
    """
    try:
        query = """
            UPDATE proveedor 
            SET nombre_prov = %s, apellido_prov = %s 
            WHERE id_prov = %s
        """
        params = (first_name, last_name, provider_id)
        return db_manager.execute_query(query, params)
    except Exception as e:
        print(f"Error al actualizar proveedor: {e}")
        return False


def delete_provider(provider_id):
    """
    Eliminar un proveedor de la base de datos
    
    Args:
        provider_id (int): ID del proveedor a eliminar
        
    Returns:
        int: Número de filas afectadas o False si hay error
    """
    try:
        query = """
            DELETE FROM proveedor WHERE id_prov = %s
        """
        params = (provider_id,)
        return db_manager.execute_query(query, params)
    except Exception as e:
        print(f"Error al eliminar proveedor: {e}")
        return False


def search_providers(search_term):
    """
    Buscar proveedores por nombre o apellido
    
    Args:
        search_term (str): Término de búsqueda
        
    Returns:
        list: Lista de proveedores que coinciden con la búsqueda
    """
    query = """
        SELECT id_prov, nombre_prov, apellido_prov 
        FROM proveedor
        WHERE nombre_prov LIKE %s OR apellido_prov LIKE %s
        ORDER BY nombre_prov, apellido_prov
    """
    search_pattern = f"%{search_term}%"
    return db_manager.execute_query(query, (search_pattern, search_pattern), fetch=True)