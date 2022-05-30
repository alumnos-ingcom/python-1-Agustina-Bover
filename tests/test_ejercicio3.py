############
#Nombre-@Agustina-Bover
#UNRN Andina - Introduccion a la Ingenieria en Computacion
###########
"""
Estos son los test correspondientes al archivo "ejercicio3.py"
que estan en la carpeta "src".
"""
import pytest
from src.ejercicio3 import comparar
def test_comparar_menor():
    '''
    Comprueba la fundion en el caso de que el primer numero sea menor
    que el segundo
    '''
    nro1=3
    nro2=5
    resultado= comparar(nro1,nro2)
    assert isinstance (resultado, int), "El resultado debe ser un numero entero"
    assert resultado==-1, "No se obtiene el resultado esperado"
def test_comparar_mayor():
    '''
    Comprueba la fundion en el caso de que el primer numero sea mayor
    que el segundo
    '''
    nro1=6
    nro2=5
    resultado= comparar(nro1,nro2)
    assert isinstance (resultado, int), "El resultado debe ser un numero entero"
    assert resultado==1, "No se obtiene el resultado esperado"
def test_comparar_igual():
    '''
    Comprueba la fundion en el caso de que el primer numero sea igual
    que el segundo
    '''
    nro1=3
    nro2=3
    resultado= comparar(nro1,nro2)
    assert isinstance (resultado, int), "El resultado debe ser un numero entero"
    assert resultado==0, "No se obtiene el resultado esperado"   
