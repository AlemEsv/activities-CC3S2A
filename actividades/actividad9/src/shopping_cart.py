# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, nombre, cantidad, precio):
        if nombre in self.items:
            self.items[nombre]["cantidad"] += cantidad
        else:
            self.items[nombre] = {"cantidad": cantidad, "precio": precio}

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def calculate_total(self):
        return sum(item["cantidad"] * item["precio"] for item in self.items.values())