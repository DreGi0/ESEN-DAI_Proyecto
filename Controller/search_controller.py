from Model.search_model import filtered_products
from Model.search_model import filtered_products, get_categories

class SearchController:
    def search_products(self, name, category, location):
        return filtered_products(name=name, category_id=category, location=location)

    def get_categories(self):
        return get_categories()
    