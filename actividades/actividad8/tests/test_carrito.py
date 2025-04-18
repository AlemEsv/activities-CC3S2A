# tests/test_carrito.py

import pytest
from src.carrito import Carrito
from src.factories import ProductoFactory

def test_agregar_producto_nuevo(carrito, producto_generico):
    """
    AAA:
    Arrange: Se crea un carrito y se genera un producto.
    Act: Se agrega el producto al carrito.
    Assert: Se verifica que el carrito contiene un item con el producto y cantidad 1.
    """
    
    # Act
    carrito.agregar_producto(producto_generico,cantidad=1)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].producto.nombre == producto_generico.nombre
    assert items[0].cantidad == 1


def test_agregar_producto_existente_incrementa_cantidad(carrito,producto_generico):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se agrega el mismo producto nuevamente aumentando la cantidad.
    Assert: Se verifica que la cantidad del producto se incrementa en el item.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=1)
    
    # Act
    carrito.agregar_producto(producto_generico, cantidad=2)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 3


def test_remover_producto(carrito,producto_generico):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto con cantidad 3.
    Act: Se remueve una unidad del producto.
    Assert: Se verifica que la cantidad del producto se reduce a 2.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=3)
    
    # Act
    carrito.remover_producto(producto_generico, cantidad=1)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 2


def test_remover_producto_completo(carrito,producto_generico):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se remueve la totalidad de la cantidad del producto.
    Assert: Se verifica que el producto es eliminado del carrito.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=2)
    
    # Act
    carrito.remover_producto(producto_generico, cantidad=2)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 0


def test_actualizar_cantidad_producto(carrito,producto_generico):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se actualiza la cantidad del producto a 5.
    Assert: Se verifica que la cantidad se actualiza correctamente.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=1)
    
    # Act
    carrito.actualizar_cantidad(producto_generico, nueva_cantidad=5)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 1
    assert items[0].cantidad == 5


def test_actualizar_cantidad_a_cero_remueve_producto(carrito,producto_generico):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se actualiza la cantidad del producto a 0.
    Assert: Se verifica que el producto se elimina del carrito.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=3)
    
    # Act
    carrito.actualizar_cantidad(producto_generico, nueva_cantidad=0)
    
    # Assert
    items = carrito.obtener_items()
    assert len(items) == 0


def test_calcular_total(carrito, producto_generico, producto_generico_2):
    """
    AAA:
    Arrange: Se crea un carrito y se agregan varios productos con distintas cantidades.
    Act: Se calcula el total del carrito.
    Assert: Se verifica que el total es la suma correcta de cada item (precio * cantidad).
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=2)  # Total 200
    carrito.agregar_producto(producto_generico_2, cantidad=1)  # Total 120
    
    # Act
    total = carrito.calcular_total()
    
    # Assert
    assert total == 320.00


def test_aplicar_descuento(carrito, producto_generico):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto con una cantidad determinada.
    Act: Se aplica un descuento del 10% al total.
    Assert: Se verifica que el total con descuento sea el correcto.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=2)  # Total 200
    
    # Act
    total_con_descuento = carrito.aplicar_descuento(10)
    
    # Assert
    assert total_con_descuento == 180.00


def test_aplicar_descuento_limites(carrito,producto_generico):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act y Assert: Se verifica que aplicar un descuento fuera del rango [0, 100] genere un error.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=1)
    
    # Act y Assert
    with pytest.raises(ValueError):
        carrito.aplicar_descuento(150)
    with pytest.raises(ValueError):
        carrito.aplicar_descuento(-5)

def test_carrito_vacio(carrito, producto_generico,producto_generico_2):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega 2 productos.
    Act: Se eliminan todos los productos.
    Assert: Se verifica que el carrito esté vacip
    """
    # Arrange
    carrito.agregar_producto(producto_generico,cantidad=1)
    carrito.agregar_producto(producto_generico_2,cantidad=1)
        
    # Act
    carrito.vaciar()

    # Assert
    assert carrito.obtener_items() == []

def test_costo_de_productos_nulo(carrito, producto_generico, producto_generico_2):
    """
    AAA:
    Arrange: Se crea un carrito y se le agrega 2 productos.
    Act: Se vacía el carrito.
    Assert: Se verifica si el carrito sin items retornará un total igual a 0.
    """
    # Arrange
    carrito.agregar_producto(producto_generico,cantidad=1)
    carrito.agregar_producto(producto_generico_2,cantidad=1)

    # Act
    carrito.vaciar()

    # Assert
    assert carrito.calcular_total() == 0

def test_aplicar_descuento_condicional(carrito,producto_generico,producto_generico_2):
    """
    AAA:
    Arrange: Crear un carrito y agregarle 2 productos.
    Act y Assert: Verificar si se aplica el descuento condicional.
    """
    # Arrange
    carrito.agregar_producto(producto_generico,cantidad=1)
    carrito.agregar_producto(producto_generico_2,cantidad=1)
    # Act y Assert
    assert carrito.aplicar_descuento_condicional(20,100) == (220*0.8)
    assert carrito.aplicar_descuento_condicional(20,500) == 220


def test_agregar_productos_dentro_del_stock(carrito, producto_generico):
    """
    AAA:
    Arrange: Crear un carrito y agregar un producto.
    Act: actualizar la cantidad del producto agregado sin que pase el stock 
    Assert: Verificar sino se agota el stock del producto. 
    """

    # Arrange
    carrito.agregar_producto(producto_generico,cantidad=1)
    
    # Act
    carrito.actualizar_cantidad(producto_generico,4)

    # Assert
    assert producto_generico.stock < 5

def test_items_ordenados_por_nombre(carrito, 
    producto_generico,producto_generico_2,producto_generico_3,producto_generico_4):
    """
    AAA:
    Arrange: Crear un carrito y agregar varios productos.
    Act: ordenar la lista de productos que están en el carrito
    Assert: Verificar si la lista está ordenada alfabéticamente.
    """

    # Arrange
    carrito.agregar_producto(producto_generico,cantidad=1)
    carrito.agregar_producto(producto_generico_2,cantidad=1)
    carrito.agregar_producto(producto_generico_3,cantidad=1)
    carrito.agregar_producto(producto_generico_4,cantidad=1)
    # Act
    items_ordenados = carrito.obtener_items_ordenados("nombre")
    verificar_orden = [item.producto.nombre for item in items_ordenados] # lista de nombres ordenados
    # Assert
    assert verificar_orden == sorted(verificar_orden)

def test_items_ordenados_por_precio(carrito, 
    producto_generico,producto_generico_2,producto_generico_3,producto_generico_4):
    """
    AAA:
    Arrange: Crear un carrito y agregar varios productos.
    Act: ordenar la lista de productos que están en el carrito
    Assert: Verificar si la lista está ordenada de más barato a más caro.
    """

    # Arrange
    carrito.agregar_producto(producto_generico,cantidad=1)
    carrito.agregar_producto(producto_generico_2,cantidad=1)
    carrito.agregar_producto(producto_generico_3,cantidad=1)
    carrito.agregar_producto(producto_generico_4,cantidad=1)

    # Act
    items_ordenados = carrito.obtener_items_ordenados("precio")
    verificar_orden = [item.producto.precio for item in items_ordenados] # lista de precios ordenados
    # Assert
    assert verificar_orden == sorted(verificar_orden)

