# El patrón Arrange-Act-Assert

Las pruebas unitarias no son nada misteriosas. Son solo código ejecutable escrito en el mismo lenguaje que la aplicación. Cada prueba de unidad constituye el primer uso del código que se desea escribir. Se llama al código tal como se llamará en la aplicación real.
La prueba ejecuta ese código, captura los resultados que nos interesan y verifica que sean lo que esperábamos. Dado que la prueba usa el código de la misma manera que la aplicación, recibimos comentarios inmediatos sobre qué tan fácil o difícil es usarlo. Esto puede sonar obvio, y lo es, pero es una herramienta poderosa para escribir código limpio y correcto.

## Objetivos de aprendizaje

- Aplicar el patrón **Arrange-Act-Assert (AAA)** para estructurar pruebas unitarias claras y legibles.
- Escribir pruebas efectivas usando **Pytest**, utilizando buenas prácticas como una sola aserción por prueba.
- Comprender y aplicar los principios **FIRST** para mejorar la calidad de las pruebas.

# Ejercicios

## Ejercicio 1: Método para vaciar el carrito

**Objetivo:**  
Implementa en la clase `Carrito` un método llamado `vaciar()` que elimine todos los items del carrito. Luego, escribe pruebas siguiendo el patrón AAA para verificar que, al vaciar el carrito, la lista de items quede vacía y el total sea 0.
**Pistas:**

- Agrega el método `vaciar` en `src/carrito.py` que realice `self.items = []`.
- Crea pruebas en `tests/test_carrito.py` que agreguen varios productos, invoquen `vaciar()` y verifiquen que `obtener_items()` retorne una lista vacía y `calcular_total()` retorne 0.

#### Creación del método *vaciar()*

```python
class Carrito:
  # (...)
  def vaciar(self):
    """
    Elimina todos los items del carrito.
    """
    self.items.clear()
```

### Prueba #1: verificar si el carrito está vacío

```python
  def test_carrito_vacio():
    """
    AAA:
    Arrange: Se crea un carrito y se agregan 2 productos.
    Act: Se eliminan todos los productos.
    Assert: Se verifica que el carrito esté vacio
    """
    # Arrange
    carrito = Carrito()
    producto1 = ProductoFactory(nombre="Laptop", precio=1200.00)
    producto2 = ProductoFactory(nombre="Teclado", precio=100.00)
    carrito.agregar_producto(producto1,cantidad=1)
    carrito.agregar_producto(producto2,cantidad=1)

    # Act
    carrito.vaciar()

    # Assert
    assert carrito.obtener_items() == []
```

![](img/prueba1.png)

### Prueba #2: verificar si el carrito vacío no retorna un total de elementos

```python
  def test_carrito_vacio():
    """
    AAA:
    Arrange: Se crea un carrito y se agregan 2 productos.
    Act: Se vacia el carrito.
    Assert: Se verifica que el carrito esté vacio
    """
    # Arrange
    carrito = Carrito()
    producto1 = ProductoFactory(nombre="Peine", precio=5.00)
    producto2 = ProductoFactory(nombre="Botella de agua", precio=2.50)
    carrito.agregar_producto(producto1,cantidad=1)
    carrito.agregar_producto(producto2,cantidad=1)

    # Act
    carrito.vaciar()

    # Assert
    assert carrito.calcular_total() == 0
```

![](img/prueba2.png)

## Ejercicio 2: Descuento por compra mínima

**Objetivo:**  
Amplía la lógica del carrito para aplicar un descuento solo si el total supera un monto determinado. Por ejemplo, si el total es mayor a \$500, se aplica un 15% de descuento.
**Pistas:**

- Agrega un nuevo método, por ejemplo, `aplicar_descuento_condicional(porcentaje, minimo)` en la clase `Carrito` que primero verifique si `calcular_total() >= minimo`.  
- Si se cumple la condición, aplica el descuento; de lo contrario, retorna el total sin descuento.
- Escribe pruebas para ambos escenarios (condición cumplida y no cumplida).

#### Creación de la función *aplicar_descuento_condicional()*

```python
def aplicar_descuento_condicional(self,porcentaje,minimo):
  """
  Aplicar descuento condicional a una cantidad mínima.
  El porcentaje debe estar entre 0 y 100.
  """
  if self.calcular_total() >= minimo:
    return self.aplicar_descuento(porcentaje)
  else:
    return self.calcular_total()
```

### Prueba #1: Verificar si el descuento condicional se cumple

![](img/img4.png)

### Prueba #2: Verificiar si el descuento condicional no se cumple

![](img/img5.png)

## Ejercicio 3: Manejo de stock en producto

