# CRUD de clientes para facturación de ventas.
from Model.db import db_manager

def create_provider(nombre_prov, apellido_prov):
    query = """
    INSERT INTO proveedor (nombre_prov, apellido_prov)
    VALUES (%s, %s) """
    params = (nombre_prov, apellido_prov)
    return db_manager.execute_query(query, params)

def load_provider():
    query = """
    SELECT id_prov, nombre_prov, apellido_prov FROM proveedor
    """
    return db_manager.execute_query(query, fetch=True)

def update_provider(id_prov, nombre_prov, apellido_prov):
        try:
            query = """
            UPDATE proveedor SET nombre_prov = %s, apellido_prov = %s WHERE id_prov = %s
            """
            params = (nombre_prov, apellido_prov, id_prov)
            return db_manager.execute_query(query, params)
        except Exception as e:
            return False
        
def get_all_providers():
    """Obtiene los proveedores"""
    query = "SELECT id_prov, nombre_prov, apellido_prov FROM proveedor"
    return db_manager.execute_query(query, fetch = True)

def del_provider(id_prov):
    """ borra un proveedor de la bd"""
    try:
        query = """
        DELETE FROM proveedor WHERE id_prov = %s
        """
        params = (id_prov,)
        return db_manager.execute_query(query, params)
    except Exception as e:
        return False