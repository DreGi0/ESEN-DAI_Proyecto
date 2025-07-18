from Model import provider_model

class ProviderController:
    def __init__(self):
        pass
    
    #CREATE
    def create_provider(self, nombre_prov, apellido_prov):
        return provider_model.create_provider(nombre_prov, apellido_prov)
    
    #READ
    def load_provider(self):
        return provider_model.load_provider()
    
    # UPDATE
    def update_provider(self, id_prov, nombre_prov, apellido_prov):
        return provider_model.update_provider(id_prov, nombre_prov, apellido_prov)

    # DELETE
    def del_provider(self, id_prov):
        return provider_model.del_provider(id_prov)
    
    # get providers
    def get_all_providers(self):
        return provider_model.get_all_providers()