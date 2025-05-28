# Actividad: Orquestador local de entornos de desarrollo simulados con Terraform

**PreRequisitos:**

- Terraform.
- Python 3.
- Conocimientos básicos de bash.
- Editor de texto o IDE.

## Instalación Terraform ubuntu

1. Actualizar lista de paquetes

    ```bash
    sudo apt-get update && sudo apt-get install -y gnupg    software-properties-common
    ```

2. Agregar la clave GPG de HashiCorp

    ```bash
    wget -O- https://apt.releases.hashicorp.com/gpg | \
    gpg --dearmor | \
    sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null
    ```

3. Verificar la huella de la llave

    ```bash
    gpg --no-default-keyring \
    --keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg \
    --fingerprint
    ```

4. Agregar repositorio de HashiCorp

    ```bash
    echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
    ```

5. Instalar terraform

    ```bash
    sudo apt install terraform
    ```

**Más información en [Terraform/install](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)**

## Problemas previos

Estoy accediendo a **ubuntu** mediante WSL en windows, ya que el proyecto no reconoce ciertos comandos en bash ejecutados en Windows.

### 1. Ejecutable de python

Inicialmente cambio la variable de ejecución de python a la ruta que tengo por defecto con ubuntu.

```json
variable "python_executable" {
  description = "Ruta al ejecutable de Python (python o python3)."
  type        = string
  default     = "/usr/bin/python3" # <--- cambio
}
```

### 2. Archivos ocultos

Algunos archivos tenían caracteres ocultos `\r` debido a que eran tratador para ejecución en windows. Problema que hace que bash no sea capaz de leer bien ciertos archivos.

Al correr en Linux o mediante WSL, hay que quitarlos manualmente cambiando de **CRLF a LF** en la barra inferior a la derecha dentro de vscode o de el IDE utilizado.

![alt](image.png)

### 3. Flag "-p"

Verificar que el comando mkdir tenga el flag `-p`, ya que sino al intentar crear un directorio dentro de una estructura que aún no existe, mkdir fallará.

```json
provisioner "local-exec" {
    command = "mkdir -p ${local.install_path}/logs"
  }
```

## Inicializar el proyecto

Este proyecto contiene un orquestador local, que mediante Terraform, crea, configura y valida entornos de desarrollo simulados con múltiples servicios.

```yaml
# inicializamos el entorno y descargar los providers
terraform init

# Muestra la infraestructura que se creará en base a los archivos creados
# (opcional)
terraform plan

# Creación de la infraestructura
terraform apply -auto-approve
```

Por último, verificaremos la salida en consola que segun el archivo `outputs-tf` debería ser el siguiente:

```yaml
output "detalles_apps_simuladas" {
  value = {
    for k, app_instance in module.simulated_apps : k => {
      config_path  = app_instance.service_config_path
      install_path = app_instance.service_install_path
      # metadata    = app_instance.service_metadata_content # Puede ser muy verboso
      metadata_id = app_instance.service_metadata_content.uniqueId
    }
  }
  sensitive = true # Porque contiene mensaje_global (indirectamente)
}
```

Y efectivamente, hemos creado la infraestructura de forma satisfactoria.

![alt](image-1.png)

y para el momento que ya no necesitemos tener la infraestructura activa, podemos destruirla.

```bash
# destruye la infraestructura existente
terraform destroy -auto-approve
```

![alt text](image-2.png)
