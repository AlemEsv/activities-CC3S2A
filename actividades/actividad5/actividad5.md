# Explorando diferentes formas de fusionar en Git
# Parte teórica sobre las formas de Fusión
# Fusión Fast-forward
La fusión Fast-Forward 
### a. Pasos prácticos: 
![](imagenes/pasos_practicos-FastForward.png)
### b. Mostrar la estructura de commits resultante
![](imagenes/pregunta-FastForward.png)
# Fusión No-Fast-forward
### a. Pasos prácticos
![](imagenes/pasos_practicos-NoFastForward.png)
### b. Muestra el log de commits resultante
![](imagenes/pregunta1-NoFastForward.png)
![](imagenes/pregunta2-NoFastForward.png)
# Fusión squash
### a. Pasos prácticos
![](imagenes/pasos_practicos-Squash.png)
### b. ¿Cuál es la estructura de commits?
![](imagenes/pregunta-Squash.png)
# Ejercicios
### 1. Resolver conflictos en una fusión non-fast-forward
a. Inicializar el repositorio
![](imagenes/ejercicio1_a.png)
#### b. Crea archivo index.html y hacer el commit de este en main
![](imagenes/ejercicio1_b.png)

#### c. Cambio de rama y actualización a index.html
![](imagenes/ejercicio1_c.png)

#### d. Regreso a la rama main y actualizo desde ahí a index.html
![](imagenes/ejercicio1_d.png)

#### e. Fusión de la rama feature-update con --no-ff
![](imagenes/ejercicio1_e.png)

#### f. Al intentar hacer la fusión habrá un conflicto, asi que toca actualizar index.html.
![](imagenes/ejercicio1_f.png)

#### g. Una vez se arregla el conflicto se guarda y se termina el mergeo.
![](imagenes/ejercicio1_g.png)

![](imagenes/ejercicio1_h.png)

#### h. Revisión en el historial.
![](imagenes/ejercicio1_i.png)

### Preguntas 1
#### ¿Qué pasos adicionales tuviste que tomar para resolver el conflicto?
Entré con ayuda de nano al "index.html" para resolver el conflicto, vi que habían 2 versiones distintas para el mismo archivo asi que intenté acoplar las dos versiones en un mismo "index.html", borrando los "==== " y las cabeceras "HEAD" y "feature-update" en ambos casos.

#### ¿Qué estrategias podrías emplear para evitar conflictos en futuros desarrollos?
Para futuros trabajos se puede emplear squash para el caso de añadir código nuevo al "index.html", ya que solo se colocaría en una línea de texto posterior a la que ya se tiene inicialmente, por lo que no existirían problemas de mergeo

### 2. Comparar los historiales con git log después de diferentes fusiones

![](imagenes/ejercicio2_a.png)

![](imagenes/ejercicio2_b.png)

![](imagenes/ejercicio2_c.png)

![](imagenes/ejercicio2_d.png)
#### Antes de solucionar el conflicto
![](imagenes/ejercicio2_e.png)
#### Después de solucionar el conflicto
![](imagenes/ejercicio2_f.png)

![](imagenes/ejercicio2_g.png)

![](imagenes/ejercicio2_h.png)

![](imagenes/ejercicio2_i.png)
![](imagenes/ejercicio2_j.png)

![](imagenes/ejercicio2_k.png)
### Preguntas 2:
#### ¿Cómo se ve el historial en cada tipo de fusión?

#### ¿Qué método prefieres en diferentes escenarios y por qué?

### 3. Usando fusiones automáticas y revertir fusiones
#### Inicializa un repositorio y realiza dos commits en **main**
![](imagenes/ejercicio3_a.png)
#### Creación de la rama **auto-merge** y commit en **file.txt**
![](imagenes/ejercicio3_b.png)
![](imagenes/ejercicio3_c.png)
#### Se vuelve a la rama **master** y se realiza cambios en **file.txt** no conflictivos.
![](imagenes/ejercicio3_d.png)
#### Fusión de la rama **auto-merge** con **master**
![](imagenes/ejercicio3_e.png)
#### Revisión después de usar **git revert** para revertir commits.
![](imagenes/ejercicio3_f.png)

![](imagenes/ejercicio3_g.png)
#### Verificación del historial
![](imagenes/ejercicio3_h.png)

### Preguntas 3:
#### ¿Cuándo usarías un comando como git revert para deshacer una fusión?
Cuando haga cambios incompletos, o que el cambio provoque algún conflicto en la lógica del proyecto. Quizás el cambio empeore el código y se necesita hacer un revert al commit.
### ¿Qué tan útil es la función de fusión automática en Git?
Sirve mucho para no tener que revisar manualmente todas las fusiones que hagamos como desarrolladores, optimizando el tiempo revisando código. Más que nada cuando se hagan cambios que agreguen más código o modifiquen código en líneas ya existentes.



