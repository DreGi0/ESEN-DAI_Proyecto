from Model import client_model


class ClientController:
    """
    Controlador para manejar todas las operaciones relacionadas con clientes.
    """
    
    def __init__(self):
        """Inicializa el controlador de clientes."""
        pass
    
    # ==========================================================================
    # OPERACIONES DE LECTURA
    # ==========================================================================
    
    def get_clients(self):
        """
        Obtiene todos los clientes de la base de datos.
        
        Returns:
            list: Lista de todos los clientes registrados
        """
        return client_model.get_clients()
    
    def load_client(self):
        """
        Devuelve todos los clientes (como lista de tuplas)
        """
        return client_model.get_clients()

    def get_all_clientes(self):
        """
        Alias para compatibilidad con la vista
        """
        return client_model.get_clients()
    
    # ==========================================================================
    # OPERACIONES DE CREACIÓN
    # ==========================================================================
    
    def create_client(self, nombre_cliente, apellido_cliente):
        """
        Crea un nuevo cliente en la base de datos.
        
        Args:
            nombre_cliente (str): Nombre del cliente
            apellido_cliente (str): Apellido del cliente
            
        Returns:
            bool: True si el cliente fue creado exitosamente
        """
        return client_model.create_client(nombre_cliente, apellido_cliente)
    
    # ==========================================================================
    # OPERACIONES DE ACTUALIZACIÓN
    # ==========================================================================
    
    def update_client(self, id_cliente, nombre_cliente, apellido_cliente):
        """
        Actualiza la información de un cliente existente.
        
        Args:
            id_cliente (int): ID del cliente a actualizar
            nombre_cliente (str): Nuevo nombre del cliente
            apellido_cliente (str): Nuevo apellido del cliente
            
        Returns:
            bool: True si la actualización fue exitosa
        """
        return client_model.update_client(id_cliente, nombre_cliente, apellido_cliente)
    
    # ==========================================================================
    # OPERACIONES DE ELIMINACIÓN
    # ==========================================================================
    
    def remove_client(self, id_cliente):
        """
        Elimina un cliente de la base de datos.
        
        Args:
            id_cliente (int): ID del cliente a eliminar
            
        Returns:
            bool: True si la eliminación fue exitosa
        """
        return client_model.delete_client(id_cliente)
