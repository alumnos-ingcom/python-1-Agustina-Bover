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
def test_es_multiplo_si_positivos_ambos():
    """
    Comprueba el funcionamiento si el nro2 (positivo )efectivamente es multiplo
    de nro1 (positivo)
    """
    nro1=6
    nro2=2
    resultado=es_multiplo(nro1,nro2)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano"
    assert resultado is True, "No se obtiene el resultado esperado"

def test_es_multiplo_no_positivos_ambos():
    """
    Comprueba el funcionamiento si el nro2 (positivo) no es multiplo
    de nro1 (positivo)
    """
    nro1=7
    nro2=6
    resultado=es_multiplo(nro1,nro2)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano"
    assert resultado is False, "No se obtiene el resultado esperado"

def test_es_multiplo_si_negativo_multiplo():
    """
    Comprueba el funcionamiento si el nro2 (negativo) es multiplo
    de nro1 (positivo)
    """
    nro1=6
    nro2=-3
    resultado=es_multiplo(nro1,nro2)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano"
    assert resultado is True, "No se obtiene el resultado esperado"
def test_es_multiplo_no_negativo_multiplo():
    """
    Comprueba el funcionamiento si el nro2 (negativo) no es multiplo
    de nro1 (positivo)
    """
    nro1=7
    nro2=-3
    resultado=es_multiplo(nro1,nro2)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano"
    assert resultado is False, "No se obtiene el resultado esperado"
def test_es_multiplo_si_negativo_numero1():
    """
    Comprueba el funcionamiento si el nro2 (positivo) es multiplo
    de nro1 (negativo)
    """
    nro1=-8
    nro2=2
    resultado=es_multiplo(nro1,nro2)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano"
    assert resultado is True, "No se obtiene el resultado esperado"
def test_es_multiplo_no_negativo_numero1():
    """
    Comprueba el funcionamiento si el nro2 (positivo) no es multiplo
    de nro1 (negativo)
    """
    nro1=-9
    nro2=2
    resultado=es_multiplo(nro1,nro2)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano"
    assert resultado is False, "No se obtiene el resultado esperado"
def test_es_multiplo_si_ambos_negativos():
    """
    Comprueba el funcionamiento si el nro2 (negativo) es multiplo
    de nro1 (negativo)
    """
    nro1=-8
    nro2=-2
    resultado=es_multiplo(nro1,nro2)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano"
    assert resultado is True, "No se obtiene el resultado esperado"
def test_es_multiplo_no_ambos_negativos():
    """
    Comprueba el funcionamiento si el nro2 (negativo) no es multiplo
    de nro1 (negativo)
    """
    nro1=-8
    nro2=-3
    resultado=es_multiplo(nro1,nro2)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano"
    assert resultado is False, "No se obtiene el resultado esperado"
