from src.belly import Belly

# prueba unitaria para manejo de pepinos comidos
def test_pepinos_comidos():
    belly = Belly()
    belly.comer(1.5)
    assert belly.pepinos_comidos == 1.5

# Funcionalidad: Prueba unitaria para saber si está o no gruñendo el estomago
def test_estomago_gruñendo():
    belly = Belly()
    belly.comer(12)
    belly.esperar(1.5)
    assert belly.esta_gruñendo() == True


