class Game:
    def __init__(self):
        self.items_collected = 0
        self.inventory = []

    def collect_item(self, item):
        """Collect an item and add it to the inventory."""
        self.inventory.append(item)
        self.items_collected += 1
    
    def recycle_item(self, item):
    if item in self.inventory:
        self.inventory.remove(item)
        print(f"Recycled: {item}")

    def view_inventory(self):
    return self.inventory
    
    def craft_item(self, item_1, item_2):
    if item_1 in self.inventory and item_2 in self.inventory:
        crafted_item = f"{item_1} + {item_2}"
        print(f"Crafted: {crafted_item}")
        return crafted_item