**Objetivo:**  
Modifica la clase `Producto` para que incluya un atributo `stock` (cantidad disponible). Luego, actualiza el método `agregar_producto` en `Carrito` para que verifique que no se agregue una cantidad mayor a la disponible en stock. Si se intenta agregar más, se debe lanzar una excepción.
**Pistas:**

- Modifica `Producto` en `src/carrito.py` añadiendo `self.stock = stock` en el constructor y actualiza la fábrica en `src/factories.py` para que genere un stock (por ejemplo, entre 1 y 100).
- En `Carrito.agregar_producto`, antes de agregar o incrementar la cantidad, verifica que la suma de cantidades en el carrito no supere el `stock` del producto.
- Escribe pruebas que verifiquen:
  - Se puede agregar un producto dentro del límite de stock.
  - Se lanza una excepción al intentar agregar más unidades de las disponibles.

### Resolución

Modificación de la clase **Producto** para que reconozca un stock como atributo:

```python
class Producto:
  def __init__(self, nombre, precio, stock):
    self.nombre = nombre
    self.precio = precio
    self.stock = stock
  def __repr__(self):
    return f"Producto({self.nombre}, {self.precio}, {self.stock})"
```

Modificación de la clase **ProductoFactory** para que se pueda colocar un stock entre 1 y 100 unidades

```python
class ProductoFactory(factory.Factory):
  class Meta:
    model = Producto
  nombre = factory.Faker("word")
  precio = factory.Faker("pyfloat", left_digits=2, right_digits=2, positive=True)
  # Stock entre 1 y 100 unidades por producto
  stock = factory.Faker("pyint", min_value=1, max_value=100)
```

### Modificación de las clases que agreguen o quiten productos del carrito para que tomen en cuenta la existencia de un producto con stock

#### a. agregar_producto()

```python
    def agregar_producto(self, producto, cantidad=1):
        """
        Agrega un producto al carrito.
        Si el producto ya existe, incrementa la cantidad.
        """
        if producto.stock == 0:
            raise ValueError("No hay stock para este producto.")
        for item in self.items:
            if item.producto.nombre == producto.nombre:
              item.cantidad += cantidad
              producto.stock -= 1
              return
        self.items.append(ItemCarrito(producto, cantidad))
```

#### b. remover_producto()

```python
    def remover_producto(self, producto, cantidad=1):
        """
        Remueve una cantidad del producto del carrito.
        Si la cantidad llega a 0, elimina el item.
        """
        if producto.stock == 0:
            raise ValueError("No hay stock para este producto.")
        for item in self.items:
            if item.producto.nombre == producto.nombre:
                if item.cantidad > cantidad:
                    item.cantidad -= cantidad
                    producto.stock += 1
                elif item.cantidad == cantidad:
                    self.items.remove(item)
                else:
                    raise ValueError("Cantidad a remover es mayor que la cantidad en el carrito")
                return
        raise ValueError("Producto no encontrado en el carrito")
```

#### c. actualizar_cantidad()

```python
    def actualizar_cantidad(self, producto, nueva_cantidad):
        """
        Actualiza la cantidad de un producto en el carrito.
        Si la nueva cantidad es 0, elimina el item.
        """
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        if producto.stock < nueva_cantidad:
            raise ValueError("No hay stock suficiente.")
        for item in self.items:
            if item.producto.nombre == producto.nombre:
                if nueva_cantidad == 0:
                    self.items.remove(item)
                    producto.stock += 1
                else:
                    item.cantidad = nueva_cantidad
                    producto.stock -= nueva_cantidad
                return
        raise ValueError("Producto no encontrado en el carrito")
```

### Prueba #1: Validar si la cantidad del producto agregado está en el límite de stock

![](img/img13.png)

### Prueba #2: Lanzar excepción si se agregan más de la cuenta

![](img/img14.png)

## Ejercicio 4: Ordenar items del carrito

**Objetivo:**  
Agrega un método en `Carrito` que devuelva la lista de items ordenados por un criterio (por ejemplo, por precio unitario o por nombre del producto).
**Pistas:**

- Crea un método `obtener_items_ordenados(criterio: str)` donde `criterio` pueda ser `"precio"` o `"nombre"`.
- Utiliza la función `sorted()` con una función lambda para ordenar según el criterio.
- Escribe pruebas que verifiquen que, al agregar varios productos, la lista devuelta esté ordenada correctamente según el criterio solicitado.

### Se creó el método *obtener_items_ordenados()* usando el método sorted()

