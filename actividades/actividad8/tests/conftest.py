import pytest
from src.carrito import Carrito
from src.factories import ProductoFactory

@pytest.fixture
def carrito():
    return Carrito()

@pytest.fixture
def producto_generico():
    return ProductoFactory(nombre="Pelota", precio=100.0, stock=5)

@pytest.fixture
def producto_generico_2():
    return ProductoFactory(nombre="Caja", precio=120.0, stock=10)

@pytest.fixture
def producto_generico_3():
    return ProductoFactory(nombre="Botella", precio=320.0, stock=30)

@pytest.fixture
def producto_generico_4():
    return ProductoFactory(nombre="Camisa", precio=10.0, stock=2)

