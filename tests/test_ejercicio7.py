############
#Nombre-@Agustina-Bover
#UNRN Andina - Introduccion a la Ingenieria en Computacion
###########
"""
Estos son los test correspondientes al archivo "ejercicio7.py"
que estan en la carpeta "src".
"""
import pytest
from src.ejercicio7 import decimal_a_sexadecimal, sexadecimal_a_decimal
def test_decimal_a_sexadecimal():
    """
    Esta funcion comprueba el buen funcionamiento del pasaje a sexadecimal
    """
    numero=300
    resultado=decimal_a_sexadecimal(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser Una tupla"
    assert resultado==(0,5,0), "No se obtiene el resultado esperado"
def test_sexadecimal_a_decimal():
    """
    Esta funcion comprueba el buen funcionamiento del pasaje a decimal
    """
    horas=5
    minutos=3
    segundos=2
    resultado=sexadecimal_a_decimal(horas,minutos,segundos)
    assert isinstance(resultado, int), "El resultado debe ser un numero entero"
    assert resultado==18182, "No se obtiene el resultado esperado"

