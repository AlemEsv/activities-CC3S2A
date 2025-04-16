# Actividad 6
# Parte 1: git rebase para mantener un historial lineal
## Escenario del ejemplo
![](imagenes/parte1_a.png)
![](imagenes/parte1_b.png)
### **Tarea**: Realiza el rebase de `new-feature` sobre `main` con los siguientes comandos:
![](imagenes/parte1_c.png)
### Revisión final:
![](imagenes/parte1_d.png)
# Parte 2: git cherry-pick para la integración selectiva de commit
### Escenario de ejemplo
![](imagenes/parte2_a.png)
### **Pregunta:** Muestra un diagrama de como se ven las ramas en este paso.
![](imagenes/parte2_b.png)
## **Preguntas de discusión:**
### 1. ¿Por qué se considera que rebase es más útil para mantener un historial de proyecto lineal en comparación con merge? 
uso **rebase** cuando quiero que el historial de cambios se vea más limpio y ordenado. A diferencia de **merge**, que mezcla ramas, **rebase** lo que hace es mover mis cambios como si los hubiera hecho justo después del último commit de la rama `main`. 
### 2. ¿Qué problemas potenciales podrían surgir si haces rebase en una rama compartida con otros miembros del equipo?  
Se podría ocasionar conflictos entre los progresos que tenga cada uno de los integrantes, ocasionando archivos en conflicto dentro de la misma rama, o sobreposición de elementos ya añadidos en la rama.
### 3. ¿En qué se diferencia cherry-pick de merge, y en qué situaciones preferirías uno sobre el otro?  
Utilizo **Cherry-pick** cuando quiero seleccionar y aplicar commits concretos de una rama a otra, sin necesidad de trasladar todo el historial. Mientras que cuando uso **merge** me encargo de integrar todos los commits de una rama en otra, combinando ambos historiales. Por lo que, si busco aplicar cambios puntuales es más adecuado usar **cherry-pick**, mientras que si la intención es unir el trabajo completo de dos ramas, lo recomendable es usar **merge**.
### 4. ¿Por qué es importante evitar hacer rebase en ramas públicas?
Al trabajar con ramas públicas tanto nosotros como los otros miembros del equipo estaríamos trabajando con el historial antiguo, por lo que podría resultar en conflictos al momento de intentar aplicar algún cambio. 
## **Ejercicios teóricos**
### 1. **Diferencias entre git merge y git rebase**  
#### **Explica la diferencia entre git merge y git rebase y describe en qué escenarios sería más adecuado utilizar cada uno en un equipo de desarrollo ágil que sigue las prácticas de Scrum.**
Git merge y git rebase son comandos que permiten integrar cambios de una rama a otra, pero funcionan de manera distinta. Merge une dos ramas y crea un nuevo commit conservando el historial completo de ambas. En cambio, rebase mueve los commits de una rama y los aplica después del último commit de la rama base, reorganizando el historial como si todos los cambios se hubieran hecho en línea recta, lo que lo hace más limpio y fácil de leer. 
En un equipo Scrum, lo mejor sería usar rebase cuando se trabaje en una rama local y se quiera actualizar los cambios antes de hacer un pull request, ya que evita acumulación de commits de fusión. Merge es mejor usarlo cuando ya se han compartido cambios con otros miembros del equipo, para conservar el historial original y mostrar claramente cómo se integraron las diferentes tareas o historias de usuario.
### 2. **Relación entre git rebase y DevOps**  
#### **¿Cómo crees que el uso de git rebase ayuda a mejorar las prácticas de DevOps, especialmente en la implementación continua (CI/CD)? Discute los beneficios de mantener un historial lineal en el contexto de una entrega continua de código y la automatización de pipelines.**
`git rebase` ayuda a DevOps y CI/CD porque permite mantener un historial de commits limpio y lineal, reduce conflictos al integrarse con la rama principal antes de hacer merge, facilita la automatización y depuración en pipelines, mejora la trazabilidad del código, evita errores en despliegues automáticos y promueve una cultura de responsabilidad sobre los cambios
### 3. **Impacto del git cherry-pick en un equipo Scrum**  
#### **Un equipo Scrum ha finalizado un sprint, pero durante la integración final a la rama principal (main) descubren que solo algunos commits específicos de la rama de una funcionalidad deben aplicarse a producción. ¿Cómo podría ayudar git cherry-pick en este caso? Explica los beneficios y posibles complicaciones.**
`git cherry-pick` permite seleccionar commits específicos para aplicarlos en la rama principal, facilitando despliegues controlados en Scrum, evitando introducir código incompleto o no aprobado, aunque puede generar conflictos si los commits dependen de otros cambios no seleccionados.

