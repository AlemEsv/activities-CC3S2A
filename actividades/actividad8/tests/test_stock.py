# tests/test_stock.py
import pytest
from src.carrito import Carrito, Producto


def test_agregar_producto_excede_stock(carrito, producto_generico):
    """
    Red: Se espera que al intentar agregar una cantidad mayor a la disponible en stock se lance un ValueError.
    """
    # Arrange
    # Suponemos que el producto tiene 5 unidades en stock.

    # Act & Assert
    with pytest.raises(ValueError):
        carrito.agregar_producto(producto_generico, cantidad=6)