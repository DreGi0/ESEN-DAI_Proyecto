from Model.db import connect

class FacturaModel:
    def __init__(self):
        pass
    
    def obtener_clientes(self):
        """Otiene la lista de clientes"""
        conn = None
        cursor = None
        try:
            conn = connect()
            if conn is None:
                return []
            cursor = conn.cursor()
            cursor.execute("SELECT id_cliente, nombre_cliente FROM cliente")
            clientes = cursor.fetchall()
            return clientes
        except Exception as e:
            print(f"Error al obtener clientes: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def obtener_administradores(self):
        """Otiene la lista de administradores"""
        conn = None
        cursor = None
        try:
            conn = connect()
            if conn is None:
                return []
            cursor = conn.cursor()
            cursor.execute("SELECT id_admin, nombre_admin FROM administrador")
            admins = cursor.fetchall()
            return admins
        except Exception as e:
            print(f"Error al obtener administradores: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def obtener_productos(self):
        """Obtiene la lista de productos"""
        conn = None
        cursor = None
        try:
            conn = connect()
            if conn is None:
                return []
            cursor = conn.cursor()
            cursor.execute("SELECT id_producto, nombre_producto FROM producto")
            productos = cursor.fetchall()
            return productos
        except Exception as e:
            print(f"Error al obtener productos: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def obtener_precio_producto(self, id_producto):
        """Obtiene el precio unitario del producto"""
        conn = None
        cursor = None
        try:
            conn = connect()
            if conn is None:
                return 0.0
            cursor = conn.cursor()
            query = """
                SELECT precio
                FROM producto_proveedor
                WHERE id_producto = %s
                LIMIT 1
            """
            cursor.execute(query, (id_producto,))
            result = cursor.fetchone()
            if result:
                return float(result[0])
            else:
                return 0.0
        except Exception as e:
            print(f"Error al obtener precio del producto: {e}")
            return 0.0
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def guardar_factura(self, id_cliente, id_admin, total, detalles):
        """Guarda una factura y sus detalles en la base"""
        conn = None
        cursor = None
        try:
            conn = connect()
            if conn is None:
                return False
            cursor = conn.cursor()

            # Insertar la factura principal
            query_factura = """
                INSERT INTO factura (id_cliente, id_admin, fecha_factura, total)
                VALUES (%s, %s, NOW(), %s)
            """
            cursor.execute(query_factura, (id_cliente, id_admin, total))
            id_factura = cursor.lastrowid

            # Insertar cada detalle de la factura
            query_detalle = """
                INSERT INTO detalle_factura (id_factura, id_producto, cantidad, precio_unitario, subtotal)
                VALUES (%s, %s, %s, %s, %s)
            """
            for detalle in detalles:
                id_producto, cantidad, precio_unitario = detalle
                subtotal = cantidad * precio_unitario
                cursor.execute(query_detalle, (id_factura, id_producto, cantidad, precio_unitario, subtotal))

            conn.commit()
            return True

        except Exception as e:
            print(f"Error al guardar la factura: {e}")
            if conn:
                conn.rollback()
            return False 
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()