class Game:
    def __init__(self):
        self.items_collected = 0
        self.inventory = []

    def collect_item(self, item):
        """Collect an item and add it to the inventory."""
        self.inventory.append(item)
        self.items_collected += 1
        print(f"Collected: {item}")

    def recycle_item(self, item):
        """Recycle an item if it's in the inventory."""
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"Recycled: {item}")
        else:
            print("Item not found in inventory.")

    def update(self):
        """Placeholder for game logic updates (e.g., player movement)."""
        pass
