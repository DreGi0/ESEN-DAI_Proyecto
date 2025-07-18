from Model import client_model

class ClientController:
    def __init__(self):
        pass
    
    #CREATE
    def create_cliente(self, nombre_cliente, apellido_cliente):
        return client_model.create_cliente(nombre_cliente, apellido_cliente)
    
    #READ
    def load_cliente(self):
        return client_model.load_cliente()
    
    # UPDATE
    def update_cliente(self, id_cliente, nombre_cliente, apellido_cliente):
        return client_model.update_cliente(id_cliente, nombre_cliente, apellido_cliente)

    # DELETE
    def del_cliente(self, id_cliente):
        return client_model.del_cliente(id_cliente)
    
    # get clientes
    def get_all_clientes(self):
        return client_model.get_all_clientes()