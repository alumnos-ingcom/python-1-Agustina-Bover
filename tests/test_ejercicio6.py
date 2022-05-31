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
    Nro1=3
    Nro2=2
    Nro3=1
    resultado=ordenar_mayor_a_menor(Nro1,Nro2,Nro3)
    assert isinstance(resultado, tuple), "El resultado debe ser Una tupla" 
    assert resultado==(3,2,1), "No se obtiene el resultado esperado"
def test_ordenar_mayor_a_menor_2():
    """
    Comprueba como ordena si Nro3 es el mayor
    """
    Nro1=1
    Nro2=4
    Nro3=7
    resultado=ordenar_mayor_a_menor(Nro1,Nro2,Nro3)
    assert isinstance(resultado, tuple), "El resultado debe ser Una tupla" 
    assert resultado==(7,4,1), "No se obtiene el resultado esperado"
def test_ordenar_mayor_a_menor_3():
    """
    Comprueba como ordena si Nro2 es el mayor
    """
    Nro1=1
    Nro2=5
    Nro3=3
    resultado=ordenar_mayor_a_menor(Nro1,Nro2,Nro3)
    assert isinstance(resultado, tuple), "El resultado debe ser Una tupla" 
    assert resultado==(5,3,1), "No se obtiene el resultado esperado"
def test_ordenar_menor_a_mayor_1():
     """
     Comprueba como ordena si Nro1 es el menor
     """
     Nro1=1
     Nro2=2
     Nro3=3
     resultado=ordenar_menor_a_mayor(Nro1,Nro2,Nro3)
     assert isinstance(resultado, tuple), "El resultado debe ser Una tupla" 
     assert resultado==(1,2,3), "No se obtiene el resultado esperado"

def test_ordenar_menor_a_mayor_2():
    """
    Comprueba como ordena si Nro3 es el menor
    """
    Nro1=9
    Nro2=6
    Nro3=1
    resultado=ordenar_menor_a_mayor(Nro1,Nro2,Nro3)
    assert isinstance(resultado, tuple), "El resultado debe ser Una tupla" 
    assert resultado==(1,6,9), "No se obtiene el resultado esperado"
def test_ordenar_menor_a_mayor_3():
    """
    Comprueba como ordena si Nro2 es el menor
    """
    Nro1=5
    Nro2=1
    Nro3=3
    resultado=ordenar_menor_a_mayor(Nro1,Nro2,Nro3)
    assert isinstance(resultado, tuple), "El resultado debe ser Una tupla" 
    assert resultado==(1,3,5), "No se obtiene el resultado esperado"
 