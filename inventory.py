class Inventory:
    def __init__(self):
        self.items={}
    
    def add_item(self, item_name, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        
        if item_name in self.items:
            self.items[item_name] += quantity

        else:
            self.items[item_name] = quantity

    
    def remove_item(self, item_name, quantity):
        if item_name not in self.items:
            raise ValueError("Item not found in inventory")
        
        if quantity > self.items[item_name]:
            raise ValueError("Not enough quantity in inventory")
        
        self.items[item_name] -= quantity
        if self.items[item_name] == 0:
            del self.items[item_name]
    
    def get_inventory(self):
        return self.items