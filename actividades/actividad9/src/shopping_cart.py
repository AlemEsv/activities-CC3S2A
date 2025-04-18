# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.items = {}
        self.discount = 0
    
    def add_item(self, nombre, cantidad, precio):
        if nombre in self.items:
            self.items[nombre]["cantidad"] += cantidad
        else:
            self.items[nombre] = {"cantidad": cantidad, "precio": precio}

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def calculate_total(self):
        total = sum(item["cantidad"] * item["precio"] for item in self.items.values())
        if self.discount > 0:
            total *= (1 - self.discount / 100)
        return round(total,2)

    def apply_discount(self, discount_percentage):
        if 0 <= discount_percentage <= 100:
            self.discount = discount_percentage    
        else:
            raise ValueError("El porcentaje de descuento debe estar entre 1 y 100")

