# Actividad 6
# Parte 1: git rebase para mantener un historial lineal
1. **Introducción a Rebase:**
 El rebase mueve tus commits a una nueva base, dándote un historial lineal y limpio. En lugar de fusionar ramas y mostrar un "commit de merge", el rebase integra los cambios aplicándolos en la parte superior de otra rama.
- **Caso de uso**: Simplifica la depuración y facilita la comprensión del historial de commits.
## Escenario del ejemplo
Creación del repositorio de prueba `prueba-git-rebase` dentro de mi carpeta actividad6 localmente.
- Crear archivo `README.md` como primer archivo dentro de la rama master
- Añadir una rama `new-feature` con un archivo `NewFeature.md` que agrega una funcionalidad exclusiva de la rama.
### Visualización del log inicial:
![](imagenes/parte1_b.png)
### **Tarea**: 
Realiza el rebase de `new-feature` sobre `master`:
![](imagenes/parte1_c.png)
### Revisión final:
Con el `rebase` se logra insertar un nuevo commit previo a los cambios realizados en la rama `master` después de la creación de la rama `new-feature`

![](imagenes/parte1_d.png)
# Parte 2: git cherry-pick para la integración selectiva de commit
### Escenario de ejemplo
Creación del repositorio de prueba `prueba-cherry-pick` dentro de mi carpeta actividad6 localmente.
- Se agrega documentación inicial a la rama `master`.
- Se revisa los commits hechos mediante el comando `git log --graph --oneline`
![](imagenes/parte2_a.png)
### **Pregunta:** 
Muestra un diagrama de como se ven las ramas en este paso.

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
**Contexto:**  
Tienes una rama `main` y una rama `feature` en la que trabajas. Durante el desarrollo del sprint, se han realizado commits tanto en `main` como en `feature`.  
**Desarrollo:**
- Crea un repositorio y haz algunos commits en la rama main.
```bash
cd scrum-workflow
# no realizo un git init ya que trabajo desde el repositorio de las actividades
echo "Commit inicial en main" > mainfile.md
git add mainfile.md
git commit -m "Commit inicial en main"
```
- Crea una rama feature, agrega nuevos commits, y luego realiza algunos commits adicionales en main.
```bash
git checkout -b feature
echo "Nueva característica en feature" > featurefile.md
git add featurefile.md
git commit -m "Nueva característica en feature" > featurefile.md

git checkout master
echo "Actualización en main" >> mainfile.md
git add mainfile.md
git commit -m "Actualizar rama main"
```
- Realiza un rebase de feature sobre main.
```bash
git checkout feature
git rebase master
```
- Finalmente, realiza una fusión fast-forward de feature con main.
```bash
git checkout master
# merge del tipo fast forward
git merge --ff feature
```
![](imagenes/ejercicio1_b.png)
#### a. **¿Qué sucede con el historial de commits después del rebase?**
Se fusionó el commit **Actualización en main** en la rama principal
![](imagenes/ejercicio1_c.png)
#### b. **¿En qué situación aplicarías una fusión fast-forward en un proyecto ágil?**
Sería muy útil para proyectos en los que la rama principal no avance mientras se trabajaba en las ramas generadas.
### 2. Cherry-pick para integración selectiva en un pipeline CI/CD
**Contexto:**  
Durante el desarrollo de una funcionalidad, te das cuenta de que solo ciertos cambios deben ser integrados en la rama de producción, ya que el resto aún está en desarrollo. Para evitar fusionar toda la rama, decides hacer cherry-pick de los commits que ya están listos para producción.
**Instrucciones:**
- Crea un repositorio con una rama main y una rama feature.
```bash
cd ci-cd-workflow
# no se realiza git init porque ya estoy en un repositorio
echo "Commit inicial en master" > main.md
git add main.md
git commit -m "Commit inicial en master"
```
- Haz varios commits en la rama feature, pero solo selecciona uno o dos commits específicos que consideres listos para producción.
```bash
git checkout -b feature
echo "Primera característica" > feature1.md
git add feature1.md
git commit -m "Agregar primera característica"

echo "Segunda característica" > feature2.md
git add feature2.md
git commit -m "Agregar segunda característica"
```
- Realiza un cherry-pick de esos commits desde feature a main.
```bash
git log --oneline
# revisar los hashes de cada commit hecho en la rama feature
git checkout master
# Commit con la primera característica
git cherry-pick b6d65b9
# Commit con la segunda característica
git cherry-pick bbbe2cd
```
- Verifica que los commits cherry-picked aparezcan en main.
```bash
git checkout master
git log --oneline --graph
```
![](imagenes/ejercicio2_b.png)
#### a. **¿Cómo utilizarías cherry-pick en un pipeline de CI/CD para mover solo ciertos cambios listos a producción?**
Usaría cherry-pick para casos en los cuales necesito usar ciertas funciones de otra rama que no hayan estado en el momento en que yo creé mi rama. Otra utilidad que le encuentro es cuando al trabajar sobre una rama encuentro un error que otra persona del equipo ya lo arregló en su rama, asi que podría 
#### b. **¿Qué ventajas ofrece cherry-pick en un flujo de trabajo de DevOps?**
con cherry-pick puedes dar uso de commits hechos en diferentes ramas que pueden ayudar a tener funciones agregadas a la rama donde estás trabajando sin necesidad de colocarse en esa rama y hacer varios merges.
# **Git, Scrum y Sprints**
## Ejercicio 1: Crear ramas de funcionalidades (feature branches)
### Crear repositorio, crear rama **main** y dos ramas para usuarios
```bash
# Creación del repositorio
cd scrum-project
echo "# Proyecto Scrum" > README.md
git add README.md
git commit -m "Commit inicial en master

# Creación de ramas a partir de la rama master
git checkout -b feature-user-story-1
git checkout master
git checkout -b feature-user-story-2
```
![](imagenes/ejercicio3_a.png)
### ¿Por qué es importante trabajar en ramas de funcionalidades separadas durante un sprint?
Al cada rama no estar conectada directamente con las demás, cada persona puede avanzar por cada funcionalidad sin necesidad de estar en constante pregunta con su equipo para que sus cambios no hagan conflictos con los demás, además hace tener un trabajo mejor organizado y óptimo para no hacer cambios improvistos que dañen el código a largo plazo.
## Ejercicio 2: Desarrollo del sprint (sprint execution)
### Hacer commits en main y un rebase en una de las ramas creadas
```bash
# Commit nuevo en master
git checkout master
echo "Actualización en master" > updates.md
git add updates.md
git commit -m "Actualizar main con nuevas funciones"

# rebase
git checkout feature-user-story-1
git rebase master
```
### ¿Qué ventajas proporciona el rebase durante el desarrollo de un sprint en términos de integración continua?
Estos rebase son útiles si hay funcionalidad nuevas implementadas en la rama principal y quieres tener esas funcionalidades dentro de la rama de tu trabajo, por lo que puedes implementar estos cambios hechos en los commits posteriores a la creación de tu rama como si fueran cambios puestos antes de que comenzara tu etapa de desarrollo.
## Ejercicio 3: Integración selectiva con `git cherry-pick`
### Realizar cambios en la rama feature-user-story-2 y cherry-pick en main
Realización de cambios en la rama `feature-user-story-2` para tener un progreso respecto al que hay en la rama `master`.
```bash
# Funcionalidad completa
git checkout feature-user-story-2
echo "Funcionalidad lista" > feature2.md
git add feature2.md
git commit -m "Funcionalidad lista para revisión"

# Funcionalidad en progreso
echo "Funcionalidad en progreso" > progres.md
git add progress.md
git commit -m "Crear funcionalidad en progreso"

git log --oneline
# Revisión de hashes para el git cherry-pick
git checkout master
# Añadir función completada a la rama master
git cherry-pick 10ce99f
```
### Validación:
![](imagenes/ejercicio5_a.png)
### ¿Cómo ayuda `git cherry-pick` a mostrar avances de forma selectiva en un sprint review?
al usar `git cherry-pick` puedes tomar uno o varios commits de otras ramas y aplicarla a la que estés trabajando, por lo que puedes implementar avances funcionales y completos a tu rama sin necesidad de conectarte con main u otra rama que tenga otros cambios que puedan provocar un posible conflicto entre archivos.
## Ejercicio 4: Revisión de conflictos y resolución
### Cambios en las subramas de los usuarios para resolver conflictos y hacer un merge exitoso
![](imagenes/ejercicio6_a.png)
### ¿Cómo manejas los conflictos de fusión al final de un sprint? 
Al haber un conflicto de fusión reviso con `nano (archivo)` los posibles conflictos y arreglo manualmente cada uno de los archivos en conflicto para asegurarme que no pase nada a la hora de hacer una fusión con otra rama, como por ejemplo la rama **main**
### ¿Cómo puede el equipo mejorar la comunicación para evitar conflictos grandes?
Haciendo divisiones de un trabajo por ramas que no toquen los mismos archivos, y que no modifiquen partes del código que afecten a las demás partes encargadas del desarrollo del software. Además, la necesidad de hacer commits frecuentes en cada rama para visualizar si algunas funciones están completadas o si falta darles revisiones ayudan a evitar conflictos a gran escala. 
## Ejercicio 5: Automatización de rebase con hooks de Git
### Configurar un hook `pre-push` para un rebase en la rama master y su respectiva prueba.
En este ejercicio crearé un hook `pre-push` que hará lo siguiente:
```bash
git fetch origin main
git rebase origin/main
```
cada que se haga uso del comando `git push`, para añadir archivos al repositorio en github.
Estos hooks ayudan a mantener un código más claro, corrigiendo posibles errores a la hora de utilizar comandos como `git push, git commit, etc...`.
![](imagenes/ejercicio7_b.png)
### ¿Qué ventajas y desventajas observas al automatizar el rebase en un entorno de CI/CD?
El rebase permite evitar commits de fusiones innecesarias, dejando un historial claro y fácil de leer para los demás integrantes del proyecto. También facilita la revisión de cambios con `git log`.
# Navegando conflictos y versionado en un entorno devOps
## Ejemplo:
Primero inicializo el proyecto llamado `proyecto_colaborativo`.
- Mi primer commit tendrá solo al archivo `archivo_colaborativo.txt` donde añadí un texto de ejemplo inicial.
```bash
git init
echo "Este es el contenido inicial del proyecto" > archivo_colaborativo.txt
git add .
git commit -m "Commit inicial con contenido base"
```
Creé una rama llamada `feature-branch` donde modifiqué el archivo anteriormente mencionado, para hacer pruebas de creación de ramas.
```bash
git branch feature-branch
git checkout feature-branch
echo "Este es un cambio en la rama feature-branch" >> archivo_colaborativo.txt
git add .
git commit -m "Cambios en feature-branch"
```
Para este ejemplo haré cambios en la rama **master** para poder entender cómo manejar los conflictos ocasionados a la hora de hacer cualquier tipo de fusión.
```bash
git checkout master
echo "Esto es un cambio en la rama master"
git add .
git commit -m "Cambios en master"
```
### Validación del contenido
![](imagenes/ejercicio8_a.png)
### Fusión y resolución de conflictos
Realización de un `git merge` para visualizar el desarrollo del conflicto en la fusión de las ramas `master` y `feature-branch`.
```bash
git merge feature-branch
# conflicto detectado
git status
# archivos conflictivos
```
### Validación:
![](imagenes/ejercicio8_b.png)
### Simulación de fusiones y uso de git diff
Realización de una simulación de una fusión no fast-forward.
Al solo habler colocado una nueva linea de código en `readme.md` no provocará ningun conflicto
```bash
git checkout feature-branch
echo "Hola a todos" > readme.md
git checkout master
git merge --no-ff feature-branch
```
Al no haber cambios en `cached`, el comando `git diff --cached` no mostrará nada fuera de lo normal
```bash
git diff --cached
# diferencia entre el archivo en feature-branch y master
```
![](imagenes/ejercicio8_c.png)
### Uso de git mergetool
En mi caso usaré **visual studio code** para la resolución de conflictos en mis archivos, ya que ese entorno lo tengo configurado de forma que se me hace mucho más comodo de trabajar.
```
# Configuración global de la herramienta
git config --global merge.tool vscode
# Revisa si hay un archivo en conflicto
git mergetool
```
Herramienta que proporciona tener un entorno global para todo el equipo encargado de trabajar con archivos conflictivos.
## Uso de git revert y git reset
### Prueba con git revert
Primero agregaré un cambio en mi rama **master** para hacer uso de `git_revert`
```bash
echo "Hola" > cont.txt
git add cont.txt
git commit -m "Commit de prueba"
```
mediante un `git log --oneline` revisé los hashes de los commits que llevo hasta ahora y decidí revertir el último commit realizado
```bash
git revert 8cf49d2
# revert realizado
```
Por lo que al revisar `git log --oneline` se podrá ver cómo se crea un nuevo commit que revierte los cambios hechos por el commit pasado.
### Prueba con git reset
Utilicé `git reset --mixed` ya que quiero modificar los cambios que hice antes de mandarlo al estado `staged`, un simple error de contenido en el archivo, haciendo que la documentación no se vea clara. Una vez realizado se vuelve a hacer commit del cambio para mantener limpio mi entorno de trabajo.
```bash
git log --oneline
# Revisar los hashes de los commits hechos
git reset --mixed 8cf49d2
```
Con este `git reset --mixed` pude ir al paso anterior de hacer el commit y poder verificar si están correctos los cambios antes de mandarlo al estado `staged`. Hubiera utilizado `--hard` si el commit desencadenaba algún error con otras ramas o `--soft` si solo quería cambiarle el nombre al commit.
### Validación:
![](imagenes/ejercicio8_e.png)
### Versionado semántico y etiquetado
Para tener un control en las versiones estables de mis proyectos realizo el comando `git tag` para añadirle un tag a esos commits que tienen el proyecto en un buen estado.
```bash
git tag -a v1.0.0 -m "Primera versión estable"
git log --graph --oneline
# visualización del tag en el log
```
### Validación:
![](imagenes/ejercicio8_f.png)
### Aplicación de git bisect para depuración
Para buscar errores en el código del proyecto uso el comando `git bisect` y así no tener que buscar entre cada uno de los commits al error en cuestión.
Un buen comienzo sería denotar un `git bisect good` a la versión estable, marcada con un tag, de la siguiente manera:
```bash
git bisect start
git bisect bad <hash del commit donde se vió un error>
git bisect good 8cf49d2
```
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
```bash
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
