# test_shopping_cart.py

import pytest
from src.shopping_cart import ShoppingCart
from unittest.mock import Mock

def test_add_item():
    cart = ShoppingCart()
    cart.add_item("manzana", 2, 0.5)  # nombre, cantidad, precio unitario
    assert cart.items == {"manzana": {"cantidad": 2, "precio": 0.5}}

def test_remove_item():
    cart = ShoppingCart()
    cart.add_item("manzana", 2, 0.5)
    cart.remove_item("manzana")
    assert cart.items == {}

def test_calculate_total():
    cart = ShoppingCart()
    cart.add_item("apple", 2, 0.5)
    cart.add_item("banana", 3, 0.75)
    total = cart.calculate_total()
    assert total == 2*0.5 + 3*0.75  # 2*0.5 + 3*0.75 = 1 + 2.25 = 3.25

def test_apply_discount():
    cart = ShoppingCart()
    cart.add_item("apple", 2, 0.5)
    cart.add_item("banana", 3, 0.75)
    cart.apply_discount(10)  # Descuento del 10%
    total = cart.calculate_total()
    expected_total = (2*0.5 + 3*0.75) * 0.9  # Aplicando 10% de descuento
    assert total == round(expected_total, 2)  # Redondear a 2 decimales

def test_process_payment():
    payment_gateway = Mock()
    payment_gateway.process_payment.return_value = True
    
    cart = ShoppingCart(payment_gateway=payment_gateway)
    cart.add_item("manzana", 2, 0.5)
    cart.add_item("platano", 3, 0.75)
    cart.apply_discount(10)
    
    total = cart.calculate_total()
    result = cart.process_payment(total)
    
    payment_gateway.process_payment.assert_called_once_with(total)
    assert result == True