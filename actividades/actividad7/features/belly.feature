# language: es

Característica: Comportamiento del Estómago

# Funcionalidad: Soporte de escenario simple para tiempo en segundos
Escenario: Comer pepinos y esperar en minutos y segundos
  Dado que he comido 35 pepinos
  Cuando espero "1 hora y 30 minutos y 45 segundos"
  Entonces mi estómago debería gruñir

# Funcionalidad: Soporte de escenario con tiempo fraccionario
Escenario: Comer una cantidad fraccionaria de pepinos
  Dado que he comido 0.5 pepinos
  Cuando espero 2 horas
  Entonces mi estómago no debería gruñir

# Funcionalidad: Soporte para idioma inglés
Escenario: Esperar usando horas en inglés
  Dado que he comido 20 pepinos
  Cuando espero "two hours and thirty minutes"
  Entonces mi estómago debería gruñir

Escenario: Comer 5 pepinos en 3 horas y 20 minutos
  Dado que he comido 5 pepinos
  Cuando espero "three hours and twenty minutes"
  Entonces mi estómago no debería gruñir

# Funcionalidad nueva: Comer pepinos en un tiemp aleatorio entre dos horas
Escenario: Comer pepinos y esperar un tiempo aleatorio
  Dado que he comido 25 pepinos
  Cuando espero un tiempo aleatorio entre 1 y 3 horas
  Entonces mi estómago debería gruñir

# Funcionalidad: Saltar una excepción cuando se pruebe con valores negativos
#Escenario: Manejar una cantidad no válida de pepinos
#  Dado que he comido -5 pepinos
#  Entonces debería ocurrir un error de cantidad negativa.

# Funcionalidad: Escalabilidad cuando se pruebe con valores muy grandes
Escenario: Comer 1000 pepinos y esperar 10 horas
  Dado que he comido 1000 pepinos
  Cuando espero 10 horas
  Entonces mi estómago debería gruñir

# Funcionalidad: Manejo de tiempos complejos
Escenario: Manejar tiempos complejos 1
  Dado que he comido 50 pepinos
  Cuando espero "1 hora, 30 minutos y 45 segundos"
  Entonces mi estómago debería gruñir

Escenario: Manejar tiempos complejos 2
  Dado que he comido 10 pepinos
  Cuando espero "10 minutos y 50 segundos"
  Entonces mi estómago no debería gruñir

Escenario: Manejar tiempos complejos 3
  Dado que he comido 20 pepinos
  Cuando espero "5 hora, 45 minutos y 5 segundos"
  Entonces mi estómago debería gruñir

# Conversion de test unitario test_belly_steps()
Escenario: Comer muchos pepinos y esperar el tiempo suficiente
  Dado que he comido 15 pepinos
  Cuando espero 2 horas
  Entonces mi estómago debería gruñir

# =========================================
# Historia de usuario:
# "Como usuario que ha comido pepinos, 
#  quiero saber si mi estómago va a gruñir 
#  después de esperar un tiempo suficiente, 
#  para poder tomar una acción."
# =========================================

Escenario: Comer suficientes pepinos y esperar el tiempo adecuado
  Dado que he comido 20 pepinos
  Cuando espero 2 horas
  Entonces mi estómago debería gruñir

Escenario: Comer pocos pepinos y no esperar suficiente tiempo
  Dado que he comido 5 pepinos
  Cuando espero 1 hora
  Entonces mi estómago no debería gruñir

# Prueba de secuencia TDD a BDD
Escenario: Saber cuántos pepinos he comido
  Dado que he comido 15 pepinos
  Entonces debería haber comido 15 pepinos

# Prueba refactorización
Escenario: Verificar que el estómago gruñe tras comer suficientes pepinos y esperar
  Dado que he comido 20 pepinos
  Cuando espero 2 horas
  Entonces mi estómago debería gruñir

Escenario: Predecir si mi estómago gruñirá tras comer y esperar
  Dado que he comido 15 pepinos
  Cuando espero 2 horas
  Entonces mi estómago debería gruñir

# =======================================================
# Historia de usuario:
# "Como usuario que ha comido cierta cantidad de pepinos, 
#  quiero saber si podré esperar un tiempo suficiente
#  para poder tomar otro."
# =======================================================

Escenario: Ver cuántos pepinos puedo comer antes de que el estómago gruña
  Dado que he comido 8 pepinos
  Cuando pregunto cuántos pepinos más puedo comer
  Entonces debería decirme que puedo comer 80 pepinos más
