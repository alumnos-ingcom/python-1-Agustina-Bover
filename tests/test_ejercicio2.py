############
#Nombre-@Agustina-Bover
#UNRN Andina - Introduccion a la Ingenieria en Computacion
###########
"""
Estos son los test correspondientes al archivo "ejercicio2.py"
que estan en la carpeta "src".
"""
import pytest
from src.ejercicio2 import signo
def test_signo_positivo():
    """
    Se prueba la funcion ingresando un numero entero positivo
    """
    numero=4
    resultado="El numero es Positivo"
    assert isinstance(resultado,str),"El resultado debe ser un numero decimal"
    assert resultado=="El numero es Positivo", "No se obtiene el resultado esperado"
def test_signo_negativo():
    """
    Se prueba la funcion ingresando un numero entero negativo
    """
    numero=-4
    resultado="El numero es Negativo"
    assert isinstance(resultado,str),"El resultado debe ser un numero decimal"
    assert resultado=="El numero es Negativo", "No se obtiene el resultado esperado"
def test_signo_cero():
    """
    Se prueba la funcion ingresando cero
    """
    numero=0
    resultado="El numero es Cero"
    assert isinstance(resultado,str),"El resultado debe ser un numero decimal"
    assert resultado=="El numero es Cero", "No se obtiene el resultado esperado"
