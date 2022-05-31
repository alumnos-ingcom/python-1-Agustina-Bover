############
#Nombre-@Agustina-Bover
#UNRN Andina - Introduccion a la Ingenieria en Computacion
###########
"""
Estos son los test correspondientes al archivo "ejercicio10.py"
que estan en la carpeta "src".
"""
import pytest
from src.ejercicio10 import palindromo
def test_palindromo_si():
    """
    Comprueba el funcionamiento si la palabra efectivamente es un
    palindromo
    """
    palabra="neuquen"
    resultado=palindromo(palabra)
    assert isinstance(resultado, bool),"El resultado debe ser un valor booleano"
    assert resultado==True, "No se obtiene el resultado esperado"
def test_palindromo_no():
    """
    Comprueba el funcionamiento si la palabra no es un palindromo
    """
    palabra="milanesa"
    resultado=palindromo(palabra)
    assert isinstance(resultado, bool),"El resultado debe ser un valor booleano"
    assert resultado==False, "No se obtiene el resultado esperado"
       