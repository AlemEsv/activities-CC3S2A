# Flujo del Proyecto - Activities CC3S2A

## Descripción General

Este proyecto implementa **Infrastructure as Code (IaC)** usando **Terraform** y **Python**, aplicando patrones de diseño de software para gestionar infraestructura de manera local. El proyecto está organizado en actividades progresivas que demuestran diferentes patrones y enfoques.

## Arquitectura General del Proyecto

```
activities-CC3S2A/
├── actividades/
│   ├── actividad20/     # IaC Orquestador Local
│   ├── actividad21/     # Patrones de Diseño en IaC
│   └── actividad22/     # Patrones de Dependencias y Módulos
└── README.md
```

## Flujo Principal por Actividades

### 📋 Actividad 20: IaC Orquestador Local

**Objetivo**: Introducción a Infrastructure as Code usando Terraform con recursos locales.

**Flujo de Datos**:
```
Python Script (main.py) → JSON Config (main.tf.json) → Terraform → Recursos Locales
```

**Componentes**:
1. **`main.py`**: Genera configuración Terraform en formato JSON
2. **`main.tf.json`**: Configuración de recursos `null_resource` para simular infraestructura
3. **Terraform**: Aplica la configuración y ejecuta comandos locales

**Proceso**:
1. Ejecutar `python main.py` genera `main.tf.json`
2. Ejecutar `terraform apply` crea recursos simulados
3. Los recursos ejecutan comandos locales usando `local-exec`

### 🏗️ Actividad 21: Patrones de Diseño en IaC

**Objetivo**: Implementar patrones de diseño clásicos adaptados para IaC.

**Patrones Implementados**:

#### 1. **Singleton** (`singleton.py`)
- Gestiona configuración global única
- Evita duplicación de configuraciones

#### 2. **Factory** (`factory.py`)
- Crea recursos `null_resource` de manera estandarizada
- Genera triggers únicos (UUID + timestamp)

#### 3. **Prototype** (`prototype.py`)
- Clona recursos existentes
- Permite mutaciones personalizadas

#### 4. **Builder** (`builder.py`)
- Construye infraestructura de manera fluida
- Combina Factory, Prototype y Composite

#### 5. **Composite** (`composite.py`)
- Agrupa múltiples recursos en módulos
- Estructura jerárquica de configuraciones

**Flujo de Construcción**:
```python
# Ejemplo de uso del Builder
builder = InfrastructureBuilder(env_name="demo")
builder.build_null_fleet(count=3)
builder.export(path="terraform/main.tf.json")
```

### 🔄 Actividad 22: Patrones de Dependencias y Módulos

**Objetivo**: Implementar inyección de dependencias e inversión de control en IaC.

#### Subcarpeta: Inyección de Dependencias

**Flujo de Datos Completo**:
```
network.tf → network_metadata.json → main.py → server.tf.json → Terraform
```

**Proceso Detallado**:

1. **Provisionar Red** (`network/network.tf`):
   ```bash
   cd network
   terraform init
   terraform apply -auto-approve
   ```
   - **Salida**: `network_metadata.json` con `{"name": "hello-local-network", "cidr": "10.0.0.0/28"}`

2. **Generar Configuración del Servidor** (`main.py`):
   ```bash
   cd ..
   python main.py
   ```
   - Lee `network_metadata.json`
   - Calcula IP (quinta dirección del rango CIDR)
   - **Salida**: `server.tf.json` con triggers `name`, `subnetwork`, `network_ip`

3. **Provisionar Servidor**:
   ```bash
   terraform init
   terraform apply -auto-approve
   ```
   - Ejecuta `local-exec` mostrando configuración del servidor

#### Subcarpeta: Inversión de Control

**Flujo Modificado**:
```
network.tf.json → network_outputs.json → main.py → main.tf.json → Terraform
```