## ejercicios prácticos
### 1. Simulación de un flujo de trabajo Scrum con git rebase y git merge
![](imagenes/ejercicio1_a.png)
![](imagenes/ejercicio1_b.png)
### Preguntas:
##### **¿Qué sucede con el historial de commits después del rebase?**
Se fusionó el commit **Actualización en main** en la rama principal
![](imagenes/ejercicio1_c.png)
#### **¿En qué situación aplicarías una fusión fast-forward en un proyecto ágil?**
Sería muy útil para proyectos en los que la rama principal no avance mientras se trabajaba en las ramas generadas.
### 2. Cherry-pick para integración selectiva en un pipeline CI/CD
![](imagenes/ejercicio2_a.png)
![](imagenes/ejercicio2_b.png)
### Preguntas:
#### 1. **¿Cómo utilizarías cherry-pick en un pipeline de CI/CD para mover solo ciertos cambios listos a producción?**
Usaría cherry-pick para casos en los cuales necesito usar ciertas funciones de otra rama que no hayan estado en el momento en que yo creé mi rama. Otra utilidad que le encuentro es cuando al trabajar sobre una rama encuentro un error que otra persona del equipo ya lo arregló en su rama, asi que podría 
#### 1. **¿Qué ventajas ofrece cherry-pick en un flujo de trabajo de DevOps?**
con cherry-pick puedes dar uso de commits hechos en diferentes ramas que pueden ayudar a tener funciones agregadas a la rama donde estás trabajando sin necesidad de colocarse en esa rama y hacer varios merges.
# **Git, Scrum y Sprints**
## Ejercicio 1: Crear ramas de funcionalidades (feature branches)
### Crear repositorio, crear rama **main** y dos ramas para usuarios
![](imagenes/ejercicio3_a.png)
### ¿Por qué es importante trabajar en ramas de funcionalidades separadas durante un sprint?
Al cada rama no estar conectada directamente con las demás, cada persona puede avanzar por cada funcionalidad sin necesidad de estar en constante pregunta con su equipo para que sus cambios no hagan conflictos con los demás, además hace tener un trabajo mejor organizado y óptimo para no hacer cambios improvistos que dañen el código a largo plazo.
## Ejercicio 2: Desarrollo del sprint (sprint execution)
### Hacer commits en main y un rebase en una de las ramas creadas
![](imagenes/ejercicio4_a.png)
### ¿Qué ventajas proporciona el rebase durante el desarrollo de un sprint en términos de integración continua?
Estos rebase son útiles si hay funcionalidad nuevas implementadas en la rama principal y quieres tener esas funcionalidades dentro de la rama de tu trabajo, por lo que puedes implementar estos cambios hechos en los commits posteriores a la creación de tu rama como si fueran cambios puestos antes de que comenzara tu etapa de desarrollo.
## Ejercicio 3: Integración selectiva con `git cherry-pick`
### Realizar cambios en la rama feature-user-story-2 y cherry-pick en main
![](imagenes/ejercicio5_a.png)
### ¿Cómo ayuda `git cherry-pick` a mostrar avances de forma selectiva en un sprint review?
al usar `git cherry-pick` puedes tomar uno o varios commits de otras ramas y aplicarla a la que estés trabajando, por lo que puedes implementar avances funcionales y completos a tu rama sin necesidad de conectarte con main u otra rama que tenga otros cambios que puedan provocar un posible conflicto entre archivos.
## Ejercicio 4: Revisión de conflictos y resolución
### Cambios en las subramas de los usuarios para resolver conflictos y hacer un merge exitoso
![](imagenes/ejercicio6_a.png)
![](imagenes/ejercicio6_b.png)
### ¿Cómo manejas los conflictos de fusión al final de un sprint? 
Al haber un conflicto de fusión reviso con `nano (archivo)` los posibles conflictos y arreglo manualmente cada uno de los archivos en conflicto para asegurarme que no pase nada a la hora de hacer una fusión con otra rama, como por ejemplo la rama **main**
### ¿Cómo puede el equipo mejorar la comunicación para evitar conflictos grandes?
Haciendo divisiones de un trabajo por ramas que no toquen los mismos archivos, y que no modifiquen partes del código que afecten a las demás partes encargadas del desarrollo del software. Además, la necesidad de hacer commits frecuentes en cada rama para visualizar si algunas funciones están completadas o si falta darles revisiones ayudan a evitar conflictos a gran escala. 
## Ejercicio 5: Automatización de rebase con hooks de Git
### Configurar un hook `pre-push` para un rebase en la rama master y su respectiva prueba.
![](imagenes/ejercicio7_a.png)
![](imagenes/ejercicio7_b.png)
### ¿Qué ventajas y desventajas observas al automatizar el rebase en un entorno de CI/CD?
El rebase permite evitar commits de fusiones innecesarias, dejando un historial claro y fácil de leer para los demás integrantes del proyecto. También facilita la revisión de cambios con `git log`.
# Navegando conflictos y versionado en un entorno devOps
## Ejemplo:
### Inicialización del proyecto y creación de ramas
![](imagenes/ejercicio8_a.png)
### Fusión y resolución de conflictos
![](imagenes/ejercicio8_b.png)
### Simulación de fusiones y uso de git diff
![](imagenes/ejercicio8_c.png)
### Uso de git mergetool
![](imagenes/ejercicio8_d.png)
### Uso de git revert y git reset
![](imagenes/ejercicio8_e.png)
### Versionado semántico y etiquetado
![](imagenes/ejercicio8_f.png)
### Aplicación de git bisect para depuración
![](imagenes/ejercicio8_g.png)
## Preguntas
### 1. ¿Cómo utilizarías los comandos `git checkout --ours` y `git checkout --theirs` para resolver este conflicto de manera rápida y eficiente? Explica cuándo preferirías usar cada uno de estos comandos y cómo impacta en la pipeline de CI/CD. ¿Cómo te asegurarías de que la resolución elegida no comprometa la calidad del código?
Si inicialmente quise hacer un merge desde main con el equipo B y quiero mantener los cambios sugeridos por ellos usaría `git checkout --ours` para resolver el conflicto manteniendo sus cambios, y en dado caso quiera los cambios del equipo A lo normal sería usar `git checkout --theirs` para guardar sus modificaciones y así no armar un conflicto mayor al hacer que ambos equipos trabajen cambios sobre el mismo archivo con diferentes cambios. 
- Usaría `--ours` cuando confíe en la estabilidad y las pruebas del código en la rama actual.
- Usaría `--theirs` si las correcciones y posibles mejores de la otra rama tienen arreglos más sofisticados y simples de leer.
Haciendo uso de un `git diff` antes de hacer el `commit` podremos observar los cambios exactos que quedaron tras el `--ours o --theirs`
### 2. Utilizando el comando `git diff`, ¿cómo compararías los cambios entre ramas para identificar diferencias específicas en archivos críticos? Explica cómo podrías utilizar `git diff feature-branch..main` para detectar posibles conflictos antes de realizar una fusión y cómo esto contribuye a mantener la estabilidad en un entorno ágil con CI/CD.
Al utilizar  `git diff feature-branch..main` se muestra qué cambios hay en  `main` que no están en la rama `feature-branch`, por lo que uno puede anticipar los posibles conflictos que podría generar un posible futuro merge entre ambas ramas. Por lo que contribuye en la estabilidad del código a futuros merges conflictivos.
### 3. Describe cómo usarías el comando `git merge --no-commit --no-ff` para simular una fusión en tu rama local. ¿Qué ventajas tiene esta práctica en un flujo de trabajo ágil con CI/CD, y cómo ayuda a minimizar errores antes de hacer commits definitivos? ¿Cómo automatizarías este paso dentro de una pipeline CI/CD?
Al usar `git merge --no-commit --no-ff` tenemos como ventaja que si, a la hora de hacer el merge, hay algún conflicto no sea de forma definitiva al no haber realizado el commit automático. Esto muestra que se puede tratar con mejor cuidado los mergeos que se puedan hacer sin necesidad de afectar a las otras ramas.
```
jobs:
  test-merge:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
- name: Obtener ramas
        run: |
          git fetch origin
          git checkout feature-branch
          git merge origin/main --no-commit --no-ff
- name: Ejecutar pruebas
        run: |
          ./run-tests.sh
```
### 4. Explica cómo configurarías y utilizarías `git mergetool` en tu equipo para integrar herramientas gráficas que faciliten la resolución de conflictos. ¿Qué impacto tiene el uso de `git mergetool` en un entorno de trabajo ágil con CI/CD, y cómo aseguras que todos los miembros del equipo mantengan consistencia en las resoluciones?
Primero configuraría el  `git mergetool` con la herramienta gráfica que mejor se acomode a las preferencias generales de la mayoría del equipo de desarrollo. El impacto se da a la hora de trabajar con archivos conflictivos ya que pueden ser resueltas  en un mismo entorno gráfico, aumentando velocidad de integración en sprints con poco tiempo entre ellos, facilidad en colaboración entre desarrolladores por el uso de la herramienta gráfica y una mejor calidad y legibilidad del código.
### 5. Explica las diferencias entre `git reset --soft`, `git reset --mixed` y `git reset --hard`. ¿En qué escenarios dentro de un flujo de trabajo ágil con CI/CD utilizarías cada uno? Describe un caso en el que usarías `git reset --mixed` para corregir un commit sin perder los cambios no commiteados y cómo afecta esto a la pipeline.
Primero, usaría `git reset --soft` cuando necesite hacer cambios al commit sin necesidad de que mis cambios sean borrados, por ejemplo por si no especifiqué bien el mensaje de mi commit.
Para `git reset --mixed` lo necesitaré cuando quiera hacer cambios previos a la entrada al **staging** por si me olvidé agregar un cambio a los archivos modificados antes de hacer el commit.
y por último `git reset --hard` para cuando el cambio que hice no fue el esperado y necesito eliminar todo rastro localmente del cambio y volver a un estado limpio. No creo que sea recomendable su uso tan seguidamente debido a que borra todos los cambios dentro del último commit hecho.
Un escenario posible puede ser a la hora de trabajar durante un sprint y subir parte del código incompleto, rompiendo la pipeline de **CI**. Por lo que haría el `git reset --mixed` para añadir todo el código faltante, realizar las pruebas necesarias y corregir bien cada cambio hech para recién poder realizar bien el commit sin necesidad de empezar todo denuevo como sería si pongo `git reset --hard`
### 6. Explica cómo utilizarías `git revert` para deshacer los cambios sin modificar el historial de commits. ¿Cómo te aseguras de que esta acción no afecte la pipeline de CI/CD y permita una rápida recuperación del sistema? Proporciona un ejemplo detallado de cómo revertirías varios commits consecutivos.
La función que tiene `git revert` es la de aplicar un nuevo commit que deshace los cambios puestos en el último commit hecho en la rama que se esté trabajando, otorgando un historial limpio y sin necesidad de tener que recurrir a un  `git reset --hard`. Esto hace que la pipeline siga funcionando, y no se tenga que usar reseteos o `force push` por parte de los otros integrantes del proyecto.
### 7. Explica cómo utilizarías `git stash` para guardar temporalmente tus cambios y volver a ellos después de haber terminado el hotfix. ¿Qué impacto tiene el uso de `git stash` en un flujo de trabajo ágil con CI/CD cuando trabajas en múltiples tareas? ¿Cómo podrías automatizar el proceso de _stashing_ dentro de una pipeline CI/CD?
Si tengo un cambio a medias en una rama especifica y necesito hacer cambios a otra rama sin tener que hacer un commit de los cambios que tengo actualmente usaría `git stash`
```
git stash push -m "funcionalidad incompleta"
```
para los cambios temporales, y revisaría lo que se necesita en la otra rama.
El uso del `git stash` permite trabajar en diferentes ramas en paralelo sin la necesidad de hacer commits en cada cambio incompleto para poder pasar entre ramas y que tu progreso no se elimine 
```
git stash push -m "temporal"
git checkout hotfix-temporal
# ...acciones...
git stash pop
```
### 8. Diseña un archivo `.gitignore` que excluya archivos innecesarios en un entorno ágil de desarrollo. Explica por qué es importante mantener este archivo actualizado en un equipo colaborativo que utiliza CI/CD y cómo afecta la calidad y limpieza del código compartido en el repositorio.
En un proyecto ágil, los desarrolladores usan entornos distintos para el trabajo, generando logs, configuraciones locales y archivos temporales que no deberían llegar al repositorio.
```
# Entorno que usen los desarrolladores
.vscode/
.idea/
# Archivos temporales
*.temp
*.tmp
*.log
# Entornos virtuales
venv/
.env/
# Configuraciones locales
*.env
secrets.json
```
Esto mantiene el repositorio limpio de configuraciones locales y posibles archivos que pueden hacer conflictos a la hora de probarlos en otros equipos con diferentes configuraciones, reduce el tamaño del repositorio y facilita la colaboración continua.
