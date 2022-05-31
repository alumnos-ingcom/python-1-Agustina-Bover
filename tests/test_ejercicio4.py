############
#Nombre-@Agustina-Bover
#UNRN Andina - Introduccion a la Ingenieria en Computacion
###########
"""
Estos son los test correspondientes al archivo "ejercicio4.py"
que estan en la carpeta "src".
"""
import pytest
from src.ejercicio4 import suma_lenta
def test_suma_lenta_positivo():
    '''
    Comprueba la fundion en el caso de ambos numeros sean positivos
    '''
    nro1=6
    nro2=2
    resultado=suma_lenta(nro1,nro2)
    assert isinstance  (resultado,int), "El resultado debe ser un numero entero"
    assert resultado==8, "No se obtiene el resultado esperado"
    assert resultado>=nro1, "No se obtiene el resultado esperado"
def test_suma_lenta_negativos():
    '''
    Comprueba la fundion en el caso de ambos numeros sean negativos
    '''
    nro1=-5
    nro2=-6
    resultado=suma_lenta(nro1,nro2)
    assert isinstance  (resultado,int), "El resultado debe ser un numero entero"
    assert resultado==-11, "No se obtiene el resultado esperado"
    assert resultado<=nro1, "No se obtiene el resultado esperado"
def test_suma_lenta_mezclado_uno():
    '''
    Comprueba la fundion en el caso de que el primer nro sea negativo
    y el otro positivo
    '''
    nro1=-5
    nro2=6
    resultado=suma_lenta(nro1,nro2)
    assert isinstance  (resultado,int), "El resultado debe ser un numero entero"
    assert resultado==1, "No se obtiene el resultado esperado"
    assert resultado>=nro1, "No se obtiene el resultado esperado"
def test_suma_lenta_mezclado_dos():
    '''
    Comprueba la fundion en el caso de que el primer nro sea positivo
    y el otro negativo
    '''
    nro1=5
    nro2=-6
    resultado=suma_lenta(nro1,nro2)
    assert isinstance  (resultado,int), "El resultado debe ser un numero entero"
    assert resultado==-1, "No se obtiene el resultado esperado"
    assert resultado<=nro1, "No se obtiene el resultado esperado"
