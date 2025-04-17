from src.belly import Belly

def test_gruñir_si_comido_muchos_pepinos():
    belly = Belly()
    belly.comer(15)
    belly.esperar(2)
    assert belly.esta_gruñendo() == True

def test_gruñir_sino_he_comido_muchos_pepinos():
    belly = Belly()
    belly.comer(1)
    belly.esperar(20.1)
    assert belly.esta_gruñendo() == False

def test_pepinos_restantes():
    belly = Belly()
    belly.comer(15)
    assert belly.pepinos_comidos == 15