> **Tarea teórica:**  
> - Investigar una herramienta de IaC (p. ej. Terraform) y describir cómo organiza sus módulos.  
> - Proponer la estructura de archivos y directorios para un proyecto hipotético que incluya tres módulos: `network`, `database` y `application`. Justificar la jerarquía elegida.
### Terraform

#### Módulos de terraform

### Estructura de archivos

> **Tarea teórica:**  
> - Describir un flujo simple de despliegue donde un desarrollador hace un cambio en el código, se construye una nueva imagen Docker y se actualiza un Deployment de Kubernetes.  
> - Explicar las ventajas de usar Kubernetes para escalar una aplicación en un evento de alto tráfico.
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
