# Ejercicios
## Ejercicio 1: Método para vaciar el carrito
#### Creación del método *vaciar()*: 
![](img/img1.png)
### Prueba #1: verificar si el carrito está vacío
![](img/img2.png)
### Prueba #2: verificar si el carrito vacío no retorna un total de elementos
![](img/img3.png)
## Ejercicio 2: Descuento por compra mínima
#### Creación de la función *aplicar_descuento_condicional()*:
![](img/img6.png)
### Prueba #1: Verificar si el descuento condicional se cumple
![](img/img4.png)
### Prueba #2: Verificiar si el descuento condicional no se cumple

![](img/img5.png)
## Ejercicio 3: Manejo de stock en producto
### Modificación de la clase **Producto** para que tenga un stock
![](img/img7.png)
![](img/img8.png)
### Modificación de las clases que agreguen o quiten productos del carrito para que tomen en cuenta la existencia de un producto con stock
#### a. agregar_producto():
![](img/img9.png)
#### b. remover_producto():
![](img/mg10.png)
#### c. actualizar_cantidad()
![](img/mg12.png)
### Prueba #1: Validar si la cantidad del producto agregado está en el límite de stock
![](img/mg13.png)
### Prueba #2: Lanzar excepción si se agregan más de la cuenta.
![](img/mg14.png)
## Ejercicio 4: Ordenar items del carrito
### Se creó el método *obtener_items_ordenados()* usando el método sorted() 
![](img/ig15.png)
### Prueba #1: Verificar si se ordena los productos por nombre
![](img/mg15.png)
### Prueba #2: Verificar si se ordena los productos por precio
![](img/mg16.png)
## Ejercicio 5: Uso de Pytest Fixtures
### Creación de fixtures para la refactorización de las pruebas.
##### Para este caso se colocaron 4 productos por los casos de ordenamiento de objetos.
![](img/mg17.png)
### Refactorización:
![](img/mg18.png)
![](img/mg19.png)
![](img/mg20.png)
![](img/mg21.png)
![](img/mg22.png)
![](img/mg23.png)
![](img/mg24.png)
![](img/mg25.png)
![](img/mg26.png)
![](img/mg27.png)
![](img/mg28.png)
![](img/mg29.png)
![](img/mg30.png)
# Ejercicio 6: Pruebas parametrizadas
### Prueba #1: Parametrizando pruebas para el método *aplicar descuento*:
![](img/mg31.png)
## Prueba #2: Parametrizando pruebas para el método *actualizar cantidades*:
![](img/mg32.png)
# Ejercicio 7: Calcular impuestos en el carrito
#### Red:
![](img/mg33.png)
### Green:
![](img/mg34.png)
### Refactor:
![](img/mg35.png)
# Ejercicio 8: Aplicar cupón de descuento con límite máximo
#### Red:
![](img/mg36.png)
### Green:
![](img/mg37.png)
### Refactorizar:
![](img/mg38.png)
# Ejercicio 9: Validación de stock al agregar productos (RGR)
#### Red:
![](img/mg39.png)
### Green:
![](img/mg40.png)
### Refactor:
![](img/mg41.png)