**Diferencias Clave**:
- La red expone **outputs** en lugar de metadatos
- El servidor consume estos outputs como **inputs**
- Implementa el patrón de Inversión de Control

## Patrones de Diseño Aplicados

### 1. **Inyección de Dependencias**
- **Interfaz**: Archivo JSON con metadatos de red
- **Implementación**: Configuración específica de red en Terraform
- **Beneficio**: Desacoplamiento entre componentes

### 2. **Inversión de Control**
- La red define qué expone (outputs)
- El servidor consume lo que necesita
- Control invertido desde el consumidor hacia el proveedor

### 3. **Factory Pattern**
- Creación estandarizada de recursos
- Generación automática de identificadores únicos

### 4. **Builder Pattern**
- Construcción fluida de infraestructura compleja
- Combinación de múltiples patrones

### 5. **Composite Pattern**
- Agrupación jerárquica de recursos
- Tratamiento uniforme de recursos individuales y grupos

## Flujo de Validación y Testing

### Validaciones Implementadas

1. **Validación de CIDR**:
   - Verificar que el rango CIDR sea válido
   - Asegurar que contenga al menos 5 hosts

2. **Validación de Metadatos**:
   - Verificar campos obligatorios (`name`, `cidr`)
   - Validación de tipos de datos

3. **Tests Automatizados**:
   - Tests unitarios con `pytest`
   - Validación de estructura JSON generada
   - Tests de integración para flujos completos

## Herramientas y Tecnologías

### Stack Principal
- **Terraform**: Orquestación de infraestructura
- **Python**: Lógica de negocio y generación de configuraciones
- **JSON**: Formato de intercambio de datos y configuración

### Proveedores Terraform Utilizados
- **null**: Para recursos de prueba y simulación
- **local**: Para archivos y comandos locales

### Bibliotecas Python
- **json**: Manipulación de configuraciones
- **ipaddress**: Cálculos de red y direcciones IP
- **uuid**: Generación de identificadores únicos
- **datetime**: Timestamps para triggers

## Casos de Uso y Aplicaciones

### 1. **Desarrollo Local**
- Simulación de infraestructura sin recursos reales
- Pruebas de configuraciones antes del despliegue

### 2. **Prototipado**
- Validación de arquitecturas
- Experimentación con configuraciones

### 3. **Educación**
- Aprendizaje de patrones de diseño
- Comprensión de IaC sin costos de nube

### 4. **CI/CD**
- Validación automática de configuraciones
- Tests de infraestructura en pipelines

## Beneficios del Enfoque

### 1. **Desacoplamiento**
- Separación clara entre componentes
- Interfaces bien definidas

### 2. **Reutilización**
- Patrones aplicables a diferentes contextos
- Componentes modulares

### 3. **Mantenibilidad**
- Código organizado y estructurado
- Fácil modificación y extensión

### 4. **Testabilidad**
- Componentes aislados fáciles de probar
- Validaciones automatizadas

## Evolución del Proyecto

### Progresión de Complejidad

1. **Actividad 20**: Conceptos básicos de IaC
2. **Actividad 21**: Aplicación de patrones de diseño
3. **Actividad 22**: Patrones avanzados de dependencias

### Próximos Pasos Sugeridos

1. **Integración con Proveedores Reales**
   - AWS, GCP, Azure
   - Recursos de infraestructura real

2. **Automatización Avanzada**
   - GitHub Actions
   - Makefile para automatización

3. **Validaciones Externas**
   - Key-Value stores (Consul, Vault)
   - APIs REST para configuración

4. **Monitoreo y Observabilidad**
   - Logs estructurados
   - Métricas de infraestructura

## Conclusión

Este proyecto demuestra cómo aplicar principios de ingeniería de software a Infrastructure as Code, creando un flujo robusto, mantenible y escalable para gestión de infraestructura. La progresión desde conceptos básicos hasta patrones avanzados proporciona una base sólida para proyectos de IaC más complejos.