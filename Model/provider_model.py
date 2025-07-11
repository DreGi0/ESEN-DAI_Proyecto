from Model.db import db_manager

def get_all_providers():
    """Obtiene los proveedores"""
    query = "SELECT id_prov, nombre_prov, apellido_prov FROM proveedor"
    return db_manager.execute_query(query, fetch = True)