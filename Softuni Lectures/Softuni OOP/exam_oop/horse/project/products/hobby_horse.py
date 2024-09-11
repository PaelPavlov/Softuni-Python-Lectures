from project.products.base_product import BaseProduct


class HobbyHorse(BaseProduct):
    MATERIAL = "Wood/Plastic"
    SUB_TYPE = "Toys"

    def __init__(self, model: str, price: float):
        super().__init__(model, price, self.MATERIAL, self.SUB_TYPE)

    def discount(self):
        self.price *= 0.80

