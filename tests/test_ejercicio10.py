############
#Nombre-@Agustina-Bover
#UNRN Andina - Introduccion a la Ingenieria en Computacion
###########
"""
Estos son los test correspondientes al archivo "ejercicio10.py"
que estan en la carpeta "src".
"""
import pytest
from src.ejercicio10 import es_palindromo
def test_es_palindromo_si():
    """
    Comprueba el funcionamiento si la palabra efectivamente es un
    palindromo
    """
    palabra="neuquen"
    resultado=es_palindromo(palabra)
    assert isinstance(resultado, bool),"El resultado debe ser un valor booleano"
    assert resultado is True, "No se obtiene el resultado esperado"
def test_es_palindromo_no():
    """
    Comprueba el funcionamiento si la palabra no es un palindromo
    """
    palabra="milanesa"
    resultado=es_palindromo(palabra)
    assert isinstance(resultado, bool),"El resultado debe ser un valor booleano"
    assert resultado is False, "No se obtiene el resultado esperado"
       