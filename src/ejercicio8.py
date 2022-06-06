########
#Nombre - @Agustina-Bover
#UNRN Andina- Introducción a la Ingeniería en Computación
#Precondicion: Ingresar un numero entero
#Postcondicion: Determinar si el numero ingresado es o no primo
########
'''
Escribir una función que indique con True si un numero indicado es Primo.
'''
def es_primo (numero):
    '''
    Esta funcion determina si el numero es primo o no
    '''
    if numero>0:
        suma=2
        while suma<numero:
            if numero%suma==0:
                return False
                break
            suma=suma+1   
        return True
    else:
        suma=2
        while suma>numero:
            if numero%suma==0:
                return False
                break
            suma=suma+1
        return True
def principal():
    """
     Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    """
    nro= int(input("Ingrese numero entero "))
    assert nro!=0, "0 no es ni primo ni compuesto"
    resultado=es_primo(nro)
    print(f'Recuerde:\n True= es primo\n False= no es primo\n Resultado-->{resultado}')
if __name__ =='__main__':
    principal ()
