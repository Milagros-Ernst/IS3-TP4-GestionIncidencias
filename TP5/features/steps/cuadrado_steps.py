
from behave import given, when, then
from funciones import cuadrado

@given('un número entero {n:d}')
def step_given_entero(context, n):
    context.numero = n

@when('calculo el cuadrado del número')
def step_when_cuadrado(context):
    context.resultado = cuadrado(context.numero)

@then('el resultado debe ser {esperado:d}')
def step_then_resultado(context, esperado):
    assert context.resultado == esperado
