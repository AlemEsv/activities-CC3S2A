# shopping_cart.py

class ShoppingCart:
    def __init__(self, payment_gateway=None):
        self.items = {}
        self.discount = 0
        self.payment_gateway = payment_gateway
    
    def add_item(self, nombre, cantidad, precio):
        if nombre in self.items:
            self.items[nombre]["cantidad"] += cantidad
        else:
            self.items[nombre] = {"cantidad": cantidad, "precio": precio}
    
    def remove_item(self, nombre):
        if nombre in self.items:
            del self.items[nombre]

    def calculate_total(self):
        total = sum(item["cantidad"] * item["precio"] for item in self.items.values())
        if self.discount > 0:
            total *= (1 - self.discount / 100)
        return round(total, 2)  # Redondear a 2 decimales
    
    def apply_discount(self, discount_percentage):
        if 0 <= discount_percentage <= 100:
            self.discount = discount_percentage
        else:
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")

    def process_payment(self, cantidad):
        if not self.payment_gateway:
            raise ValueError("No se ha configurado un método de pago.")
        try:
            success = self.payment_gateway.process_payment(cantidad)
            return success
        except Exception as e:
            # Manejo de excepciones
            raise e