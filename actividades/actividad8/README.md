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
![](img/img10.png)
#### c. actualizar_cantidad()
![](img/img12.png)
### Prueba #1: Validar si la cantidad del producto agregado está en el límite de stock
![](img/img13.png)
### Prueba #2: Lanzar excepción si se agregan más de la cuenta.
![](img/img14.png)
## Ejercicio 4: Ordenar items del carrito
### Se creó el método *obtener_items_ordenados()* usando el método sorted() 
![](img/ig15.png)
### Prueba #1: Verificar si se ordena los productos por nombre
![](img/img15.png)
### Prueba #2: Verificar si se ordena los productos por precio
![](img/img16.png)
## Ejercicio 5: Uso de Pytest Fixtures
### Creación de fixtures para la refactorización de las pruebas.
##### Para este caso se colocaron 4 productos por los casos de ordenamiento de objetos.
![](img/img17.png)
### Refactorización:
![](img/img18.png)
![](img/img19.png)
![](img/img20.png)
![](img/img21.png)
![](img/img22.png)
![](img/img23.png)
![](img/img24.png)
![](img/img25.png)
![](img/img26.png)
![](img/img27.png)
![](img/img28.png)
![](img/img29.png)
![](img/img30.png)
# Ejercicio 6: Pruebas parametrizadas
### Prueba #1: Parametrizando pruebas para el método *aplicar descuento*:
![](img/img31.png)
## Prueba #2: Parametrizando pruebas para el método *actualizar cantidades*:
![](img/img32.png)
# Ejercicio 7: Calcular impuestos en el carrito
#### Red:
![](img/img33.png)
### Green:
![](img/img34.png)
### Refactor:
![](img/img35.png)
# Ejercicio 8: Aplicar cupón de descuento con límite máximo
#### Red:
![](img/img36.png)
### Green:
![](img/img37.png)
### Refactorizar:
![](img/img38.png)
# Ejercicio 9: Validación de stock al agregar productos (RGR)
#### Red:
![](img/img39.png)
### Green:
![](img/img40.png)
### Refactor:
![](img/img41.png)