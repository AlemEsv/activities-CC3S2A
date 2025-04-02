# 1. Contenedores
Los contenedores son una forma de compartimento digital que contienen todos los archivos necesarios para poder correr un software. Normalmente contienen código, librerías, variables, archivos de configuración y herramientas de sistema. 
Ayudan a aislar cargas de trabajo pesadas, para poder tener una mejor robustez en la seguridad de la información del software.
### Problemas de seguridad
- Attack surfaces: al tener un kernel compartido hay posibilidad en hacer ataques desde otros contenedores mediante exploits.
- Herramientas de orquestación: partes defectuosas en dichas herramientas ayudan a facilitar un ataque dichos contenedores
# 2. Kubernetes
Un **software** de ayuda para el manejo de aplicaciones en contenedores.
### Secretos y manejo de configuraciones
Kubernetes te deja guardar y manejar información sensible como Oauth tokens y llaves SSH. El control de secretos por medio de kubernets te permite actualizar y aplicar secretos sin necesidad de hacer un rebuilding a los container de imágenes.
### Qué no es K8s
No lleva el sistema tradicional de todos los PaaS, aunque hace uso de funciones comunes que los PaaS ofrecen, como el escalado, deplyment, balanceo de carga, entre otros. Kubernetes provee de funcionalidads en bloques para preservar la flexibilidad al usuario a nivel hardware.
# 3. Observabilidad
Es la capacidad de comprender el estado interno de un sistema.

# 4. Time-to-market
Gracias al uso de pipelines CI/CD podemos reducir significativamente este "time-to-market", ya que se comienza a automatizar procesos dentro del ciclo build, test y deployment. Esto da un aceleramiento en el feedback por ciclo que se da dentro del ambiente del desarrollo de software, dando pasos más solidos hacia una mayor robustez en el código.
Además se da uso a herramientas de seguridad integradas en el proceso CI/CD, como el usio de testeos por medio de algoritmos de machine learning para encontrar la mayor cantidad de errores en el código en tan poco tiempo. Asi que para una empresa es muy necesario hacer uso de herramientas de CI/CD así agilizan el tiempo de mercado de sus productos de software.

# 5. Empresas y el uso de herramientas para el control de altos volúmenes de tráfico de datos  
Tenemos varios casos de herramientas que manejen dichos desafíos como:
- Netflix:
Netflix hace uso de balanceadores de carga elásticos (ELB) para distribuir mejor su tráfico entre zonas, además de tener bases de datos descentralizadas para poder tener mayor seguridad por si hay alguna caída en los almacenes de sus computadores, y así reducir errores por la cantidad de datos almacenados que tienen.
- Spotify: 
Spotify hace uso de Kubernetes como software para la gestión de la orquestación de contenedores en su infraestructura de microservicios.
- Uber: 
Uber maneja grandes volúmenes de datos utilizando softwares como apache Kafka para poder transmitir eventos de forma más eficiente, y Cassandra para el manejo de sus datos
