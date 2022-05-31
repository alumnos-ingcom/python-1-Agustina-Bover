############
#Nombre-@Agustina-Bover
#UNRN Andina - Introduccion a la Ingenieria en Computacion
###########
"""
Estos son los test correspondientes al archivo "ejercicio10.py"
que estan en la carpeta "src".
"""
import pytest
from src.ejercicio11 import es_multiplo
def test_es_multiplo_si():
    """
    Comprueba el funcionamiento si el nro2 efectivamente es multiplo
    de nro1
    """
    nro1=6
    nro2=2
    resultado=es_multiplo(nro1,nro2)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano"
    assert resultado is True, "No se obtiene el resultado esperado"
    assert nro1>0 and nro2>0, "Los numeros deben ser positivos"
def test_es_multiplo_no():
    """
    Comprueba el funcionamiento si el nro2 no es multiplo
    de nro1
    """
    nro1=7
    nro2=6
    resultado=es_multiplo(nro1,nro2)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano"
    assert resultado is False, "No se obtiene el resultado esperado"
    assert nro1>0 and nro2>0, "Los numeros deben ser positivos"
