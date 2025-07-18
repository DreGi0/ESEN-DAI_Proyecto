from Model.db import db_manager


def validate_credentials(username, password):
    """
    Validar credenciales de administrador
    
    Args:
        username (str): Nombre de usuario del administrador
        password (str): Contraseña del administrador
        
    Returns:
        bool: True si las credenciales son válidas, False en caso contrario
    """
    query = """
        SELECT COUNT(*) FROM administrador
        WHERE usuario_admin = %s AND contrasena_admin = %s
    """
    result = db_manager.execute_query(query, (username, password), fetchone=True)
    return result and result[0] > 0


def get_admin_by_credentials(username, password):
    """
    Obtener información del administrador por credenciales
    
    Args:
        username (str): Nombre de usuario del administrador
        password (str): Contraseña del administrador
        
    Returns:
        tuple: Información del administrador o None si no existe
    """
    query = """
        SELECT id_administrador, usuario_admin, nombre_admin, apellido_admin
        FROM administrador
        WHERE usuario_admin = %s AND contrasena_admin = %s
    """
    return db_manager.execute_query(query, (username, password), fetchone=True)