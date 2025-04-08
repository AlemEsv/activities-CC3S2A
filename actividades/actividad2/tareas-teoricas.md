> **Tareas teóricas**  
### Terraform 
Una herramienta de IaC que proporciona un flujo de trabajo de aprovisionamiento y gestion de infrastructura en cualquier nube mediante archivos declarativos en HCL.
Los modulos son configuraciones pequeñas y reurtilizables para multiples recursos de la infrastructura que se utilizan juntos. Un ejemplo de como se organizan los modulos en terraform es de la siguiente manera:
```plaintext
Project/
|── main.tf
|── variables.tf
|── outputs.tf
|── modulo/
|  |── network/
|  |  |── main.tf
|  |  |── variables.tf
|  |  |── outputs.tf
|  |── database/
|  |  |── main.tf
|  |  |── variables.tf
|  |  |── outputs.tf
|  |── application/
|  |  |── main.tf
|  |  |── variables.tf
|  |  |── outputs.tf
```
Se utiliza esta estructura ya que la separacion de modulos (network, database, application) facilita la reutilizacion del codigo, ademas que facilita el mantenimiento ya que cada modulo esa aislado.

### Describir un flujo simple de despliegue donde un desarrollador hace un cambio en el código, se construye una nueva imagen Docker y se actualiza un Deployment de Kubernetes.  

1. Se hace un cambio en el código fuente del software.
2. El código se sube a un sistema de control de versiones, como Git.
3. Se genera una imagen Docker conteniendo los cambios ya implementados. Para evitar conflictos, a la imagen se le pone una etiqueta con una versión específica, facilitando su rastreo.
4. Se carga esta imagen nueva a un registro de contenedores, como Docker Hub, para que Kubernetes pueda acceder a esta.
5. Se edita el archivo .yaml del Deployment para actualizar la nueva imagen recién creada. Acá se define que versión de la aplicación será usada en los Pods del clúster.
6. Se aplica el cambio en Kubernetes.
7. Se revisa el estado del Deployment y se inspeccionan los Pods para asegurar de que la nueva versión está en correcto funcionamiento.
8. Se accede a los logs para verificar que no hay errores. Si hay fallos, se pueden corregir antes de que el despliegue afecte a los usuarios.

### Explicar las ventajas de usar Kubernetes para escalar una aplicación en un evento de alto tráfico.

Cuando una aplicación sufre un evento de alto tráfico, como el inicio de venta de entradas de un concierto o el lanzamiento de un nuevo producto en una tienda virtual, es importante que el sistema pueda manejar ese gran aumento de usuarios sin fallar. Para esto nos ayuda Kubernetes, ya que permite ajustar automáticamente los recursos de la aplicación de manera eficiente dependiendo de la demanda, evitando caidas en el servicio, a continuación algunas ventajas de usar Kubernetes en estos casos:

1. Escalado automático: Kubernetes ajusta la cantidad de instancias, aumentándolas o reduciéndolas, dependiendo de la demanda actual, sin necesidad de una intervención humana.

2. Distribución de carga: Kubernetes reparte el tráfico con todas las instancias disponibles, evitando sobrecargas por tantas operaciones en algunas.

3. Alta disponibilidad: En caso de que una instancia falle (por diferentes motivos), Kubernetes la reemplaza automáticamente para que el servicio no se detenga o reduzca su velocidad y seguir manteniéndose en funcionamiento.

4. Optimización de recursos: Kubernetes ajusta el consumo de memoria y CPU según la carga que se esté experimentando, administrando muy bien los recursos y optimizando el rendimiento.

5. Versatilidad: Funciona en distintos entornos: en la nube, servidores físicos o en una combinación de estos, lo cual nos da una alta disponibilidad.

### Proponer un set de métricas y alertas mínimas para una aplicación web (por ejemplo, latencia de peticiones, uso de CPU/memoria, tasa de errores).

**1. Métricas de Aplicación**

