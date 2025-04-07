# Explorando diferentes formas de fusionar en Git
# Fusión Fast-forward

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

#### a. Inicializar el repositorio
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

