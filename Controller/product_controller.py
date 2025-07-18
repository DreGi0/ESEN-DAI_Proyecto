from Model import product_model


class ProductController:
    """
    Controlador para manejar todas las operaciones relacionadas con productos.
    """
    
    def __init__(self):
        """Inicializa el controlador de productos."""
        pass
    
    # ==========================================================================
    # OPERACIONES DE LECTURA
    # ==========================================================================
    
    def get_products(self):
        """
        Obtiene todos los productos con sus relaciones (categorías y unidades).
        
        Returns:
            list: Lista de productos con información completa
        """
        return product_model.get_products()
    
    def get_product_by_id(self, id_prod):
        """
        Obtiene un producto específico por su ID.
        
        Args:
            id_prod (int): ID del producto a buscar
            
        Returns:
            tuple: Información completa del producto o None si no existe
        """
        return product_model.get_product_by_id(id_prod)
    
    def get_products_by_provider(self, provider_id):
        """
        Obtiene todos los productos asociados a un proveedor específico.
        
        Args:
            provider_id (int): ID del proveedor
            
        Returns:
            list: Lista de productos del proveedor con precios de compra
        """
        return product_model.get_products_by_provider(provider_id)
    
    def get_product_suppliers(self, id_prod):
        """
        Obtiene todos los proveedores asociados a un producto específico.
        
        Args:
            id_prod (int): ID del producto
            
        Returns:
            list: Lista de proveedores del producto con precios de compra
        """
        return product_model.get_product_suppliers(id_prod)
    
    # ==========================================================================
    # OPERACIONES DE CREACIÓN
    # ==========================================================================
    
    def create_product(self, name, description, location, price, category_id, unit_id):
        """
        Crea un nuevo producto en la base de datos.
        
        Args:
            name (str): Nombre del producto
            description (str): Descripción del producto
            location (str): Ubicación física del producto
            price (float): Precio unitario del producto
            category_id (int): ID de la categoría del producto
            unit_id (int): ID de la unidad de medida
            
        Returns:
            bool: True si el producto fue creado exitosamente
        """
        return product_model.create_product(name, description, location, price, category_id, unit_id)
    
    def assign_supplier_to_product(self, id_prod, id_prov, precio_compra):
        """
        Asigna un proveedor a un producto con un precio de compra específico.
        
        Args:
            id_prod (int): ID del producto
            id_prov (int): ID del proveedor
            precio_compra (float): Precio de compra del producto al proveedor
            
        Returns:
            bool: True si la asignación fue exitosa
        """
        return product_model.assign_supplier_to_product(id_prod, id_prov, precio_compra)
    
    # ==========================================================================
    # OPERACIONES DE ACTUALIZACIÓN
    # ==========================================================================
    
    def update_product(self, id_prod, nombre, descripcion, ubicacion, precio, id_categoria, id_unidad):
        """
        Actualiza la información de un producto existente.
        
        Args:
            id_prod (int): ID del producto a actualizar
            nombre (str): Nuevo nombre del producto
            descripcion (str): Nueva descripción del producto
            ubicacion (str): Nueva ubicación del producto
            precio (float): Nuevo precio unitario
            id_categoria (int): ID de la nueva categoría
            id_unidad (int): ID de la nueva unidad de medida
            
        Returns:
            bool: True si la actualización fue exitosa
        """
        return product_model.update_product(id_prod, nombre, descripcion, ubicacion, precio, id_categoria, id_unidad)

    # ==========================================================================
    # PROVISIONALES
    # ==========================================================================
    
    def get_porduct_categories(self):
        return product_model.get_categories()
    
    def get_units(self):
        return product_model.get_units()
    
    def get_suppliers(self):
        return product_model.get_suppliers()
    
    def assign_supplier_to_product(self, product_id, provider_id, purchase_price):
        product_model.assign_supplier_to_product(product_id, provider_id, purchase_price)
        