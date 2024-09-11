from typing import List

from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:
    VALID_PRODUCTS = {"Chair": Chair,
                      "HobbyHorse": HobbyHorse

                      }
    VALID_FURNITURE = {"FurnitureStore": FurnitureStore,
                       "ToyStore": ToyStore

                       }

    def __init__(self, name: str):
        self.name = name
        self.income = 0.0
        self.products: List[BaseProduct] = []
        self.stores: List[BaseStore] = []

    def produce_item(self, product_type: str, model: str, price: float):
        if self.VALID_PRODUCTS.get(product_type):
            product = self.VALID_PRODUCTS[product_type](model, price)
            self.products.append(product)
            return f"A product of sub-type {product.sub_type} was produced."
        raise Exception("Invalid product type!")

    def register_new_store(self, store_type: str, name: str, location: str):
        if self.VALID_FURNITURE.get(store_type):
            store = self.VALID_FURNITURE[store_type](name, location)
            self.stores.append(store)
            return f"A new {store_type} was successfully registered."
        raise Exception(f"{store_type} is an invalid type of store!")

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if len(products) > store.capacity:
            return f"Store {store.name} has no capacity for this purchase."

        matching_products = [p for p in products if p.sub_type == store.store_type[:-5]]

        if not matching_products:
            return "Products do not match in type. Nothing sold."

        for product in matching_products:
            self.products.remove(product)
            store.products.append(product)

        store.capacity -= len(matching_products)
        self.income += sum(product.price for product in matching_products)

        return f"Store {store.name} successfully purchased {len(matching_products)} items."

    def unregister_store(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)
        if not store:
            raise Exception("No such store!")

        if store.products:
            return "The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store)
        return f"Successfully unregistered store {store.name}, location: {store.location}."

    def discount_products(self, product_model: str):
        matching_products = [p for p in self.products if p.model == product_model]

        for product in matching_products:
            product.discount()

        return f"Discount applied to {len(matching_products)} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)
        if not store:
            return "There is no store registered under this name!"

        return store.store_stats()

    def statistics(self):
        total_products_price = sum(p.price for p in self.products)
        unsold_products_count = len(self.products)
        product_breakdown = {}

        for product in self.products:
            if product.model in product_breakdown:
                product_breakdown[product.model] += 1
            else:
                product_breakdown[product.model] = 1

        product_breakdown_str = "\n".join(
            [f"{model}: {count}" for model, count in sorted(product_breakdown.items())]
        )

        store_names = "\n".join(sorted(store.name for store in self.stores))

        return (f"Factory: {self.name}\nIncome: {self.income:.2f}\n"
                f"***Products Statistics***\n"
                f"Unsold Products: {unsold_products_count}. Total net price: {total_products_price:.2f}\n"
                f"{product_breakdown_str}\n"
                f"***Partner Stores: {len(self.stores)}***\n"
                f"{store_names}")
