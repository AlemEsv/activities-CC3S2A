# test_shopping_cart.py
import pytest
from src.shopping_cart import ShoppingCart

def test_add_item():
    cart = ShoppingCart()
    cart.add_item("Manzana", 2, 0.5)  # nombre, cantidad, precio unitario
    assert cart.items == {"Manzana": {"cantidad": 2, "precio": 0.5}}

def test_remove_item():
    cart = ShoppingCart()
    cart.add_item("manzana", 2, 0.5)
    cart.remove_item("manzana")
    assert cart.items == {}

def test_calculate_total():
    cart = ShoppingCart()
    cart.add_item("manzana", 2, 0.5)
    cart.add_item("platano", 3, 0.75)
    total = cart.calculate_total()
    assert total == 2*0.5 + 3*0.75  # 2*0.5 + 3*0.75 = 1 + 2.25 = 3.25
