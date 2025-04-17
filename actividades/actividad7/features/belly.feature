# language: es

Característica: Comportamiento del Estómago

  Escenario: Comer muchos pepinos y gruñir
    Dado que he comido 42 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  Escenario: Comer pocos pepinos y no gruñir
    Dado que he comido 10 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir

  Escenario: Comer muchos pepinos y esperar menos de una hora
    Dado que he comido 50 pepinos
    Cuando espero media hora
    Entonces mi estómago no debería gruñir

  Escenario: Comer pepinos y esperar en minutos
    Dado que he comido 30 pepinos
    Cuando espero 90 minutos
    Entonces mi estómago debería gruñir

  Escenario: Comer pepinos y esperar en diferentes formatos
    Dado que he comido 25 pepinos
    Cuando espero "dos horas y treinta minutos"
    Entonces mi estómago debería gruñir

  Escenario: Comer pepinos y esperar en minutos y segundos
    Dado que he comido 35 pepinos
    Cuando espero "1 hora y 30 minutos y 45 segundos"
    Entonces mi estómago debería gruñir
  
  Escenario: Comer una cantidad fraccionaria de pepinos
  Dado que he comido 0.5 pepinos
  Cuando espero 2 horas
  Entonces mi estómago no debería gruñir

  Escenario: Esperar usando horas en inglés 1
  Dado que he comido 20 pepinos
  Cuando espero "two hours and thirty minutes"
  Entonces mi estómago debería gruñir

  Escenario: Esperar usando horas en inglés 2
  Dado que he comido 5 pepinos
  Cuando espero "one hours and twenty seconds"
  Entonces mi estómago no debería gruñir

  Escenario: Comer pepinos y esperar un tiempo aleatorio
  Dado que he comido 25 pepinos
  Cuando espero un tiempo aleatorio entre 1 y 3 horas
  Entonces mi estómago debería gruñir

  Escenario: Manejar una cantidad negativa de pepinos
  Dado que he comido 5 pepinos
  Entonces debería ocurrir un error de cantidad negativa

  Escenario: Manejar tiempos complejos 1
  Dado que he comido 50 pepinos
  Cuando espero "1 hora, 30 minutos y 45 segundos"
  Entonces mi estómago debería gruñir

  Escenario: Manejar tiempos complejos 2
  Dado que he comido 10 pepinos
  Cuando espero "4 hora, 2 minutos y 50 segundos"
  Entonces mi estómago no debería gruñir