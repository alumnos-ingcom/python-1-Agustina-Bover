############
#Nombre-@Agustina-Bover
#UNRN Andina - Introduccion a la Ingenieria en Computacion
###########
"""
Estos son los test correspondientes al archivo "ejercicio8.py"
que estan en la carpeta "src".
"""
import pytest
from src.ejercicio8 import es_primo
def test_es_primo_primo():
    """
    Esta funcion comprueba el funcionamiento de la misma si se ingresa
    un numero primo
    """
    numero=3
    resultado=es_primo(numero)
    assert isinstance(resultado, bool),"El resultado debe ser un booleano"
    assert resultado is True, "No se obtiene el resultado esperado"
    assert numero>0, "No se ingreso un numero positivo"
def test_es_primo_no_primo():
    """
    Esta funcion comprueba el funcionamiento de la misma si se ingresa
    un numero que no es primo
    """
    numero=6
    resultado=es_primo(numero)
    assert isinstance(resultado, bool),"El resultado debe ser un booleano"
    assert resultado is False, "No se obtiene el resultado esperado"
    assert numero>0, "No se ingreso un numero positivo"
