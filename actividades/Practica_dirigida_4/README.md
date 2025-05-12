# Testing y DevOps con SOLID

## Nivel teórico

### 1. Clasificación de responsabilidades

- *Contexto:* El módulo `services.py` concentra orquestación de pagos.
- *Enunciado:* Señala cuatro responsabilidades concretas de `PaymentService`. Indica cuáles serían candidatas a extraerse a nuevos "policies" u "object collaborators" para reforzar SRP sin romper LSP.
- *Aceptación:* ensayo de 400 palabras; menciona qué fixtures habría que crear para las nuevas clases.

**Resolución:**

Los mocks simulan objetos que tratan de imitar la lógica de métodos reales, aunque se escriba erróneamente el nombre del método, este podrá llamar a ese método ficticio, colocarle una lógica propia y *simular* que se está tratando con el método original, por lo que el comportamiento general permanecerá consistente en el tiempo.
Esto puede suponer llamadas erróneas por lo que en pruebas más rigurosas se usan los usespecs, oara restringir el uso del mock a solo poder imitar la lógica de métodos ya conocidos por esa clase.

### 2. Mapa de dependencias

### 3. Análisis de sustitución

### 4. Cobertura

- Lógica incorrecta validada por inputs limitados.

- Fallos ante entradas corruptas o inesperadas.

- Contratos rotos entre servicios.

### 5. Ventajas y riesgos de monkeypatch

- *Enunciado:* contrapón en 300 palabras setter-like vs constructor-like.
- *Aceptación:* lista de "casos de uso apropiados" y "smells" para cada estilo.

**Resolución:**

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

*Objetivo:* permitir que los mismos tests usen `DummyGateway` localmente y un gateway real en integración.

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

*Objetivo:* señalar tests que verifiquen invariantes de dominio (p. ej. "no se persiste un `Payment` sin usuario").

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

*Objetivo:* generar montos aleatorios positivos y verificar que siempre se persiste el pago.

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

## Stubs & Mocks y configuraciones avanzadas

1. **Modelo de sustitución y variabilidad**
   Explica por qué `DummyGateway` cumple el Principio de Sustitución de Liskov mientras que un mock sin autospec podría violarlo

2. **Side effects y semántica de idempotencia**
   Describe al menos dos riesgos de emplear `side_effect` para simular errores transitorios en un servicio que, en producción, debe ser idempotente.

    a. Simulación incorrecta del estado del sistema:

    Si el `side_effect` simula un fallo y luego una respuesta exitosa, puede ocultar que la operación fue parcialmente completada en el primer intento.

    b.  (...)

3. **Covarianza de fixtures**
   Analiza la diferencia semántica entre una fixture `function` y una fixture `session` cuando el recurso subyacente representa un pool de conexiones HTTP.

    - **scope="function"**

    Una nueva instancia del pool se crea por cada test.

    - **scope="session"**

    Una sola instancia del pool se crea al comienzo y se comparte por todos los tests.

4. **Cobertura vs. mutación**
   Define **cobertura de línea** y **tasa de mutantes muertos**.

### Cobertura de línea

Métrica que indica qué porcentaje de líneas de código fueron ejecutadas al correr una suite de pruebas.

- Ejemplo: Si tu código tiene 100 líneas ejecutables y tus tests pasan por 85, entonces la cobertura de línea es del **85%**.

### Tasa de mutantes muertos

métrica usada en mutation testing que mide qué tan efectivas son tus pruebas al detectar cambios sutiles (mutaciones) en el código.

- Ejemplo: Si se generan 50 mutantes y 45 son detectados por las pruebas (mueren), la tasa de mutantes muertos es del **90%**.
