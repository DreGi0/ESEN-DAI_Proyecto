from Model.db import db_manager

"""def filtered_products(name=None, category_id=None, location=None):
    query = "SELECT id_prod, nombre_prod, id_categoria, ubicacion_prod FROM producto WHERE 1=1"
    filters = []

    if name:
        query += " AND nombre_prod LIKE %s"
        filters.append(f"%{name}%")
    if category_id:
        query += " AND id_categoria = %s"
        filters.append(category_id)
    if location:
        query += " AND ubicacion_prod LIKE %s"
        filters.append(f"%{location}%")

    results = db_manager.execute_query(query, filters, fetch=True)
    return results"""

def filtered_products(name=None, category_id=None, location=None):
    query = """
        SELECT p.id_prod, p.nombre_prod, c.nombre_categoria, p.ubicacion_prod
        FROM producto p
        LEFT JOIN categoria c ON p.id_categoria = c.id_categoria
        WHERE 1=1
    """
    filters = []

    if name:
        query += " AND p.nombre_prod LIKE %s"
        filters.append(f"%{name}%")
    if category_id:
        query += " AND p.id_categoria = %s"
        filters.append(category_id)
    if location:
        query += " AND p.ubicacion_prod LIKE %s"
        filters.append(f"%{location}%")

    results = db_manager.execute_query(query, filters, fetch=True)
    return results



def get_categories():
    query = "SELECT id_categoria, nombre_categoria FROM categoria"
    rows = db_manager.execute_query(query, fetch=True)
    if rows is None:
        return []
    return rows  


