# Orquestador local de entornos de desarrollo simulados con Terraform

Demostraremos los conceptos y principios fundamentales de IaC utilizando Terraform para gestionar un entorno de desarrollo simulado completamente
local. Aprenderemos a definir, aprovisionar y modificar "infraestructura" (archivos, directorios, scripts de configuración)  de forma reproducible y automatizada.

## Estructura del proyecto (Archivos y directorios)

```bash
proyecto_iac_local/
├── main.tf                     # Configuración principal de Terraform
├── variables.tf                # Variables de entrada
├── outputs.tf                  # Salidas del proyecto
├── versions.tf                 # Versiones de Terraform y providers (local, random)
├── terraform.tfvars.example    # Ejemplo de archivo de variables
│
├── modules/
│   ├── application_service/    # Módulo para simular un "servicio"
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   │   └── templates/
│   │       └── config.json.tpl # Plantilla de configuración del servicio
│   │
│   └── environment_setup/      # Módulo para la configuración base del entorno
│       ├── main.tf
│       ├── variables.tf
│       └── scripts/
│           └── initial_setup.sh # Script de Bash para tareas iniciales
│
├── scripts/                    # Scripts globales
│   ├── python/
│   │   ├── generate_app_metadata.py # Genera metadatos complejos para apps
│   │   ├── validate_config.py       # Valida archivos de configuración generados
│   │   └── report_status.py         # Genera un reporte del "estado" del entorno
│   └── bash/
│       ├── start_simulated_service.sh # Simula el "arranque" de un servicio
│       └── check_simulated_health.sh  # Simula una "comprobación de salud"
│
└── generated_environment/      # Directorio creado por Terraform
    └── (aquí se crearán archivos y directorios)
```

## Actividad detallada por fases y conceptos

### Fase 0: Preparación e introducción

1. **¿Qué es infraestructura?**
      * Explica que, en este contexto local, la "infraestructura" serán directorios, archivos de configuración, scripts y la estructura lógica que los conecta.
      * Compara con infraestructura tradicional (servidores físicos, redes) y cloud (VMs, VPCs).
      RESPONDER
2. **¿Qué es infraestructura como código (IaC)?**
      * **Configuración manual de infraestructura:**
          * Simula la creación manual de `generated_environment/app1/config.json` y `generated_environment/app1/run.sh`. Discute la propensión a errores, la falta de reproducibilidad y la dificultad para escalar.
          RESPONDER
      * **Infraestructura como código:**
          * Repasa Terraform como la herramienta que nos permitirá definir esta estructura en archivos de código (`.tf`).
          * Revisa un `main.tf` muy simple que solo cree un directorio. Presenta a tus compañeros un ejemplo.
          RESPONDER
      * **¿Qué NO es infraestructura como código?**
          * Escribe script que modifican infraestructura existente sin un estado deseado definido.
          * Documenta sobre cómo configurar manualmente (aunque es útil, no es IaC).
          * Modifica manualmente los recursos creados por Terraform después de `apply`.
          RESPONDER

### Fase 1: Fundamentos de terraform y primer recurso local

* **Concepto:** Creación básica de recursos.

### Fase 2: Variables, archivos de configuración y scripts Bash

* **Conceptos:** Parametrización, ejecución de scripts locales.

### Fase 3: Módulos, plantillas y scripts Python

* **Conceptos:** Modularización, generación dinámica de archivos, integración con Python.

### Fase 4: Validación y reportes (Python y Bash)

* **Conceptos:** Scripts para verificar el estado, gestión del cambio (implícita).

## Ejercicios

1. **Ejercicio de evolvabilidad y resolución de problemas:**

      * **Tarea:** Añade un nuevo "servicio" llamado `database_connector` al `local.common_app_config` en `main.tf`. Este servicio requiere un parámetro adicional en su configuración JSON llamado `connection_string`.
      * **Pasos:**
        1. Modifica `main.tf` para incluir `database_connector`.
        2. Modifica el módulo `application_service`:
              * Añade una nueva variable `connection_string_tpl` (opcional, por defecto un string vacío).
              * Actualiza `config.json.tpl` para incluir este nuevo campo.
              * Haz que el `connection_string` solo se incluya si la variable no está vacía (usar condicionales en la plantilla o en `locals` del módulo).
        3. Actualiza el script `validate_config.py` para que verifique la presencia y formato básico de `connection_string` SOLO para el servicio `database_connector`.
      * **Reto adicional:** Haz que el `start_simulated_service.sh` cree un archivo `.db_lock` si el servicio es `database_connector`.

2. **Ejercicio de refactorización y principios:**

      * **Tarea:** Actualmente, el `generate_app_metadata.py` se llama para cada servicio. Imagina que parte de los metadatos es común a *todos* los servicios en un "despliegue" (ej. un `deployment_id` global).
      * **Pasos:**
        1. Crea un nuevo script Python, `generate_global_metadata.py`, que genere este `deployment_id` (puede ser un `random_uuid`).
        2. En el `main.tf` raíz, usa `data "external"` para llamar a este nuevo script UNA SOLA VEZ.
        3. Pasa el `deployment_id` resultante como una variable de entrada al módulo `application_service`.
        4. Modifica `generate_app_metadata.py` y/o `config.json.tpl` dentro del módulo `application_service` para que incorpore este `deployment_id` global.
      * **Discusión:** ¿Cómo mejora esto la composabilidad y reduce la redundancia? ¿Cómo afecta la idempotencia?

3. **Ejercicio de idempotencia y scripts externos:**

      * **Tarea:** El script `initial_setup.sh` crea `placeholder_$(date +%s).txt`, lo que significa que cada vez que se ejecuta (si los `triggers` lo permiten), crea un nuevo archivo.
      * **Pasos:**
        1. Modifica `initial_setup.sh` para que sea más idempotente: antes de crear `placeholder_...txt`, debe verificar si ya existe un archivo `placeholder_control.txt`. Si no existe, lo crea y también crea el `placeholder_...txt`. Si `placeholder_control.txt` ya existe, no hace nada más.
        2. Ajusta los `triggers` del `null_resource "ejecutar_setup_inicial"` en el módulo `environment_setup` para que el script se ejecute de forma más predecible (quizás solo si una variable específica cambia).
      * **Reto adicional:** Implementa un "contador de ejecución" en un archivo dentro de `generated_environment`, que el script `initial_setup.sh` incremente solo si realmente realiza una acción.

4. **Ejercicio de seguridad simulada y validación:**

      * **Tarea:** El `mensaje_global` se marca como `sensitive` en `variables.tf`. Sin embargo, se escribe directamente en `config.json`.
      * **Pasos:**
        1. Modifica el script `validate_config.py` para que busque explícitamente el contenido de `mensaje_global` (que el estudiante tendrá que "conocer" o pasar como argumento al script de validación) dentro de los archivos `config.json`. Si lo encuentra, debe marcarlo como un "hallazgo de seguridad crítico".
        2. Discute cómo Terraform maneja los valores `sensitive` y cómo esto se puede perder si no se tiene cuidado al pasarlos a scripts o plantillas.
        3. (Opcional) Modifica la plantilla `config.json.tpl` para ofuscar o no incluir directamente el `mensaje_global` si es demasiado sensible, tal vez solo una referencia.
