from Model.db import db_manager

def validate_credentials(username, password):
    """Validar credenciales de administrador"""
    query = """
        SELECT COUNT(*) FROM administrador
        WHERE usuario_admin = %s AND contrasena_admin = %s
    """
    result = db_manager.execute_query(query, (username, password), fetchone=True)
    return result and result[0] > 0