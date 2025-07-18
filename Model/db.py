import faulthandler
import mysql.connector
from mysql.connector import Error
import atexit 


class DatabaseManager:
    """Gestor de base de datos para MySQL con reconexión automática"""
    
    def __init__(self):
        """Inicializar el gestor de base de datos"""
        self.connection = None
        self.connect()
        # Registrar función para cerrar conexión al terminar la aplicación
        atexit.register(self.close_connection) 
    
    def connect(self):
        """Establecer conexión con la base de datos MySQL"""
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="1234",
                database="ferreteria_monaco"
            )
            if self.connection.is_connected():
                print("Conectado a la base de datos")
        except Error as e:
            print(f"Error de conexión: {e}")
            self.connection = None
    
    def is_connected(self):
        """Verificar si la conexión está activa"""
        if self.connection is None:
            return False
        
        try:
            # Ping para verificar la conexión
            self.connection.ping(reconnect=True, attempts=3, delay=1)
            return self.connection.is_connected()
        except Error:
            return False
    
    def ensure_connection(self):
        """Asegurar que la conexión esté activa, reconectar si es necesario"""
        if not self.is_connected():
            print("Reconectando a la base de datos...")
            self.connect()
        return self.connection is not None
    
    def execute_query(self, query, params=None, fetch=False, fetchone=False):
        """
        Ejecutar una consulta de forma segura
        
        Args:
            query (str): Consulta SQL a ejecutar
            params (tuple): Parámetros para la consulta
            fetch (bool): Si debe retornar todos los resultados
            fetchone (bool): Si debe retornar solo un resultado
            
        Returns:
            Resultados de la consulta o None si hay error
        """
        if not self.ensure_connection():
            return None
        
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            
            if fetch:
                return cursor.fetchall()
            elif fetchone:
                return cursor.fetchone()
            else:
                self.connection.commit()
                return cursor.rowcount
        except Error as e:
            print(f"Error en la consulta: {e}")
            if self.connection:
                self.connection.rollback()
            return None
        finally:
            if cursor:
                cursor.close()
    
    def close_connection(self):
        """Cerrar la conexión a la base de datos"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada")


# Instancia global del gestor de base de datos
db_manager = DatabaseManager()


# ==========================================================================
# FUNCIONES PARA MANEJO MANUAL DE LA BASE DE DATOS
# ==========================================================================

def close_database_connection():
    """Cerrar la conexión manualmente"""
    db_manager.close_connection()


def reconnect_database():
    """Reconectar a la base de datos manualmente"""
    db_manager.connect()