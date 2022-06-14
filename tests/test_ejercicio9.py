############
#Nombre-@Agustina-Bover
#UNRN Andina - Introduccion a la Ingenieria en Computacion
###########
"""
Estos son los test correspondientes al archivo "ejercicio9.py"
que estan en la carpeta "src".
"""
import pytest
from src.ejercicio9 import factores_primos
def test_factores_primos_par():
    """
    Comprueba el funcionamiento con un numero par
    """
    numero=128
    resultado=factores_primos(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla"
    assert resultado==(2,2,2,2,2,2,2), "No se obtiene el resultado esperado"
    assert numero>0, "No se ingreso un numero positivo"
def test_factores_primos_impar():
    """
    Comprueba el funcionamiento con un numero impar
    """
    numero=135
    resultado=factores_primos(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla"
    assert resultado==(3,3,3,5), "No se obtiene el resultado esperado"
    assert numero>0, "No se ingreso un numero positivo"
