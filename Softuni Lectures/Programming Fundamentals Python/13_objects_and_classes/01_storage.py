class Storage:
    storage = []
 
    def __init__(self, capacity):
        self.capacity = capacity
 
    def add_product(self, product: str):
        if self.capacity > len(Storage.storage):
            Storage.storage.append(product)
 
    def get_products(self):
        return Storage.storage