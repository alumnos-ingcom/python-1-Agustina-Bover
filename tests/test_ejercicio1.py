############
#Nombre-@Agustina-Bover
#UNRN Andina - Introduccion a la Ingenieria en Computacion
###########
"""
Estos son los test correspondientes al archivo "ejercicio1.py"
que estan en la carpeta "src".
"""
import pytest
from src.ejercicio1 import convertir_fahrrenheit, convertir_centigrados

def test_convertir_fahrrenheit():
    """
    Prueba la funcion si se le ingresa un numero entero positivo
    """
    numero=20.0
    resultado= convertir_fahrrenheit(numero)
    assert isinstance(resultado,float), "El resultado debe ser un numero decimal"
    assert resultado>0,"El resultado debe ser mayor que cero"
    assert resultado==68.0, "No se obtiene el resultado esperado"
def test_convertir_fahrrenheit():
    """
    Prueba la funcion si se le ingresa un numero entero negativo
    """
    numero=-20.0
    resultado= convertir_fahrrenheit(numero)
    assert isinstance(resultado,float), "El resultado debe ser un numero decimal"
    assert resultado<0,"El resultado debe ser menor que cero"
    assert resultado==-4.0, "No se obtiene el resultado esperado"
def test_convertir_fahrrenheit():
    """
    Prueba la funcion si se le ingresa un numero menor a -273.15
    """
    numero=-273.16
    resultado= convertir_fahrrenheit(numero)
    assert isinstance(resultado,str), "El resultado debe ser una cadena"
    assert resultado=="No existe temperatura" , "No se obtiene el resultado esperado"
def test_convertir_centigrados():
    """
    Prueba la funcion si se le ingresa un numero entero positivo
    """
    numero=130.0
    resultado=convertir_centigrados(numero)
    assert  isinstance(resultado, float), "El resultado debe ser un numero decimal"
    assert resultado>0,"El resultado debe ser mayor que cero"
    assert resultado==54.44, "No se obtiene el resultado esperado"
def test_convertir_centigrados():
    """
    Prueba la funcion si se le ingresa un numero entero negativo
    """
    numero=-20.0
    resultado=convertir_centigrados(numero)
    assert  isinstance(resultado, float), "El resultado debe ser un numero decimal"
    assert resultado<0,"El resultado debe ser menor que cero"
    assert resultado==-28.89, "No se obtiene el resultado esperado"
def test_convertir_centigrados():
    """
    Prueba la funcion si se le ingresa un numero menor a -459.67
    """
    numero=-459.68
    resultado= convertir_centigrados(numero)
    assert isinstance(resultado,str), "El resultado debe ser una cadena"
    assert resultado=="No existe temperatura" , "No se obtiene el resultado esperado"