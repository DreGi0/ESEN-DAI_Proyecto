from Model.db import db_manager


def create_client(first_name, last_name):
    """
    Crear un nuevo cliente
    
    Args:
        first_name (str): Nombre del cliente
        last_name (str): Apellido del cliente
        
    Returns:
        int: Número de filas afectadas o None si hay error
    """
    query = """
        INSERT INTO clientes (nombre_cliente, apellido_cliente)
        VALUES (%s, %s)
    """
    params = (first_name, last_name)
    return db_manager.execute_query(query, params)


def get_all_clients():
    """
    Obtener todos los clientes
    
    Returns:
        list: Lista de tuplas con información de clientes
    """
    query = """
        SELECT id_cliente, nombre_cliente, apellido_cliente 
        FROM clientes
        ORDER BY nombre_cliente, apellido_cliente
    """
    return db_manager.execute_query(query, fetch=True)


def get_client_by_id(client_id):
    """
    Obtener un cliente por su ID
    
    Args:
        client_id (int): ID del cliente
        
    Returns:
        tuple: Información del cliente o None si no existe
    """
    query = """
        SELECT id_cliente, nombre_cliente, apellido_cliente 
        FROM clientes
        WHERE id_cliente = %s
    """
    return db_manager.execute_query(query, (client_id,), fetchone=True)


def update_client(client_id, first_name, last_name):
    """
    Actualizar información de un cliente
    
    Args:
        client_id (int): ID del cliente
        first_name (str): Nuevo nombre del cliente
        last_name (str): Nuevo apellido del cliente
        
    Returns:
        int: Número de filas afectadas o False si hay error
    """
    try:
        query = """
            UPDATE clientes 
            SET nombre_cliente = %s, apellido_cliente = %s 
            WHERE id_cliente = %s
        """
        params = (first_name, last_name, client_id)
        return db_manager.execute_query(query, params)
    except Exception as e:
        print(f"Error al actualizar cliente: {e}")
        return False


def delete_client(client_id):
    """
    Eliminar un cliente de la base de datos
    
    Args:
        client_id (int): ID del cliente a eliminar
        
    Returns:
        int: Número de filas afectadas o False si hay error
    """
    try:
        query = """
            DELETE FROM clientes WHERE id_cliente = %s
        """
        params = (client_id,)
        return db_manager.execute_query(query, params)
    except Exception as e:
        print(f"Error al eliminar cliente: {e}")
        return False


def search_clients(search_term):
    """
    Buscar clientes por nombre o apellido
    
    Args:
        search_term (str): Término de búsqueda
        
    Returns:
        list: Lista de clientes que coinciden con la búsqueda
    """
    query = """
        SELECT id_cliente, nombre_cliente, apellido_cliente 
        FROM clientes
        WHERE nombre_cliente LIKE %s OR apellido_cliente LIKE %s
        ORDER BY nombre_cliente, apellido_cliente
    """
    search_pattern = f"%{search_term}%"
    return db_manager.execute_query(query, (search_pattern, search_pattern), fetch=True)