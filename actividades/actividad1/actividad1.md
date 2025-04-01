# DevOps
## Qué es DevOps (developers operators)

Conjunto de herramientas, procesos y cultura que permite entregar procedimientos a una alta velocidad, garantizando no aislamiento de equipos, estabilidad y calidad del software. 

Busca derribar el muro de la confusión entre desarrolladores y operadores, para poder integrar a todo el equipo de desarrollo.

Busca entregar actualizaciones de software frecuentes gracias al conjunto anteriormente mencionado.

## Ciclo de vida

Un ciclo que no será retrasado por ningun motivo, se busca no echar la culpa a otra persona dentro del equipo de desarrollo.

1. Planning

Planificación del software.

2. Coding

Se asigna el código para cada desarrollador y se empieza a escribir parte por parte según la asignación.

3. Building

Integración del código desarrollado después de pasar los test de integración.

4. Testing

Se testea cada parte de código con el fin de cumplir cada objetivo propuesto en el planning.

5. Realese

Se crea un ejecutable listo para pasar a producción.

6. Deploy

Se desplega un ejecutable para poder ser usado por los usuarios finales de la aplicación.

7. Operate

Tareas de optimización, configuración de sistemas, implementación de infraestructuras, etc.

8. Monitor

Herramientas que buscan mirar si la aplicación está en riesgo de sufrir un cambio no pronosticado, funciona en todo el proceso del desarrollo del software.

## CI/CD

Técnicas que permiten pasar por el ciclo de vida del desarrollo de software de manera automática.

### Primera etapa: CI (Continuous integration)

Creación de pruebas automatizadas cada que envies tu código a master para asegurar que no está rompiendo algo del código entero. Busca que cumpla con todos los estandares y politicas propuestas.

### Segunda etapa: CD (continuous deployment/distribution)

deployment: Toma el código ya probado de la parte de CI y crea un ejecutable listo para ser probado por el team.

## Herramientas de DevOps

**Jira:** usado para procesos con metodología Scrum

**Asana:** Permite a los equipos planificar, organizar y hacer un seguimiento de sus tareas y proyectos

**Trello:** usado en proyectos pequeños, fácil de usar

**Notion:** Todo en uno.

**gitHub:**  “red social de programadores”, enfocado en almacenar código de diferentes desarrolladores para el uso de todo el mundo.

**gitLab:** Usado en DevOps con herramientas para facilitad el pipeline de CI/CD

**Apache Maven:** ayuda a la ejecución, empaquetado y dependenias del software.

**Gradle**: pruebas, politicas para el código.

Testing Selenium y Gremlin para el monitorio de testeo de pruebas para el código.
