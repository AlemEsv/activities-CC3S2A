# Red-Green-Refactor

**Objetivo de aprendizaje:**  El objetivo de este proyecto es desarrollar una clase ShoppingCart que permita gestionar de forma eficiente un carrito de compras. La clase debe soportar las siguientes funcionalidades:

- Agregar artículos al carrito: Permitir añadir productos especificando nombre, cantidad y precio unitario, gestionando la posibilidad de agregar múltiples cantidades del mismo producto.
- Eliminar artículos del carrito: Remover productos previamente agregados.
- Calcular el total del carrito: Sumar el costo total de los artículos en el carrito, considerando la cantidad y precio unitario de cada uno.
- Aplicar descuentos: Permitir la aplicación de un descuento porcentual sobre el total del carrito, con validación de rango y redondeo a dos decimales.
- Procesar pagos a través de un servicio externo: Integrar un gateway de pago mediante inyección de dependencias para facilitar pruebas utilizando mocks y stubs, permitiendo simular el procesamiento de pagos sin realizar llamadas a servicios externos reales.

El proyecto se desarrollará de forma incremental utilizando el proceso RGR (Red, Green, Refactor) y pruebas unitarias con pytest para asegurar la correcta implementación de cada funcionalidad.


## Ejemplo

### Iteración 1: agregar artículos al carrito

#### 1. Red

![](img/img1.png)

#### 2. Green

![](img/img2.png)

#### 3. Refactor

##### Lógica para agregar múltiples cantidades del mismo artículo

![](img/img3.png)

### Iteración 2: eliminar artículos del carrito

#### 1. Red

![](img/img4.png)

#### 2. Green

![](img/img5.png)

### Iteración 3: calcular el total del carrito

#### 1. Red

![](img/img6.png)

#### 2. Green

![](img/img7.png)

#### 3. Refactor

![](img/img8.png)

## Ejemplo avanzado

### Iteración 4: agregar artículos al carrito

#### 1. Red

![](img/img9.png)

#### 2. Green

![](img/img10.png)

### Iteración 5: eliminar artículos del carrito

#### 1. Red

![](img/img11.png)

#### 2. Green

![](img/img12.png)

#### 3. Refactor

![](img/img13.png)

### Iteración 6: calcular el total del carrito

#### 1. Red

![](img/img14.png)

#### 2. Green

![](img/img15.png)

#### 3. Refactor

![](img/img16.png)

### Iteración 7: aplicar descuentos al total

#### 1. Red

![](img/img17.png)

#### 2. Green

![](img/img18.png)

#### 3. Refactor

![](img/img19.png)

## RGR, mocks, stubs e inyección de dependencias

### Iteración 8: agregar artículos al carrito

#### 1. Red

![](img/img20.png)

#### 2. Green

![](img/img21.png)

### Iteración 9: eliminar artículos del carrito

#### 1. Red

![](img/img22.png)

#### 2. Green

![](img/img23.png)

#### 3. Refactor

![](img/img24.png)

### Iteración 10: calcular el total del carrito

#### 1. Red

![](img/img25.png)

#### 2. Green

![](img/img26.png)

#### 3. Refactor

![](img/img27.png)

### Iteración 11: aplicar descuentos al total

#### 1. Red

![](img/img28.png)

#### 2. Green

![](img/img29.png)

### Iteración 12: procesar Pagos a través de un Servicio Externo

#### 1. Red

![](img/img30.png)

#### 2. Green

![](img/img31.png)

#### 3. Refactor

![](img/img32.png)

## Ejercicio

### Iteración 1: agregar usuario

#### 1. Red

![](img/img33.png)

#### 2. Green

![](img/img34.png)

### Iteración 2: autenticación de usuario

#### 1. Red

![](img/img35.png)

#### 2. Green

![](img/img36.png)

### Iteración 3: uso de un Mock para verificar llamadas

#### 1. Red y Green

![](img/img37.png)

### Iteración 4: excepción al agregar usuario existente

#### 1. Red y Green

![](img/img38.png)

### Iteración 5: agregar un "Fake" repositorio de datos 

#### 1. Red

![](img/img39.png)

#### 2. Green

![](img/img40.png)

### Iteración 6: introducir un “Spy” de notificaciones

#### 1. Red

![](img/img41.png)

#### 2. Green

![](img/img42.png)
![](img/img43.png)
