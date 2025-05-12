# Testing y DevOps con SOLID

## Nivel teórico

### 1. Clasificación de responsabilidades


Los mocks simulan objetos que tratan de imitar la lógica de métodos reales, aunque se escriba erróneamente el nombre del método, este podrá llamar a ese método ficticio, colocarle una lógica propia y *simular* que se está tratando con el método original, por lo que el comportamiento general permanecerá consistente en el tiempo.
Esto puede suponer llamadas erróneas por lo que en pruebas más rigurosas se usan los usespecs, oara restringir el uso del mock a solo poder imitar la lógica de métodos ya conocidos por esa clase.

### 2. Mapa de dependencias

### 3. Análisis de sustitución

### 4. Cobertura

### 5. Ventajas y riesgos de monkeypatch

## Nivel implementación, código y fixtures

### 6. Fixture condicional por entorno

### 7. Custom marker @pytest.mark.contract

### 8. Policy de reintentos

### 9. Property-based testing con Hypothesis

### 10. Observabilidad: logging configurable

## Nivel proyecto

SRP: 1 responsabilidad

OCP: principio de abierto/cerrado

LSP: liesik




