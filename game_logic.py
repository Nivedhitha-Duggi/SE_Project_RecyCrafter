class ItemCollection:
    def __init__(self):
        self.collected_items = []

    def collect_item(self, item):
        """Collect item and add to the inventory"""
        self.collected_items.append(item)
        print(f"Collected: {item}")

    def show_inventory(self):
        """Display collected items"""
        return self.collected_items
