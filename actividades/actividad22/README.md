# Actividad 22: Patrones de dependencias y módulos en IaC con Terraform y Python

## Fase 1: Relaciones unidireccionales

* grafo generado del fichero **network**:

Actualmente, la carpeta network/ contiene el módulo de red, definido en network.tf.json. Este módulo simula la creación de una red usando recursos locales (null_resource y local_file) y expone sus salidas (outputs) en un archivo JSON (network_outputs.json).

![alt-text](/Inversion_control/network/graph.png)
