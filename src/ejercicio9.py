########
#Nombre - @Agustina-Bover
#UNRN Andina- Introducción a la Ingeniería en Computación
#Precondicion: Ingresar un numero entero positivo
#Postcondicion: Obtener  los factores primos de dicho nro
########
'''
Escribir una función que retorne una tuple con factores primos de un numero entero positivo.
'''
class NegativoException(Exception):
    '''
    Esta excepcion fue creada para el caso en el que se ingrese
    un numero negativo
    '''
    pass
def factores_primos (numero):
    '''
    Esta funcion determina los factores primos de un numero. En caso
    de que sea ingresado un nro negativo se interrumpira la ejecucion
    del programa
    '''
    if numero<0:
        raise NegativoException ('Ingreso un numero invalido, recuerde que debe ser positivo. Intente de nuevo')
    primos=[]
    for num in range (2, numero+1):
        while numero%num==0:
            primos.append(num)
            numero=numero/num
    tupla=tuple(primos)
    resultado=tupla
    return resultado

def principal():
    """
     Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    """
    nro=int(input('Ingrese numero entero positivo-->'))
    resultado=factores_primos(nro)
    print (f'Sus factores primos son: {resultado}')
if __name__ =='__main__':
    principal ()
