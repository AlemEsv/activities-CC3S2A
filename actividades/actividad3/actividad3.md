## 1. Motivaciones para la nube

##### a. ¿Qué problemas o limitaciones existían antes del surgimiento de la computación en la nube y cómo los solucionó la centralización de servidores en data centers?

Los problemas principales de las empresas eran los grandes costos para tener hardware físico necesario para sus proyectos, esto escapaba de empresas medianas o pequeñas, ya que no se podían permitir tener una infraestructura robusta y consistente. Además no había un escalado de recursos flexible y rápidamente adaptable a las necesidades cambiantes de los negocias gracias a la gran cantidad de dinero que conllevaba hacer cambios.

Para esto la nube vino a encontrar una solución mediante la centralización de servidores que puedan ser accedidos por diferentes usuarios mediante el internet, teniendo un costo por el servicio sin necesidad de tener la infraestructura de manera física, pudiendo configurarla a la necesidad de la empresa y poder dar una reducción en costos.

##### b. ¿Por qué se habla de “The Power Wall” y cómo influyó la aparición de procesadores multi-core en la evolución hacia la nube?

Power Wall es llamado a la barrera física y técnica que limitaba el rendimiento de los procesadores de aquellas epocas. Se trató de contrarrestar aumentando la frecuencia de reloj para así poder mejorar el rendimiento de las CPU pero generaba un consumo excesivo de energía, calor y una limitación en la eficiencia llegando a cierto punto.

Esto provocó a la aparición de procesadores de nucleos múltiples, los cuales aumentaban el rendimiento del CPU sin necesidad de un incremento de frecuencia de reloj permitiendo el crecimiento exponencial de la **computación en la nube** al proporcionar mayor eficiencia y escalabilidad.
## 2. Clusters y load balancing
##### a. Explica cómo la necesidad de atender grandes volúmenes de tráfico en sitios web condujo a la adopción de clústeres y balanceadores de carga.
A medida que los sitios web crecieron en popularidad y tráfico, surgió la necesidad de infraestructuras más robustas para garantizar disponibilidad, rendimiento y escalabilidad. Esto llevó a la adopción de **clústeres** de servidores y **balanceadores de carga**, que permiten distribuir el tráfico de manera eficiente.

Cuando un sitio web recibe un alto número de solicitudes, un solo servidor puede convertirse en un cuello de botella. Algunas de las limitaciones incluyen:
- **Capacidad limitada de procesamiento y memoria**.
- **Mayor tiempo de respuesta** debido a la sobrecarga.
- **Fallas en la disponibilidad** si el servidor se cae o experimenta problemas.

##### b. Describe un ejemplo práctico de cómo un desarrollador de software puede beneficiarse del uso de load balancers para una aplicación web.
Imaginemos que un desarrollador está construyendo una aplicación web para una tienda en línea. A medida que el sitio crece en popularidad, miles de usuarios intentan acceder simultáneamente, generando una carga pesada en el servidor.

### Problema sin Balanceador de Carga
- Un único servidor puede saturarse rápidamente, afectando el rendimiento y aumentando los tiempos de respuesta.
- Si el servidor falla, la tienda en línea deja de estar disponible, lo que afecta las ventas y la experiencia del usuario.

### Solución con Balanceador de Carga

- Se implementa un **balanceador de carga** que distribuye las solicitudes entre varios servidores.
- Si un servidor falla, el balanceador redirige el tráfico automáticamente a los servidores activos, asegurando la disponibilidad del servicio.
- Se pueden agregar nuevos servidores al clúster según la demanda, mejorando la escalabilidad.
### Beneficios

- **Mejor rendimiento**: La carga se distribuye, evitando que un solo servidor se sobrecargue.
- **Alta disponibilidad**: La aplicación sigue funcionando incluso si uno o más servidores fallan.
- **Escalabilidad**: Se pueden agregar más servidores sin interrumpir el servicio.

## 3. Elastic computing

##### a. Define el concepto de Elastic Computing.

Es la capacidad que tiene la nube para poder gestionar sus recursos informáticos para situaciones donde haya un uso máximo de los recursos sin necesidad de planeamientos previos.

##### b. ¿Por qué la virtualización es una pieza clave para la elasticidad en la nube?

la virtualización es una herramienta que permite hacer la gestión de recursos sin necesidad de depender de un hardware físico, por lo que es una parte crucial, sin la virtualización se tendría que esperar y verificar el estado de los componentes físicos de la infraestructura de nuestro software.

##### c. Menciona un escenario donde, desde la perspectiva de desarrollo, sería muy difícil escalar la infraestructura sin un entorno elástico.


## 4. Modelos de servicio(IaaS, PaaS, AaaS, DaaS)
##### a. Diferencia cada uno de estos modelos. ¿En qué casos un desarrollador optaría por PaaS en lugar de IaaS?

- **IaaS:** El usuario puede gestionar el SO y sus aplicaciones.
- **PaaS**: El usuario solo puede hacer uso de las aplicaciones dentro de la infraestructura del proveedor de la nube.
- **AaaS:** El usuario solo es capaz de visualizar y analizar datos dentro de una aplicación en la nube.
- **DaaS:** El usuario solo puede acceder a los escritorios remotos.

Un desarrollador va optar por un PaaS cuando solo quiera hacer uso de las herramientas que proporciona una plataforma, sin necesidad de tener control sobre la administración de servidores, configuraciones de la red o el manejo del SO propuesto.

##### b. Enumera tres ejemplos concretos de proveedores o herramientas que correspondan a cada tipo de servicio.

| Servicio | Proveedor 1       | Proveedor 2           | Proveedor 3           |
| -------- | ----------------- | --------------------- | --------------------- |
| IaaS     | Amazon EC2        | Google Compute Engine | Azure Virtual Machine |
| PaaS     | Google App Engine | Heroku                | Azure App Service     |
| AaaS     | Google BigQuery   | AWS QuickSight        | Microsoft Power BI    |
| DaaS     | Amazon WorkSpaces | Azure Virtual Desktop | Citrix VIrtual Apps   |

## 5. Tipos de nubes
#### a. ¿Cuáles son las ventajas de implementar una nube privada para una organización grande?

#### b. ¿Por qué una empresa podría verse afectada por el “provider lock-in”?

#### c. ¿Qué rol juegan los “hyperscalers” en el ecosistema de la nube?


# Estudio de casos

## 1. Empresas que migraron a la nube
#### a. Instagram

#### b. Netflix

#### c.

