from Model.db import db_manager
from mysql.connector import Error

def get_all_clients():
    """Obtiener los clientes"""
    query = "SELECT id_cliente, nombre_cliente, apellido_cliente FROM cliente"
    return db_manager.execute_query(query, fetch = True)

def create_client(nombre_cliente, apellido_cliente, correo):  
    connection = db_manager.connection
    cursor = None
    try: 
        cursor = connection.cursor() 
        query_contact = """
                INSERT INTO contacto_clientes (correo)
                VALUES (%s)
            """ 
        cursor.execute(query_contact, (correo,))
        id_contact = cursor.lastrowid
        
        """Crear cliente"""
        query_client = """
        INSERT INTO cliente (nombre_cliente, apellido_cliente, id_contact)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query_client, (nombre_cliente, apellido_cliente, id_contact))
        connection.commit()
        return True
    except Error as e:
        print(f"❌ Error al agregar cliente {e}")
        if connection:
                connection.rollback()
        return False
    finally:
        if cursor:
            cursor.close()