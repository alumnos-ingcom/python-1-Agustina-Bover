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
    suma=2
    contador=0
    while suma<numero:
        if numero%suma==0:
            contador+=1
            break
        suma=suma+1
    if contador==1:
        return False
    return True
def principal():
    """
     Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    """
    nro= int(input("Ingrese numero entero positivo "))
    assert nro>0, "No ingreso un numero positivo"
    print(es_primo(nro))
if __name__ =='__main__':
    principal ()
