### Actividad: **Migrando a Microservicios: Docker, Kubernetes y CI/CD**

#### Escenario general

Tu equipo está desarrollando dos microservicios en Python (Users y Orders) que forman el núcleo de una plataforma de pedidos en línea. Quieres:

* Asegurar builds reproducibles y rápidos.
* Desplegar en un entorno local para pruebas de integración continua (CI).
* Evolucionar a un clúster de Kubernetes administrado en producción.
* Automatizar tests, builds y despliegues con GitHub Actions.

>Utiliza como referencia el siguiente repositorio: [Microservicios, Kubernetes y Github Actions](https://github.com/kapumota/DS/tree/main/2025-1/microservices-k8s)

#### A. Docker y Docker Compose

**Contexto:** Al empaquetar tus servicios, debe primar la consistencia entre entornos (dev, staging, prod) y minimizar el tiempo de despliegue.

1. **Arquitectura de contenedores**

   * Explica cómo un contenedor encapsula la aplicación y sus dependencias. ¿Qué ventajas ofrece frente a una VM en términos de arranque, consumo de recursos y portabilidad?
   * En tu proyecto, ¿qué pasos ocurren al ejecutar `docker build -t user-service .` y por qué cada uno es crítico para garantizar una imagen fiable?

2. **Optimización de Dockerfile**

   * Analiza el `Dockerfile` de `service-user` y(diagrama de capas) justifica el orden de instrucciones.
   * Propón optimizaciones (por ejemplo, combinar instrucciones RUN, usar imágenes base más ligeras) y detalla cómo mejorarían el tiempo de build o el tamaño de imagen.

3. **Redes y volúmenes en un entorno real**

   * Si tu microservicio necesitara persistir sesiones o logs de auditoría, ¿cómo montarías un volumen Docker?
   * En producción, ¿qué tipo de red usarías para comunicar los servicios `user` y `order` si estuviesen en distintos hosts, y por qué?

4. **Docker Compose para entornos de desarrollo**

   * Diseña un `docker-compose.yml` que arranque:

     * `service-user` y `service-order`.
     * Una base de datos Redis para gestionar caché de sesión.
     * Un contenedor de administración (por ejemplo, phpMyAdmin o RedisInsight).
   * Explica cómo Compose acelera el onboarding de nuevos desarrolladores y facilita simular entornos de staging locales.

#### B. Infraestructura como Código (IaC)

**Contexto:** En tu pipeline CI/CD quieres tratar los manifiestos de Kubernetes igual que el código: revisión por pull request, versionado, validación automática.

5. **Principios de IaC**

   * Define IaC y enumera sus tres beneficios principales (reproducibilidad, trazabilidad, rollback).
   * Compara un script Bash que ejecute `kubectl apply` (imperativo) con un manifiesto YAML que describa un Deployment (declarativo). ¿Qué control de versiones y auditoría permite cada enfoque?

6. **Manifiestos Kubernetes como código fuente**

   * En el directorio `k8s/`, identifica en cada YAML:

     * El tipo de objeto (`Deployment`, `Service`) y su propósito.
     * El selector de pods y la configuración de puertos.
   * ¿Cómo encajarías estos archivos en tu flujo de GitFlow para asegurar revisiones de infraestructura antes de merge?

7. **Parametrización y reutilización**

   * Diseña un `ConfigMap` o `Secret` para extraer la URL de una base de datos PostgreSQL, de modo que puedas reutilizar el mismo Deployment en staging y producción cambiando sólo valores.
   * Explica brevemente cómo Helm o Kustomize automatizarían la generación de estos manifiestos según variables de entorno o valores por entorno.


#### C. Fundamentos de Kubernetes

**Contexto:** En producción, la plataforma correrá en un clúster gestionado que debe escalar automáticamente y recuperarse de fallos.

8. **¿Por qué Kubernetes?**

   * Imagina que aumentas el tráfico en un 10× durante una campaña de Black Friday. ¿Cómo ayudaría Kubernetes frente a un orquestador casero hecho con scripts?
   * Compara rápidamente Kubernetes con Docker Swarm en cuanto a ecosistema, escalabilidad y extensibilidad.

9. **Modelado de la arquitectura**

   * Dibujarás un diagrama con al menos un nodo (VM), varias réplicas de Pods y dentro de cada Pod dos containers (uno de aplicación y otro sidecar de logging).
   * Explica cómo las probes (liveness/readiness) garantizan que el tráfico no llegue a Pods no preparados o con problemas.

10. **Estrategias de despliegue**

    * Describe el objeto `Deployment`, su historia de revisiones (`RevisionHistoryLimit`) y las estrategias de rollout (`RollingUpdate` vs `Recreate`).
    * Explica cuándo usar `ClusterIP`, `NodePort` o `LoadBalancer` para exponer cada uno de tus servicios y su impacto en entornos on-premise vs nube pública.


#### D. Kubernetes – Entorno local con Minikube

**Contexto:** Antes de integrar con el clúster real, tu pipeline de CI debe validar despliegues en un entorno local idéntico (lo más posible) al de producción.

11. **Instalación del CLI**

    * Detalla los pasos para instalar `kubectl` en tu SO preferido y cómo configurar el autocompletado.
    * Comenta los comandos `kubectl version`, `kubectl config view` y qué información esencial devuelven.

**Instalación en Windows:**

```bash
# Instalar kubectl con Chocolatey
choco install kubernetes-cli

minikube docker minikube docker-env | Invoke-Expression
```

**Comandos esenciales:**
```bash
# Verificar versión cliente/servidor
kubectl version --client

# Ver configuración actual
kubectl config view
```

**Información que devuelven:**
* `kubectl version`: Versión del cliente kubectl y del servidor Kubernetes
* `kubectl config view`: Contextos, clusters, usuarios configurados y cluster actual

12. **Arranque de Minikube**

    * Explica qué sucede al lanzar `minikube start --driver=docker`: creación de VM, adaptación de red, instalación de kube-apiserver.
    * Compara Minikube con Kind en cuanto a facilidad de integración en CI y recursos requeridos.

**Solución:**

**Proceso de `minikube start --driver=docker`:**

1. **Creación del contenedor:** Crea un contenedor Docker que actúa como nodo 
2. **Configuración de red:** Establece networking entre el host y el contenedor
3. **Instalación de componentes:** Instala kube-apiserver, etcd, kubelet, kube-proxy
4. **Configuración de kubectl:** Actualiza el contexto para apuntar al cluster local

```bash
minikube start --driver=docker --cpus=2 --memory=4096
```

**Comparación Minikube vs Kind:**

| Aspecto | Minikube | Kind |
|---------|----------|------|
| **CI Integration** | Moderada | Excelente |
| **Recursos** | 2GB RAM | 1GB RAM |
| **Velocidad inicio** | 2-3 min | 30-60 seg |

Kind para CI/CD, Minikube para desarrollo local.

13. **Script de despliegue local**

    * Desglosa el script `minikube-setup.sh` en secciones: inicialización, build de imágenes, despliegue de manifests.
    * ¿Qué ventajas y limitaciones tiene esta aproximación para pruebas de integración automática en GitHub Actions?

**Solución:**

**Script `minikube-setup.sh` desglosado:**

```bash
#!/bin/bash

# 1. INICIALIZACIÓN
echo "Iniciando Minikube..."
minikube start --driver=docker --cpus=2 --memory=4096
eval $(minikube docker-env)  # Usar Docker daemon de Minikube

# 2. BUILD DE IMÁGENES
echo "Construyendo imágenes..."
docker build -t user-service:latest ./service-user
docker build -t order-service:latest ./service-order

# 3. DESPLIEGUE DE MANIFESTS
echo "Desplegando servicios..."
kubectl apply -f k8s/user-service.yaml
kubectl apply -f k8s/order-service.yaml

# 4. VERIFICACIÓN
kubectl wait --for=condition=available --timeout=300s deployment/user-service
kubectl get pods
```

**Ventajas en GitHub Actions:**
* Entorno reproducible
* Testing de manifiestos reales
* Validación de integración entre servicios

**Limitaciones:**
* Tiempo de setup (~3-5 min)
* Recursos limitados en runners
* No simula completamente producción

14. **Limpieza y recuperación**

    * Indica cómo listar y eliminar los recursos de Kubernetes creados (`kubectl get all`, `kubectl delete namespace`).
    * En caso de fallo de un Deployment, ¿qué pasos seguirías para recuperar el servicio sin downtime?

**Solución:**

**Comandos de limpieza:**

```bash
# Listar todos los recursos
kubectl get all

# Eliminar deployment específico
kubectl delete deployment user-service

# Eliminar todo en el namespace default
kubectl delete all --all
```

**Recuperación sin downtime:**

1. **Diagnóstico rápido:**
```bash
kubectl get pods
kubectl describe pod <pod-name>
kubectl logs <pod-name>
```

2. **Rollback inmediato:**
```bash
kubectl rollout undo deployment/user-service
kubectl rollout status deployment/user-service
```

3. **Escalado temporal:**
```bash
kubectl scale deployment user-service --replicas=5
```

4. **Verificación:**
```bash
kubectl get endpoints user-service
curl http://service-url/health
```

**Estrategia de recuperación:**
* Mantener siempre >1 réplica
* Usar readiness probes
* Implementar circuit breakers
* Monitorear métricas clave


#### E. CI/CD con GitHub Actions

**Contexto:** El objetivo es lograr una pipeline end-to-end que valide código, construya imágenes y despliegue a Minikube (y más adelante a producción) sin intervención manual.

15. **Anatomía del workflow**

    * Describe cada sección de `.github/workflows/ci-cd.yaml`: disparadores (`on`), jobs, steps y acciones usadas.
    * ¿Cómo encajarías una etapa adicional de tests unitarios y de integración antes de la etapa de build?

16. **Acciones Docker y kubectl**

    * ¿Por qué se emplea `docker/setup-buildx-action`? Explica qué es Buildx.
    * En el contexto de un runner de Actions, ¿por qué `push: false` y cómo modificas el workflow para empujar imágenes a Docker Hub o un registry corporativo?

17. **Despliegue remoto**

    * Si migras a EKS/GKE en AWS/GCP, ¿qué credenciales y pasos cambiarían en tu workflow para autenticar `kubectl` y proteger secretos?
    * Propón una estrategia para usar `environments` de GitHub y aprobar despliegues a staging/producción manualmente.

#### F. Preparación para producción

**Contexto:** Tras validar todo localmente y en staging, debes diseñar cómo llevarlo a tu clúster de producción con seguridad, observabilidad y cero downtime.

18. **Canary y Blue-Green**

    * Diseña un manifiesto para hacer un despliegue canary de tu `user-service`.

    Un despliegue canary permite liberar una nueva versión gradualmente, dirigiendo solo un pequeño porcentaje del tráfico a la nueva versión mientras se monitorea su comportamiento.

    **Despliegue canary:**

    ```yaml
    # Versión estable (3 réplicas)
    apiVersion: apps/v1
    kind: Deployment
    metadata:
    name: user-service-stable
    spec:
    replicas: 3
    selector:
        matchLabels:
        app: user-service
        version: stable
    template:
        metadata:
        labels:
            app: user-service
            version: stable
        spec:
        containers:
        - name: user-service
            image: user-service:v1.0.0
            ports:
            - containerPort: 8000

    ---
    # Versión canary (1 réplica)
    apiVersion: apps/v1
    kind: Deployment
    metadata:
    name: user-service-canary
    spec:
    replicas: 1
    selector:
        matchLabels:
        app: user-service
        version: canary
    template:
        metadata:
        labels:
            app: user-service
            version: canary
        spec:
        containers:
        - name: user-service
            image: user-service:v2.0.0
            ports:
            - containerPort: 8000

    ---
    # Service común
    apiVersion: v1
    kind: Service
    metadata:
    name: user-service
    spec:
    selector:
        app: user-service
    ports:
    - port: 80
        targetPort: 8000
    ```

    **Estrategia de despliegue canary:**

    1. **Desplegar canary:**
    ```bash
    kubectl apply -f canary.yaml
    ```

    2. **Monitorear métricas:**
    * Error rate < 1%
    * Latencia normal
    * Sin errores en logs

    3. **Escalar canary (si todo va bien):**
    ```bash
    kubectl scale deployment user-service-canary --replicas=2
    ```

    4. **Rollback (si hay problemas):**
    ```bash
    kubectl delete deployment user-service-canary
    ```

19. **Seguridad en contenedores**

    * Menciona tres buenas prácticas: escanear imágenes (Clair, Trivy), mínima base (`distroless`, **scratch**), políticas de PSP/OPA Gatekeeper.

20. **Monitoreo y logs**

    * Propón un stack basado en Prometheus, Grafana y ELK/EFK para métricas y logs de tus microservicios. Explica cómo integrar un sidecar de Fluentd o Filebeat.