- Latencia de peticiones: Un aumento en la latencia puede indicar que algo no está funcionando correctamente, por ejemplo problemas de rendimiento en la aplicación o en la base de datos. Se deben identificar estos grandes latencias para evitar una mala experiencia al usuario.
- Tasa de errores: Una alta tasa de errores (HTTP 4xx o 5xx) puede indicar problemas como errores de autenticación o fallos en la API/backend. Si estos errores se no corrigen rápidamente, pueden ocasionar suspensiones en el servicio.
- Número de solicitudes: Permite analizar patrones de tráfico y detectar posibles cuellos de botella cuando hay bastante carga. Entonces, analizar el tráfico nos permite optimizar la escalabilidad.

**2. Métricas de Infraestructura**

  - Uso de CPU: Un alto consumo de CPU puede ser originado por un aumento en los procesos de solicitudes o por código ineficiente. Detectar estas sobrecargas evita que el servidor se colapse.
  - Uso de memoria: Si el consumo de memoria es demasiado alto puede ocasionar problemas o reinicios forzados por Kubernetes, esto es conocido como OOMKill. Entonces, es importante estar atento a estos consumos para evitar problemas en el despliegue.
  
**3. Métricas de Base de Datos**

- Conexiones activas: Si se alcanza el límite de conexiones permitido en la base de datos, la aplicación puede llegar a fallar o volverse inestable. Por eso, tener una buena gestión de conexiones evita a que el sistema de bloquee.
- Errores en consultas: Un aumento en los errores de queries puede indicar problemas en la base de datos, ocasionando bloqueos o consultas ineficientes.

### Investigar y describir cómo Prometheus y Grafana se integran con Kubernetes para monitorear los contenedores y el cluster.

- **Prometheus:** Sistema de monitoreo encargado de crear métricas de los componentes del clúster y de las aplicaciones en ejecución. Se despliega como un Pod independiente o junto con Prometheus Operator.

- **Grafana:** Grafana se complementa con Prometheus, brinda representación visual de las métricas obtenidas. También se ejecuta como un Pod en Kubernetes y se configura para obtener datos directamente desde Prometheus como su fuente de datos.

## Explicar la diferencia entre entrega continua (continuous delivery) y despliegue continuo (continuous deployment).

Primeramente, el **continuous delivery** automatiza los testeos de la aplicación, pero deja el tema del despliegue a producción a decisión del desarrollador, de forma manual. Por otro lado el **continuous deployment**  te lleva automáticamente al despliegue en producción, cosa que ayuda a tener un flujo de trabajo más rápido aunque no siempre más eficaz. Cada uno se uso dependiendo del contexto de tu desarrollo de software asi que no hay una mejor forma que la otra.

## Describir la relevancia de implementar pruebas automáticas (unitarias, de integración, de seguridad) dentro del pipeline.

El uso de pruebas automáticas en el pipeline de desarrollo es importante para garantizar la escalabilidad, calidad y seguridad del software. 
Estas pruebas, al estar automatizadas, detectan errores de forma temprana, reduciendo así problemas en producción como también costos asociados a su corrección.

- **Pruebas unitarias:** Estas pruebas verifican que el funcionamiento de componentes individuales del código esté correcto. A su vez, detecta errores en la fase temprana del desarrollo, simplificando el trabajos a los desarrolladores en la corrección del código antes de que sean añadidos en el sistema o que se vuelvan más complejos en etapas avanzadas.
- **Pruebas de integración:** En estas pruebas se evalúa cómo se comportan diferentes módulos o servicios dentro de la aplicación. Son importantes para detectar problemas entre componentes (incompatibilidad), como bases de datos o APIs. La identificación temprana evita que esos errores de comunicación afecten al software en la etapa de producción.
- **Pruebas de seguridad:** Estas pruebas son fundamentales ya que si no se aplican puede afectar la reputación de la empresa. Acá se detectan vulnerabilidades en el código o configuraciones erróneas que podrían ser aprovechadas por atacantes con el fin de hacer daño al sistema u obtener información.
