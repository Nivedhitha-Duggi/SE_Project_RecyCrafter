class Game:
    def __init__(self):
        self.items_collected = 0
        self.inventory = []

    def collect_item(self, item):
        self.inventory.append(item)
        self.items_collected += 1
        print(f"Collected: {item}")

    def recycle_item(self, item):
            if item in self.inventory:
            self.inventory.remove(item)
            print(f"Recycled: {item}")
        else:
            print(f"Cannot recycle: {item} not found in inventory.")

    def view_inventory(self):
         return self.inventory

    def craft_item(self, item_1, item_2):
        if item_1 in self.inventory and item_2 in self.inventory:
            crafted_item = f"{item_1} + {item_2}"
            self.inventory.remove(item_1)
            self.inventory.remove(item_2)
            self.inventory.append(crafted_item)
            print(f"Crafted: {crafted_item}")
            return crafted_item
        else:
            print(f"Cannot craft: {item_1} or {item_2} not in inventory.")
            return None
