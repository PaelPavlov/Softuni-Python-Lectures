from project.stores.base_store import BaseStore


class ToyStore(BaseStore):
    CAPACITY = 100

    def __init__(self, name: str, location: str):
        super().__init__(name, location, self.CAPACITY)

    @property
    def store_type(self):
        return "ToyStore"

    def store_stats(self):
        product_stats = {}
        for product in self.products:
            if product.model in product_stats:
                product_stats[product.model]['count'] += 1
                product_stats[product.model]['total_price'] += product.price
            else:
                product_stats[product.model] = {'count': 1, 'total_price': product.price}

        stats = [f"{model}: {count['count']}pcs, average price: {count['total_price'] / count['count']:.2f}"
                 for model, count in sorted(product_stats.items())]

        profit_str = self.get_estimated_profit()
        return (f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}\n"
                f"{profit_str}\n**Toys for sale:" + "\n".join(stats))
