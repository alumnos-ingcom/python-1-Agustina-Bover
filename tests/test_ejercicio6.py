############
#Nombre-@Agustina-Bover
#UNRN Andina - Introduccion a la Ingenieria en Computacion
###########
"""
Estos son los test correspondientes al archivo "ejercicio6.py"
que estan en la carpeta "src".
"""
import pytest
from src.ejercicio6 import ordenar_mayor_a_menor, ordenar_menor_a_mayor
def test_ordenar_mayor_a_menor_1():
    """
    Comprueba como ordena si Nro1 es el mayor
    """
    nro1=3
    nro2=2
    nro3=1
    resultado=ordenar_mayor_a_menor(nro1,nro2,nro3)
    assert isinstance(resultado, tuple), "El resultado debe ser Una tupla"
    assert resultado==(3,2,1), "No se obtiene el resultado esperado"
def test_ordenar_mayor_a_menor_2():
    """
    Comprueba como ordena si Nro3 es el mayor
    """
    nro1=1
    nro2=4
    nro3=7
    resultado=ordenar_mayor_a_menor(nro1,nro2,nro3)
    assert isinstance(resultado, tuple), "El resultado debe ser Una tupla"
    assert resultado==(7,4,1), "No se obtiene el resultado esperado"
def test_ordenar_mayor_a_menor_3():
    """
    Comprueba como ordena si Nro2 es el mayor
    """
    nro1=1
    nro2=5
    nro3=3
    resultado=ordenar_mayor_a_menor(nro1,nro2,nro3)
    assert isinstance(resultado, tuple), "El resultado debe ser Una tupla"
    assert resultado==(5,3,1), "No se obtiene el resultado esperado"
def test_ordenar_menor_a_mayor_1():
    """
    Comprueba como ordena si Nro1 es el menor
    """
    nro1=1
    nro2=2
    nro3=3
    resultado=ordenar_menor_a_mayor(nro1,nro2,nro3)
    assert isinstance(resultado, tuple), "El resultado debe ser Una tupla"
    assert resultado==(1,2,3), "No se obtiene el resultado esperado"

def test_ordenar_menor_a_mayor_2():
    """
    Comprueba como ordena si Nro3 es el menor
    """
    nro1=9
    nro2=6
    nro3=1
    resultado=ordenar_menor_a_mayor(nro1,nro2,nro3)
    assert isinstance(resultado, tuple), "El resultado debe ser Una tupla"
    assert resultado==(1,6,9), "No se obtiene el resultado esperado"
def test_ordenar_menor_a_mayor_3():
    """
    Comprueba como ordena si Nro2 es el menor
    """
    nro1=5
    nro2=1
    nro3=3
    resultado=ordenar_menor_a_mayor(nro1,nro2,nro3)
    assert isinstance(resultado, tuple), "El resultado debe ser Una tupla"
    assert resultado==(1,3,5), "No se obtiene el resultado esperado"
 