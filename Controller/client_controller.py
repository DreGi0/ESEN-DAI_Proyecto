from Model import client_model

class ClientController:
    def __init__(self):
        self.clients = []
    
    def get_clients(self):
        return client_model.get_all_clients()
    
    def save_client(self, nombre_cliente, apellido_cliente, correo):
        return client_model.create_client(
            nombre_cliente, apellido_cliente, correo)

    def reset_client(self):
        self.clients = []