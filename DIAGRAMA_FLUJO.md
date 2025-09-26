# Diagrama de Flujo del Proyecto

## Flujo General del Sistema

```mermaid
graph TD
    A[Actividad 20: IaC Básico] --> B[Actividad 21: Patrones de Diseño]
    B --> C[Actividad 22: Dependencias y Módulos]
    
    subgraph "Actividad 20"
        D[main.py] --> E[main.tf.json]
        E --> F[Terraform Apply]
        F --> G[Recursos Locales]
    end
    
    subgraph "Actividad 21"
        H[Singleton] --> I[Factory]
        I --> J[Prototype]
        J --> K[Builder]
        K --> L[Composite]
        L --> M[Infrastructure JSON]
    end
    
    subgraph "Actividad 22"
        N[Network Module] --> O[Metadata JSON]
        O --> P[Server Generator]
        P --> Q[Server Config]
        Q --> R[Final Infrastructure]
    end
```

## Flujo Detallado - Inyección de Dependencias (Actividad 22)

```mermaid
sequenceDiagram
    participant N as network.tf
    participant M as network_metadata.json
    participant P as main.py
    participant S as server.tf.json
    participant T as Terraform

    Note over N,T: Fase 1: Provisionar Red
    N->>M: terraform apply
    Note right of M: {"name": "hello-local-network", "cidr": "10.0.0.0/28"}
    
    Note over N,T: Fase 2: Generar Servidor
    P->>M: Lee metadatos
    M-->>P: Devuelve name y cidr
    P->>P: Calcula IP (10.0.0.5)
    P->>S: Genera configuración
    Note right of S: Triggers: name, subnetwork, network_ip
    
    Note over N,T: Fase 3: Provisionar Servidor
    T->>S: terraform apply
    S-->>T: Ejecuta local-exec
    T->>T: Muestra: "Server hello-world usa red: hello-local-network IP: 10.0.0.5"
```

## Arquitectura de Patrones (Actividad 21)

```mermaid
classDiagram
    class ConfigSingleton {
        -instance: ConfigSingleton
        +getInstance(): ConfigSingleton
        +getConfig(): Dict
    }
    
    class NullResourceFactory {
        +create(name, triggers): Dict
        +createTimestamped(name, triggers, fmt): Dict
    }
    
    class ResourcePrototype {
        -data: Dict
        +clone(mutator): ResourcePrototype
    }
    
    class CompositeModule {
        -children: List
        +add(resource): void
        +export(): Dict
    }
    
    class InfrastructureBuilder {
        -env_name: str
        -module: CompositeModule
        +build_null_fleet(count): InfrastructureBuilder
        +add_custom_resource(name, triggers): InfrastructureBuilder
        +export(path): void
    }
    
    InfrastructureBuilder --> CompositeModule
    InfrastructureBuilder --> NullResourceFactory
    InfrastructureBuilder --> ResourcePrototype
    CompositeModule --> NullResourceFactory
```

## Flujo de Datos - Patrones de Dependencias

```mermaid
graph LR
    subgraph "Inyección de Dependencias"
        A1[network.tf] --> B1[network_metadata.json]
        B1 --> C1[main.py]
        C1 --> D1[server.tf.json]
        D1 --> E1[Terraform]
    end
    
    subgraph "Inversión de Control"
        A2[network.tf.json] --> B2[network_outputs.json]
        B2 --> C2[main.py]
        C2 --> D2[main.tf.json]
        D2 --> E2[Terraform]
    end
    
    subgraph "Interfaces vs Implementaciones"
        F[Interfaz: JSON Files] --> G[Implementación: Terraform HCL]
        H[Interfaz: Python Classes] --> I[Implementación: Terraform Resources]
    end
```

## Ciclo de Vida del Recurso

```mermaid
stateDiagram-v2
    [*] --> Diseño
    Diseño --> Generación: Python Script
    Generación --> Validación: JSON Schema
    Validación --> Aplicación: terraform apply
    Aplicación --> Monitoreo: Recursos Activos
    Monitoreo --> Modificación: Cambios Requeridos
    Modificación --> Generación: Regenerar Config
    Monitoreo --> Destrucción: terraform destroy
    Destrucción --> [*]
    
    state Generación {
        [*] --> Factory
        Factory --> Prototype
        Prototype --> Builder
        Builder --> Composite
        Composite --> [*]
    }
```

## Patrón de Comunicación entre Módulos

```mermaid
graph TB
    subgraph "Módulo de Red"
        N1[Network Resource] --> N2[Local File Output]
        N2 --> N3[network_metadata.json]
    end
    
    subgraph "Módulo de Servidor"
        S1[Python Script] --> S2[Lee Metadatos]
        S2 --> S3[Calcula IP]
        S3 --> S4[Genera Config]
        S4 --> S5[server.tf.json]
    end
    
    subgraph "Terraform Engine"
        T1[Terraform Plan] --> T2[Terraform Apply]
        T2 --> T3[Local Exec]
        T3 --> T4[Output Display]
    end
    
    N3 --> S2
    S5 --> T1
    
    style N1 fill:#e1f5fe
    style S1 fill:#f3e5f5
    style T1 fill:#e8f5e8
```

## Matriz de Responsabilidades

| Componente | Responsabilidad | Entrada | Salida |
|------------|----------------|---------|--------|
| **network.tf** | Definir infraestructura de red | Variables Terraform | network_metadata.json |
| **main.py** | Lógica de negocio | network_metadata.json | server.tf.json |
| **server.tf.json** | Configuración del servidor | Triggers generados | Recursos Terraform |
| **Terraform** | Orquestación | Archivos .tf/.tf.json | Infraestructura real |
| **Factory** | Creación de recursos | Parámetros | Configuración JSON |
| **Builder** | Composición fluida | Configuraciones | Módulo completo |
| **Composite** | Agrupación | Recursos individuales | Módulo agrupado |

## Flujo de Validación y Testing

```mermaid
graph TD
    A[Código Fuente] --> B{Validación Sintáctica}
    B -->|✓| C[Tests Unitarios]
    B -->|✗| A
    C --> D{Tests de Integración}
    D -->|✓| E[Terraform Plan]
    D -->|✗| A
    E --> F{Validación Plan}
    F -->|✓| G[Terraform Apply]
    F -->|✗| A
    G --> H[Verificación Post-Deploy]
    H --> I[Infraestructura Lista]
    
    style A fill:#ffeb3b
    style I fill:#4caf50
    style B fill:#2196f3
    style D fill:#2196f3
    style F fill:#2196f3
```

Esta documentación visual complementa el flujo textual y proporciona una comprensión clara de la arquitectura y los flujos de datos del proyecto.