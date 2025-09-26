# Flujo Específico del Ejercicio - Inyección de Dependencias

## Diagrama de Cajas y Flechas del Flujo de Datos

Según las instrucciones del ejercicio en `actividades/actividad22/Inyeccion_dependencias/Instrucciones.md`, el flujo de datos entre los componentes es:

```
┌─────────────┐    ┌─────────────────────┐    ┌─────────┐    ┌───────────────┐    ┌───────────┐
│ network.tf  │───▶│ network_metadata.   │───▶│ main.py │───▶│ server.tf.json│───▶│ Terraform │
│             │    │ json                │    │         │    │               │    │           │
└─────────────┘    └─────────────────────┘    └─────────┘    └───────────────┘    └───────────┘
      1                        2                     3               4                   5
```

## Descripción Detallada del Flujo

### 1. **network.tf** → 2. **network_metadata.json**

**Componente**: `network/network.tf`
**Acción**: Define un `null_resource` con triggers de red y un `local_file` que genera metadatos.

```hcl
resource "null_resource" "network" {
  triggers = {
    name = "hello-local-network"
    cidr = "10.0.0.0/28"
  }
}

resource "local_file" "network_metadata" {
  content = jsonencode({
    name = null_resource.network.triggers.name,
    cidr = null_resource.network.triggers.cidr
  })
  filename = "${path.module}/network_metadata.json"
}
```

**Salida**: Archivo `network_metadata.json` con:
```json
{
  "name": "hello-local-network",
  "cidr": "10.0.0.0/28"
}
```

### 2. **network_metadata.json** → 3. **main.py**

**Componente**: `main.py`
**Acción**: Lee el archivo JSON de metadatos de red.

```python
def get_network_metadata(path="network/network_metadata.json"):
    with open(path) as f:
        data = json.load(f)
    return data['name'], data['cidr']
```

**Proceso**:
- Lee `network_metadata.json`
- Extrae `name` y `cidr`
- Calcula la quinta IP del rango CIDR (10.0.0.5)

### 3. **main.py** → 4. **server.tf.json**

**Componente**: `main.py` (clase `ServerFactoryModule`)
**Acción**: Genera configuración Terraform para el servidor.

```python
class ServerFactoryModule:
    def __init__(self, name, metadata_path="network/network_metadata.json"):
        self._name = name
        network_name, cidr = get_network_metadata(metadata_path)
        self._network = network_name
        self._network_ip = self._allocate_fifth_ip_address_in_range(cidr)
        self.resources = self._build()

    def _allocate_fifth_ip_address_in_range(self, ip_range):
        network = ipaddress.IPv4Network(ip_range)
        return str(list(network.hosts())[4])  # Quinta IP
```

**Salida**: Archivo `server.tf.json` con:
```json
{
    "resource": {
        "null_resource": {
            "server": {
                "triggers": {
                    "name": "hello-world",
                    "subnetwork": "hello-local-network",
                    "network_ip": "10.0.0.5"
                },
                "provisioner": [{
                    "local-exec": {
                        "command": "echo Server hello-world \n  usa red: hello-local-network \n  IP asignada: 10.0.0.5"
                    }
                }]
            }
        }
    }
}
```

### 4. **server.tf.json** → 5. **Terraform**

**Componente**: Terraform Engine
**Acción**: Aplica la configuración y ejecuta el provisioner.

```bash
terraform init
terraform apply -auto-approve
```

**Resultado**:
```
Server hello-world 
  usa red: hello-local-network 
  IP asignada: 10.0.0.5
```

## Análisis de Interfaz vs Implementación

### **Interfaz** (Contratos)

1. **network_metadata.json**: 
   - **Qué**: Contrato de datos entre red y servidor
   - **Estructura**: `{"name": string, "cidr": string}`
   - **Responsabilidad**: Define qué información expone la red

2. **server.tf.json**:
   - **Qué**: Contrato de configuración para Terraform
   - **Estructura**: Formato JSON válido para Terraform
   - **Responsabilidad**: Define cómo se debe crear el servidor

### **Implementación** (Detalles concretos)

1. **network.tf**:
   - **Qué**: Implementación específica de la red
   - **Detalles**: Uso de `null_resource` y `local_file`
   - **Responsabilidad**: Cómo se crea y expone la información de red

2. **main.py**:
   - **Qué**: Implementación de la lógica de negocio
   - **Detalles**: Cálculo de IPs, lectura de archivos, generación de JSON
   - **Responsabilidad**: Cómo se transforma la información de red en configuración de servidor

3. **Terraform Engine**:
   - **Qué**: Implementación de la orquestación
   - **Detalles**: Ejecución de recursos y provisioners
   - **Responsabilidad**: Cómo se materializan los recursos definidos

## Principios de Inyección de Dependencias Aplicados

### 1. **Desacoplamiento**
- El servidor no conoce la implementación de la red
- Solo conoce el contrato (JSON de metadatos)
- Cambios en `network.tf` no afectan `main.py`

### 2. **Inversión de Dependencias**
- El servidor depende de la abstracción (JSON), no de la implementación (HCL)
- La red implementa la interfaz que el servidor necesita

### 3. **Inyección de Dependencias**
- Los valores de red se "inyectan" en la configuración del servidor
- `main.py` actúa como el "contenedor de inyección"

## Comandos de Ejecución del Flujo

### Paso 1: Provisionar red y metadatos
```bash
cd network
terraform init
terraform apply -auto-approve
```

### Paso 2: Generar configuración del servidor
```bash
cd ..
python main.py
```

### Paso 3: Provisionar servidor
```bash
terraform init
terraform apply -auto-approve
```

## Beneficios de este Flujo

1. **Mantenibilidad**: Cambios en la red se propagan automáticamente
2. **Testabilidad**: Cada componente puede probarse independientemente
3. **Reutilización**: La lógica del servidor puede usarse con diferentes redes
4. **Composabilidad**: Fácil adición de nuevos componentes al flujo

Este flujo demuestra principios sólidos de ingeniería de software aplicados a Infrastructure as Code, creando un sistema modular, mantenible y escalable.