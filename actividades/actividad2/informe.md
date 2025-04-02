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
