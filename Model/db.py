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


def get_all_products():
    """Obtener todos los productos con sus relaciones"""
    conn = connect()
    if conn is None:
        return []
    
    try:
        cursor = conn.cursor()
        query = """
            SELECT p.id_prod, p.nombre_prod, p.descripcion_prod, 
                   p.precio_unitario_prod, p.ubicacion_prod,
                   c.nombre_categoria, u.nombre_unidad, u.abreviatura_unidad
            FROM producto p
            LEFT JOIN categoria c ON p.id_categoria = c.id_categoria
            LEFT JOIN unidad_medida u ON p.id_unidad_medida = u.id_unidad_medida
            ORDER BY p.nombre_prod
        """
        cursor.execute(query)
        return cursor.fetchall()
    except Error as e:
        print(f"❌ Error al obtener productos: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def create_product(nombre, descripcion, ubicacion, precio, id_categoria, id_unidad):
    """Crear un nuevo producto"""
    conn = connect()
    if conn is None:
        return False
    
    try:
        cursor = conn.cursor()
        query = """
            INSERT INTO producto (nombre_prod, descripcion_prod, ubicacion_prod, 
                                precio_unitario_prod, id_categoria, id_unidad_medida)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (nombre, descripcion, ubicacion, precio, id_categoria, id_unidad))
        conn.commit()
        return True
    except Error as e:
        print(f"❌ Error al crear producto: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

def update_product(id_prod, nombre, descripcion, ubicacion, precio, id_categoria, id_unidad):
    """Actualizar un producto existente"""
    conn = connect()
    if conn is None:
        return False
    
    try:
        cursor = conn.cursor()
        query = """
            UPDATE producto 
            SET nombre_prod = %s, descripcion_prod = %s, ubicacion_prod = %s,
                precio_unitario_prod = %s, id_categoria = %s, id_unidad_medida = %s
            WHERE id_prod = %s
        """
        cursor.execute(query, (nombre, descripcion, ubicacion, precio, id_categoria, id_unidad, id_prod))
        conn.commit()
        return cursor.rowcount > 0
    except Error as e:
        print(f"❌ Error al actualizar producto: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

def delete_product(id_prod):
    """Eliminar un producto"""
    conn = connect()
    if conn is None:
        return False
    
    try:
        cursor = conn.cursor()
        # Verificar si el producto tiene dependencias
        cursor.execute("SELECT COUNT(*) FROM producto_proveedor WHERE id_prod = %s", (id_prod,))
        (count,) = cursor.fetchone()
        
        if count > 0:
            print("❌ No se puede eliminar: el producto tiene proveedores asociados")
            return False
        
        # Eliminar el producto
        cursor.execute("DELETE FROM producto WHERE id_prod = %s", (id_prod,))
        conn.commit()
        return cursor.rowcount > 0
    except Error as e:
        print(f"❌ Error al eliminar producto: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

def get_product_by_id(id_prod):
    """Obtener un producto por su ID"""
    conn = connect()
    if conn is None:
        return None
    
    try:
        cursor = conn.cursor()
        query = """
            SELECT p.id_prod, p.nombre_prod, p.descripcion_prod, 
                   p.precio_unitario_prod, p.ubicacion_prod,
                   p.id_categoria, p.id_unidad_medida,
                   c.nombre_categoria, u.nombre_unidad
            FROM producto p
            LEFT JOIN categoria c ON p.id_categoria = c.id_categoria
            LEFT JOIN unidad_medida u ON p.id_unidad_medida = u.id_unidad_medida
            WHERE p.id_prod = %s
        """
        cursor.execute(query, (id_prod,))
        return cursor.fetchone()
    except Error as e:
        print(f"❌ Error al obtener producto: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

def get_product_suppliers(id_prod):
    """Obtener proveedores de un producto específico"""
    conn = connect()
    if conn is None:
        return []
    
    try:
        cursor = conn.cursor()
        query = """
            SELECT pp.id_producto_proveedor, pp.precio_compra,
                   prov.id_prov, prov.nombre_prov, prov.apellido_prov
            FROM producto_proveedor pp
            INNER JOIN proveedor prov ON pp.id_prov = prov.id_prov
            WHERE pp.id_prod = %s
        """
        cursor.execute(query, (id_prod,))
        return cursor.fetchall()
    except Error as e:
        print(f"❌ Error al obtener proveedores: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def assign_supplier_to_product(id_prod, id_prov, precio_compra):
    """Asignar un proveedor a un producto"""
    conn = connect()
    if conn is None:
        return False
    
    try:
        cursor = conn.cursor()
        query = """
            INSERT INTO producto_proveedor (id_prod, id_prov, precio_compra)
            VALUES (%s, %s, %s)
        """
        cursor.execute(query, (id_prod, id_prov, precio_compra))
        conn.commit()
        return True
    except Error as e:
        print(f"❌ Error al asignar proveedor: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

def get_categories():
    """Obtener todas las categorías"""
    conn = connect()
    if conn is None:
        return []
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id_categoria, nombre_categoria FROM categoria ORDER BY nombre_categoria")
        return cursor.fetchall()
    except Error as e:
        print(f"❌ Error al obtener categorías: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def get_units():
    """Obtener todas las unidades de medida"""
    conn = connect()
    if conn is None:
        return []
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id_unidad_medida, nombre_unidad, abreviatura_unidad FROM unidad_medida ORDER BY nombre_unidad")
        return cursor.fetchall()
    except Error as e:
        print(f"❌ Error al obtener unidades: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def get_suppliers():
    """Obtener todos los proveedores"""
    conn = connect()
    if conn is None:
        return []
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id_prov, nombre_prov, apellido_prov FROM proveedor ORDER BY nombre_prov")
        return cursor.fetchall()
    except Error as e:
        print(f"❌ Error al obtener proveedores: {e}")
        return []
    finally:
        cursor.close()
        conn.close()