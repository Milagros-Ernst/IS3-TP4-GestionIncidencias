from funciones import cuadrado_binomio

def test_cuadrado_binomio():
    assert cuadrado_binomio(3, 2) == 25
    assert cuadrado_binomio(-1, 1) == 0