```python
    def obtener_items_ordenados(self, criterio: str):
        """
        Ordena los items de un carrito dependiendo del criterio puesto.
        Luego retorna la lista ordenada
        'precio' = ordena por precio (menor a mayor)
        'nombre' = ordena por nombre (A a Z)
        """
        if criterio == "precio":
            return sorted(self.items, key=lambda item: item.producto.precio)
        elif criterio == "nombre":
            return sorted(self.items, key=lambda item: item.producto.nombre)
        else:
            raise ValueError("Selecciona un criterio adecuado.")
```

### Prueba #1: Verificar si se ordena los productos por nombre

![](img/img15.png)

### Prueba #2: Verificar si se ordena los productos por precio

![](img/img16.png)

## Ejercicio 5: Uso de Pytest Fixtures

**Objetivo:**  
Refactoriza las pruebas para que utilicen **fixtures** de Pytest, de modo que se reutilicen instancias comunes de `Carrito` o de productos.
**Pistas:**

- En el archivo `tests/conftest.py`, crea una fixture para un carrito vacío.
- Actualiza las pruebas existentes para usar estas fixtures en lugar de instanciar los objetos directamente en cada test.

### Creación de fixtures para la refactorización de las pruebas

##### Para este caso se colocaron 4 productos por los casos de ordenamiento de objetos

```python
import pytest
from src.carrito import Carrito
from src.factories import ProductoFactory

@pytest.fixture
def carrito():
    return Carrito()
# Productos genericos para tener un mejor manejo de variables
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
```

### Refactorización

Esta refactorización ayuda a que el código del proyecto sea más legible, con menos lineas de código innecesarias.

- Refactorización de algunos `tests`

```python
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

def test_actualizar_cantidad_producto(carrito,producto_generico):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se actualiza la cantidad del producto.
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
# (. . .)
```

# Ejercicio 6: Pruebas parametrizadas

**Objetivo:**  
Utiliza la marca `@pytest.mark.parametrize` para crear pruebas que verifiquen múltiples escenarios de descuento o actualización de cantidades.
**Pistas:**

- Por ejemplo, parametriza pruebas para `aplicar_descuento` usando distintos porcentajes y totales esperados.
- De igual forma, para actualizar cantidades: prueba con diferentes valores (válidos e inválidos) y verifica que se lance la excepción en los casos correspondientes.

### Prueba #1: Parametrizando pruebas para el método *aplicar descuento*

```python
@pytest.mark.parametrize(
    "cantidad, porcentaje_descuento, total_esperado",
    [
        (2, 10, 180.00),  # 200 - 10% = 180
        (3, 20, 240.00),  # 300 - 20% = 240
        (1, 50, 50.00),   # 100 - 50% = 50
        (5, 0, 500.00),   # no hay descuento
        (4, 100, 0.00)    # total 0
    ]
)
def test_aplicar_descuento(carrito, producto_generico, cantidad, porcentaje_descuento, total_esperado):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto con una cantidad determinada.
    Act: Se aplica un descuento al total.
    Assert: Se verifica que el total con descuento sea el correcto.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=cantidad)
    
    # Act
    total_con_descuento = carrito.aplicar_descuento(porcentaje_descuento)
    
    # Assert
    assert total_con_descuento == total_esperado
```

![](img/prueba3.png)

## Prueba #2: Parametrizando pruebas para el método *actualizar cantidades*

```python
@pytest.mark.parametrize(
        "nueva_cantidad, excepcion",
        [(5, False),(0, False),(-1, True)]
)
def test_actualizar_cantidad_producto(carrito,producto_generico, nueva_cantidad, excepcion):
    """
    AAA:
    Arrange: Se crea un carrito y se agrega un producto.
    Act: Se actualiza la cantidad del producto.
    Assert: Se verifica que la cantidad se actualiza correctamente.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=1)
    
    # Act y Assert
    if excepcion:
        with pytest.raises(ValueError):
            carrito.actualizar_cantidad(producto_generico, nueva_cantidad)
    else:
        carrito.actualizar_cantidad(producto_generico,nueva_cantidad)
        items = carrito.obtener_items()
        if nueva_cantidad == 0:
            assert len(items) == 0
        else:
            assert items[0].cantidad == nueva_cantidad
```

![](img/prueba4.png)

# Ejercicio 7: Calcular impuestos en el carrito

**Objetivo:**  
Implementar un método `calcular_impuestos(porcentaje)` que retorne el valor del impuesto calculado sobre el total del carrito.

#### Red

Crea un nuevo archivo de pruebas (por ejemplo, `tests/test_impuestos.py`) y escribe una prueba que espere que, dado un carrito con un total de \$1000, al aplicar un 10% de impuestos se retorne \$100.

