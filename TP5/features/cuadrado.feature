

Feature: Calcular el cuadrado de un número
  Como usuario
  Quiero calcular el cuadrado de un valor entero
  Para obtener su valor al multiplicarse por sí mismo

  Scenario: Calcular el cuadrado de un número positivo
    Given un número entero 4
    When calculo el cuadrado del número
    Then el resultado debe ser 16

  Scenario: Calcular el cuadrado de un número negativo
    Given un número entero -3
    When calculo el cuadrado del número
    Then el resultado debe ser 9

  Scenario: Calcular el cuadrado de cero
    Given un número entero 0
    When calculo el cuadrado del número
    Then el resultado debe ser 0
