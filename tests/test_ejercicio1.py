############
#Nombre-@Agustina-Bover
#UNRN Andina - Introduccion a la Ingenieria en Computacion
###########
"""
Estos son los test correspondientes al archivo "ejercicio1"
que estan en la carpeta "src".
"""
import pytest
from src.ejercicio1 import convertir_a_fahrrenheit, convertir_a_centigrados

def test_convertir_a_fahrrenheit_positivo():
    """
    Prueba la funcion si se le ingresa un numero entero positivo
    """
    numero=20.0
    resultado= convertir_a_fahrrenheit(numero)
    assert isinstance(resultado,float), "El resultado debe ser un numero decimal"
    assert resultado>0,"El resultado debe ser mayor que cero"
    assert resultado==68.0, "No se obtiene el resultado esperado"
def test_convertir_a_fahrrenheit_negativo():
    """
    Prueba la funcion si se le ingresa un numero entero negativo
    """
    numero=-20.0
    resultado= convertir_a_fahrrenheit(numero)
    assert isinstance(resultado,float), "El resultado debe ser un numero decimal"
    assert resultado<0,"El resultado debe ser menor que cero"
    assert resultado==-4.0, "No se obtiene el resultado esperado"
def test_convertir_a_centigrados_positivo():
    """
    Prueba la funcion si se le ingresa un numero entero positivo
    """
    numero=130.0
    resultado=convertir_a_centigrados(numero)
    assert  isinstance(resultado, float), "El resultado debe ser un numero decimal"
    assert resultado>0,"El resultado debe ser mayor que cero"
    assert resultado==54.44444444444444, "No se obtiene el resultado esperado"
def test_convertir_a_centigrados_negativo():
    """
    Prueba la funcion si se le ingresa un numero entero negativo
    """
    numero=-20.0
    resultado=convertir_a_centigrados(numero)
    assert  isinstance(resultado, float), "El resultado debe ser un numero decimal"
    assert resultado<0,"El resultado debe ser menor que cero"
    assert resultado==-28.88888888888889, "No se obtiene el resultado esperado"