```python
def test_calcular_impuestos(carrito, producto_generico):
    """
    Red: Se espera que calcular_impuestos retorne el valor del impuesto.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=4)  # Total = 400

    # Act
    impuesto = carrito.calcular_impuestos(10)  # 10% de 400 = 40

    # Assert
    assert impuesto == 40.00
```

![](img/prueba5.png)

### Green

En `src/carrito.py`, añade el método de forma mínima para que la prueba pase

```python
def calcular_impuestos(self, porcentaje):
  total = self.calcular_total()
  return total * (porcentaje / 100)
```

![](img/prueba6.png)

### Refactor

- Agrega validaciones para que el porcentaje esté en un rango razonable (por ejemplo, entre 0 y 100).  
- Añade documentación al método.

```python
    def calcular_impuestos(self, porcentaje):
        """
            Calcula el valor de los impuestos basados en el porcentaje indicado.
    
        Args:
            porcentaje (float): Porcentaje de impuesto a aplicar (entre 0 y 100).
        
        Returns:
            float: Monto del impuesto.
        
        Raises:
            ValueError: Si el porcentaje no está entre 0 y 100.
    """
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje debe estar entre 0 y 100")
        total = self.calcular_total()
        return total * (porcentaje / 100)
```

![](img/prueba7.png)

# Ejercicio 8: Aplicar cupón de descuento con límite máximo

**Objetivo:**  
Implementar un método `aplicar_cupon(descuento_porcentaje, descuento_maximo)` que aplique un cupón de descuento al total del carrito, pero asegurándose de que el descuento no supere un valor máximo.

#### Red

Crea un archivo, por ejemplo, `tests/test_cupon.py` y escribe una prueba que verifique que, para un carrito con total \$400 y un cupón del 20% (lo que daría \$80), si el descuento máximo es \$50, el método retorne \$350.

```python
def test_aplicar_cupon_con_limite(carrito, producto_generico):
    """
    Red: Se espera que al aplicar un cupón, el descuento no supere el límite máximo.
    """
    # Arrange
    carrito.agregar_producto(producto_generico, cantidad=2)  # Total = 200

    # Act
    total_con_cupon = carrito.aplicar_cupon(20, 30)  # 20% de 200 = 40, pero límite es 30

    # Assert
    assert total_con_cupon == 170.00
```

![](img/prueba8.png)

### Green

En `src/carrito.py`, añade un método para aplicar el cupón de descuento de forma básica

```python
def aplicar_cupon(self, descuento_porcentaje, descuento_maximo):
  total = self.calcular_total()
  descuento_calculado = total * (descuento_porcentaje / 100)
  descuento_final = min(descuento_calculado, descuento_maximo)
  return total - descuento_final
```

![](img/prueba9.png)

### Refactorizar

- Agrega validaciones para que el porcentaje de descuento y el máximo sean valores positivos.
- Separa la lógica de cálculo y validación, y documenta el método.

```python
def aplicar_cupon(self, descuento_porcentaje, descuento_maximo):
        """
        Aplica un cupón de descuento al total del carrito, asegurando que el descuento no exceda el máximo permitido.
    
        Args:
            descuento_porcentaje (float): Porcentaje de descuento a aplicar.
            descuento_maximo (float): Valor máximo de descuento permitido.
    
        Returns:
            float: Total del carrito después de aplicar el cupón.
    
        Raises:
            ValueError: Si alguno de los valores es negativo.
        """
        if descuento_porcentaje < 0 or descuento_maximo < 0:
            raise ValueError("Los valores de descuento deben ser positivos.")
        total = self.calcular_total()
        descuento_calculado = total * (descuento_porcentaje / 100)
        descuento_final = min(descuento_calculado, descuento_maximo)
        return total - descuento_final
```

![](img/prueba10.png)

# Ejercicio 9: Validación de stock al agregar productos (RGR)

**Objetivo:**  
Asegurarse de que al agregar un producto al carrito, no se exceda la cantidad disponible en stock.  

#### Red

En un nuevo archivo, por ejemplo, `tests/test_stock.py`, escribe una prueba que verifique que si se intenta agregar más unidades de las disponibles, se lance una excepción.

```python
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
```

![](img/prueba11.png)

### Green

Modifica el método `agregar_producto` en `Carrito` para que valide el stock:

![](img/prueba12.png)

### Refactor

- Centraliza la validación del stock en un método privado o en la clase `Producto` si es necesario.
- Documenta la función y separa la lógica de búsqueda del producto en el carrito.

```python
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __repr__(self):
        return f"Producto({self.nombre}, {self.precio}, {self.stock})"
    
    def _buscar_item(self, producto):
        for item in self.items:
            if item.producto.nombre == producto.nombre:
                return item
        return None
```
