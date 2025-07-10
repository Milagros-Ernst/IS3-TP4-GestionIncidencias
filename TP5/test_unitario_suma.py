from funciones import suma, cuadrado

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0