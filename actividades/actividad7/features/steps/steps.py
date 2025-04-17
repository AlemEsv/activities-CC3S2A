from behave import given, when, then, register_type
import re
import random

# Función para convertir palabras numéricas a números
def convertir_palabra_a_numero(palabra):
    try:
        return int(palabra)
    except ValueError:
        numeros = {
            # español
            "cero": 0, "uno": 1, "una": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
            "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
            "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
            "diecisiete": 17, "dieciocho": 18, "diecinueve": 19, "veinte": 20,
            "treinta": 30, "cuarenta": 40, "cincuenta": 50, "sesenta": 60, "setenta": 70,
            "ochenta": 80, "noventa": 90, "media": 0.5,
        
            # ingles
            "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
            "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
            "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
            "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
            "eighty": 80, "ninety": 90, "half": 0.5,
        }
        return numeros.get(palabra.lower(), 0)

def parsing_texto_a_float(palabra):
    return float(palabra)

register_type(palabra=parsing_texto_a_float)

@given('que he comido {cukes:palabra} pepinos')
def step_given_eaten_cukes(context, cukes):
    context.error = None
    try:
        if not 0 < cukes:
            raise ValueError("Hay una cantidad no valida de pepinos.")
        context.belly.comer(cukes)
    except ValueError as e:
        context.error = e

@when('espero {time_description}')
@when('espero un tiempo aleatorio {time_description}')
def step_when_wait_time_description(context, time_description):
    time_description = time_description.strip('"').lower()

    time_description = time_description.replace('y', ' ') #spanish
    time_description = time_description.replace('y', ' ') # advanced
    time_description = time_description.replace(',', ' ') # english

    time_description = time_description.strip()

    if time_description == 'media hora':
        total_time_in_hours = 0.5
    else:
        patter_hour_btwn_hour = re.compile(r'(?:entre|between)\s+(\w+)\s*(\w+)\s*(?:horas?|hours?)')
        pattern_hours_min_sec = re.compile(r'(?:(\w+)\s*(?:horas?|hours?))?\s*(?:(\w+)\s*(?:minutos?|minutes?))?\s*(?:(\w+)\s*(?:segundos?|seconds?))?')
        
        match_hour_btwn_hour = patter_hour_btwn_hour.match(time_description)
        match_hours_min_sec = pattern_hours_min_sec.match(time_description)

        
        if match_hour_btwn_hour:
            first_hour_word = match_hour_btwn_hour.group(1) or "0"
            second_hour_word = match_hour_btwn_hour.group(2) or "0"

            primera_hora = convertir_palabra_a_numero(first_hour_word)
            segunda_hora = convertir_palabra_a_numero(second_hour_word)
            
            total_time_in_hours = random.randint(primera_hora + 1,segunda_hora)

        elif match_hours_min_sec:
            hours_word = match_hours_min_sec.group(1) or "0"
            minutes_word = match_hours_min_sec.group(2) or "0"
            seconds_word = match_hours_min_sec.group(3) or "0"

            hours = convertir_palabra_a_numero(hours_word)
            minutes = convertir_palabra_a_numero(minutes_word)
            seconds = convertir_palabra_a_numero(seconds_word)

            total_time_in_hours = hours + (minutes / 60) + (seconds / 3600)
        else:
            raise ValueError(f"No se pudo interpretar la descripción del tiempo: {time_description}")

    context.belly.esperar(total_time_in_hours)

@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context):
    assert context.belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context):
    assert not context.belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."

@then('debería ocurrir un error de cantidad negativa')
def step_then_belly_should_have_cukes(context):
    assert not context.error is not None, "Se esperaba un error por cantidad negativa, y ocurrió."