# CRUD de clientes para facturación de ventas.
from Model.db import db_manager

def create_cliente(nombre_cliente, apellido_cliente):
    query = """
    INSERT INTO clientes (nombre_cliente, apellido_cliente)
    VALUES (%s, %s) """
    params = (nombre_cliente, apellido_cliente)
    return db_manager.execute_query(query, params)

def load_cliente():
    query = """
    SELECT id_cliente, nombre_cliente, apellido_cliente FROM clientes
    """
    return db_manager.execute_query(query, fetch=True)

def update_cliente(id_cliente, nombre_cliente, apellido_cliente):
        try:
            query = """
            UPDATE clientes SET nombre_cliente = %s, apellido_cliente = %s WHERE id_cliente = %s
            """
            params = (nombre_cliente, apellido_cliente, id_cliente)
            return db_manager.execute_query(query, params)
        except Exception as e:
            return False
        
def get_all_clientes():
    """Obtiene los clientes"""
    query = "SELECT id_cliente, nombre_cliente, apellido_cliente FROM clientes"
    return db_manager.execute_query(query, fetch = True)

def del_cliente(id_cliente):
    """ borra un cliente de la bd"""
    try:
        query = """
        DELETE FROM clientes WHERE id_cliente = %s
        """
        params = (id_cliente,)
        return db_manager.execute_query(query, params)
    except Exception as e:
        return False