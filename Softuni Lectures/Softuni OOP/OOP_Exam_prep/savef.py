def produce_item(self, product_type: str, model: str, price: float):
    # if product_type == "Chair":
    #     product = Chair(model, price)
    # elif product_type == "HobbyHorse":
    #     product = HobbyHorse(model, price)
    # else:
    #     raise Exception("Invalid product type!")
    if self.VALID_PRODUCTS.get(product_type):
        product = self.VALID_PRODUCTS[product_type](model, price)
        self.products.append(product)
        return f"A product of sub-type {product.sub_type} was produced."
    raise Exception("Invalid product type!")

    # self.products.append(product)
    # return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        # if store_type == "FurnitureStore":
        #     store = FurnitureStore(name, location)
        # elif store_type == "ToyStore":
        #     store = ToyStore(name, location)
        # else:
        #     raise Exception(f"{store_type} is an invalid type of store!")
        #
        # self.stores.append(store)
        # return f"A new {store_type} was successfully registered."
        if self.VALID_FURNITURE.get(store_type):
            store = self.VALID_FURNITURE[store_type](name, location)
            self.stores.append(store)
            return f"A new {store_type} was successfully registered."
        raise Exception(f"{store_type} is an invalid type of store!")

        if len(value).strip() != 3 or " " in value:
            matching_products = [p for p in products if p.sub_type == store.store_type[:-5]]