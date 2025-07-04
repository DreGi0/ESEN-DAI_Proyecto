import mysql.connector
from mysql.connector import Error

def connect():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="1234",
            database="Ferreteria_Monaco"
        )
        if conn.is_connected():
            print("✅ Conexión exitosa a la base de datos")
        return conn
    except Error as e:
        print(f"❌ Error al conectar: {e}")
        return None


def validate_credentials(username, password):
    conn = connect()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()
        query = """
            SELECT COUNT(*) FROM administrador
            WHERE usuario_admin = %s AND contrasena_admin = %s
        """
        cursor.execute(query, (username, password))
        (count,) = cursor.fetchone()
        return count > 0
    except Error as e:
        print(f"❌ Error durante la validación: {e}")
        return False
    finally:
        cursor.close()
        conn.close()


# Para pruebas rápidas
if __name__ == "__main__":
    if validate_credentials("Alvin123", "Alvin123"):
        print("✅ Credenciales válidas")
    else:
        print("❌ Credenciales inválidas")
