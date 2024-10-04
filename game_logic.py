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
    def view_inventory(self):
    return self.inventory

