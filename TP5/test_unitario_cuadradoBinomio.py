from funciones import cuadrado_binomio

# Prueba unitaria REAL para cuadrado_binomio: mockea la función cuadrado
@patch('funciones.cuadrado')
def test_cuadrado_binomio_unitario(mock_cuadrado):
    mock_cuadrado.side_effect = [1, 9]
    resultado = cuadrado_binomio(1, 3)
    assert resultado == 1 + 2 * 1 * 3 + 9  # = 16
