class Inventory:
    items = []
    def __init__(self, capacity: int):
        self.__capacity = capacity
        #self.items = []
    def add_item(self, item: str):
        if self.__capacity > len(self.items):
            Inventory.items.append(item)
        return f"not enough room in the inventory"
    
    def get_capacity(self):
        return self.__capacity
    
    def __repr__(self):
        capacity_left = self.__capacity - len(self.items)
        items_list = ", ".join(self.items)
        return f'Items: {items_list}.\nCapacity left: {capacity_left}'
    
inventory = Inventory(5)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)