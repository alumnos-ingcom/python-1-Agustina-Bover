############
#Nombre-@Agustina-Bover
#UNRN Andina - Introduccion a la Ingenieria en Computacion
###########
"""
Estos son los test correspondientes al archivo "ejercicio5.py"
que estan en la carpeta "src".
"""
import pytest
from src.ejercicio5 import division_lenta
def test_division_lenta_exacta():
    '''
    Comprueba la funcion en el caso de que la division sea exacta
    '''
    nro1=6
    nro2=2
    resultado=division_lenta(nro1,nro2)
    assert isinstance  (resultado,tuple), "El resultado debe ser una tupla"
    assert resultado==(3,0), "No se obtiene el resultado esperado"
    assert nro1>0 and nro2>0, "No se ingresaron numeros postivos"
def test_division_lenta_con_resto():
    '''
    Comprueba la funcion en el caso de que la division no sea exacta
    '''
    nro1=6
    nro2=4
    resultado=division_lenta(nro1,nro2)
    assert isinstance  (resultado,tuple), "El resultado debe ser una tupla"
    assert resultado==(1,2), "No se obtiene el resultado esperado"
    assert nro1>0 and nro2>0, "No se ingresaron numeros postivos"
def test_division_lenta_sin_cociente():
    '''
    Comprueba la funcion en el caso de que nro1<nro2
    '''
    nro1=3
    nro2=4
    resultado=division_lenta(nro1,nro2)
    assert isinstance  (resultado,tuple), "El resultado debe ser Una tupla"
    assert resultado==(0,3), "No se obtiene el resultado esperado"
    assert nro1>0 and nro2>0, "No se ingresaron numeros postivos"
