# Testing y DevOps con SOLID

## Nivel teórico

### 1. Clasificación de responsabilidades

Los mocks simulan objetos que tratan de imitar la lógica de métodos reales, aunque se escriba erróneamente el nombre del método, este podrá llamar a ese método ficticio, colocarle una lógica propia y *simular* que se está tratando con el método original, por lo que el comportamiento general permanecerá consistente en el tiempo.
Esto puede suponer llamadas erróneas por lo que en pruebas más rigurosas se usan los usespecs, oara restringir el uso del mock a solo poder imitar la lógica de métodos ya conocidos por esa clase.

### 2. Mapa de dependencias

### 3. Análisis de sustitución

### 4. Cobertura

- Lógica incorrecta validada por inputs limitados.

- Fallos ante entradas corruptas o inesperadas.

- Contratos rotos entre servicios.

### 5. Ventajas y riesgos de monkeypatch

#### Setter-like (patch directo)

a) Casos de uso apropiados:

- Parchear métodos o funciones específicas en bibliotecas de terceros.

- Simular errores como fallos de red o excepciones temporales.

b) Smells:

- Parcheo excesivo de funciones.

- Dependencia en nombres internos.

#### Constructor-like (inyección de dependencias)

a) Casos de uso apropiados:

- Código basado en interfaces o dependencias inyectables.

- Reemplazo limpio por mocks, stubs o fakes.

b) Smells:

- Uso forzado de parámetros solo para tests.

- Constructores sobrecargados con múltiples dependencias.

### 6. Fixture condicional por entorno

```python
# conftest.py
@pytest.fixture
def gateway():
    use_real = os.getenv("USE_REAL_GATEWAY") == "1"
    if use_real:
        class RealGatewayWithLatency(RealGateway):
            def charge(self, user_id, amount):
                time.sleep(0.6)
                return super().charge(user_id, amount)
        return RealGatewayWithLatency()
    return DummyGateway()
```

### 7. Custom marker @pytest.mark.contract

Definir marcador `contract` en pytest.ini

```yaml
# pytest.ini
[pytest]
markers = contract: Tests que validan invariantes del dominio
```

```python
# test_payments.py
import pytest

# Etiquetar dos casos particulares.

@pytest.mark.contract
def test_no_payment_without_user():
    # test que asegura que no se puede persistir un pago sin usuario

@pytest.mark.contract
def test_user_balance_not_negative():
    # test que asegura que nunca se permite balance negativo
```

Ejecución de un step contract que verifica los tests que lleven el marcador `contract`

```yaml
 CI step (ejemplo YAML)
 - name: Contract tests
   run: pytest -m contract
```

### 8. Policy de reintentos

(...)

### 9. Property-based testing con Hypothesis

```bash
pip install hypothesis
# Colocar los requisitos actualizados
pip freeze > requirements.txt
```

Creación de una prueba con un tiempo de ejecución de < 1s con 100 ejemplos

```python
# test_payment_property.py
from hypothesis import given, strategies as st

def test_payment_persists_any_positive_amount(payment_service):
    @given(st.decimals(min_value=0.01, max_value=1000))
    def inner(amount):
        result = payment_service.process_payment("Alem", amount)
        assert result
    inner()

```

### 10. logging configurable

(...)
