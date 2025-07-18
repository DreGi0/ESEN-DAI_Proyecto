from Model import provider_model


class ProviderController:
    """
    Controlador para manejar todas las operaciones relacionadas con proveedores.
    """
    
    def __init__(self):
        """Inicializa el controlador de proveedores."""
        pass
    
    # ==========================================================================
    # OPERACIONES DE LECTURA
    # ==========================================================================
    
    def get_providers(self):
        """
        Obtiene todos los proveedores registrados.
        
        Returns:
            list: Lista de todos los proveedores
        """
        return provider_model.get_providers()
    
    def load_provider(self):
        """
        Carga la información de un proveedor específico.
        
        Returns:
            dict: Información del proveedor cargado
        """
        return provider_model.load_provider()
    
    # ==========================================================================
    # OPERACIONES DE CREACIÓN
    # ==========================================================================
    
    def create_provider(self, nombre_prov, apellido_prov):
        """
        Crea un nuevo proveedor en la base de datos.
        
        Args:
            nombre_prov (str): Nombre del proveedor
            apellido_prov (str): Apellido del proveedor
            
        Returns:
            bool: True si el proveedor fue creado exitosamente
        """
        return provider_model.create_provider(nombre_prov, apellido_prov)
    
    # ==========================================================================
    # OPERACIONES DE ACTUALIZACIÓN
    # ==========================================================================
    
    def update_provider(self, id_prov, nombre_prov, apellido_prov):
        """
        Actualiza la información de un proveedor existente.
        
        Args:
            id_prov (int): ID del proveedor a actualizar
            nombre_prov (str): Nuevo nombre del proveedor
            apellido_prov (str): Nuevo apellido del proveedor
            
        Returns:
            bool: True si la actualización fue exitosa
        """
        return provider_model.update_provider(id_prov, nombre_prov, apellido_prov)
    
    # ==========================================================================
    # OPERACIONES DE ELIMINACIÓN
    # ==========================================================================
    
    def remove_provider(self, id_prov):
        """
        Elimina un proveedor de la base de datos.
        
        Args:
            id_prov (int): ID del proveedor a eliminar
            
        Returns:
            bool: True si la eliminación fue exitosa
        """
        return provider_model.del_provider(id_prov)

