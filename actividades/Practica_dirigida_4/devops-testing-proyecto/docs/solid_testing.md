# Principios SOLID en Testing DevOps

## Fakes:
Creación de un dummy que simulará ser un usuario en mi aplicación.

## Configuración inicial en `config.py`:
Configuración globalizada e inmutable dentro de un dataclass que proporcional los elementos base que usará nuestro dummy para ser probado en diferentes pruebas siguiendo las estrategias SOLID.

## Fixtures en el modulo `conftest.py`:
se tiene los metodos *user_repo()* y *payment_repo()* con una implementación simple de lo que sería un usuario y su metodo de pago.

## Testing en la configuración de injecciones:
Con el dummy creado verificaremos si se trata de pagar con la moneda adecuada (Euro). 
```python
# Se verifica si hay un llamado a dummy
assert len(dummy_gateway.calls) == 1
_, currency, _ = dummy_gateway.calls[0]
# Se verifica si la currency está en EUROS
assert currency == "EUR"
```
Único caso especifico para no violar el principio de SRP usando un Interface-driven.


