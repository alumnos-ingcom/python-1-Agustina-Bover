########
#Nombre - @Agustina-Bover
#UNRN Andina- Introducción a la Ingeniería en Computación
#Precondicion: Ingresar un numero entero
#Postcondicion: Determinar si el numero ingresado es o no primo
########
'''
Escribir una función que indique con True si un numero indicado es Primo.
'''
class ZeroPrimoException(Exception):
    '''
    Esta excepcion fue creada en caso de que el usuario ingrese 0. Esto es debido a que
    el cero no es primo ni compuesto
    '''
    pass
def es_primo (numero):
    '''
    Esta funcion determina si el numero es primo o no.
    En caso de ingresar 0 se interrumpira la ejecucion del programa
    '''
    if numero==0:
        raise ZeroPrimoException("0 no es ni primo ni compuesto")
    if numero>0:
        suma=2
        while suma<numero:
            if numero%suma==0:
                resultado= False
                break
            suma=suma+1
            resultado= True
    if numero<0:
        suma=2
        while suma>numero:
            if numero%suma==0:
                resultado= False
                break
            suma=suma+1
            resultado= True
    return resultado
def principal():
    """
     Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    """
    nro= int(input("Ingrese numero entero "))
    resultado=es_primo(nro)
    print(f'Recuerde:\n True= es primo\n False= no es primo\n Resultado-->{resultado}')
if __name__ =='__main__':
    principal ()
