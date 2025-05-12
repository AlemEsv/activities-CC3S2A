# Testing y DevOps con SOLID

## Nivel teórico

### 1. Clasificación de responsabilidades

Los mocks simulan objetos que tratan de imitar la lógica de métodos reales, aunque se escriba erróneamente el nombre del método, este podrá llamar a ese método ficticio, colocarle una lógica propia y *simular* que se está tratando con el método original, por lo que el comportamiento general permanecerá consistente en el tiempo.
Esto puede suponer llamadas erróneas por lo que en pruebas más rigurosas se usan los usespecs, oara restringir el uso del mock a solo poder imitar la lógica de métodos ya conocidos por esa clase.

### 2. Mapa de dependencias

### 3. Análisis de sustitución

### 4. Cobertura

- Lógica incorrecta validada por inputs limitados

- Fallos ante entradas corruptas o inesperadas

- Contratos rotos entre servicios  

### 5. Ventajas y riesgos de monkeypatch

#### Setter-like (patch directo)

a) Casos de uso apropiados:

- Parchear métodos o funciones específicas en bibliotecas de terceros.

- Simular errores como fallos de red o excepciones temporales.

- Pruebas rápidas de condiciones excepcionales sin refactor.

b) Smells:

- Parcheo excesivo de funciones internas (indicativo de mal diseño).

- Dependencia en nombres internos o rutas frágiles.

- Difícil de mantener si la implementación cambia.

#### Constructor-like (inyección de dependencias)

a) Casos de uso apropiados:

- Código basado en interfaces o dependencias inyectables.

- Reemplazo limpio por mocks, stubs o fakes.

- Compatible con SOLID (especialmente DIP y SRP).

b) Smells:

- Uso forzado de parámetros solo para tests.

- Constructores sobrecargados con múltiples dependencias.

- Repetición excesiva de configuración en múltiples tests.
