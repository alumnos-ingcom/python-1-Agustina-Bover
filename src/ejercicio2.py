########
#Nombre - @Agustina-Bover
#UNRN Andina- Introducción a la Ingeniería en Computación
#Precondicion: La entrada de un numero.Puede ser negativo, positivo o cero.
#Postcondicion: El programa debe brindar el signo del numero ingresado
########
"""
Escribir una función que reciba un número e indique si el mismo es positivo,
negativo o cero utilizando sumas y restas.
"""
def signo (numero):
    """
    Esta funcion define el signo del numero
    """
    if numero==0:
        resultado= 0
    elif numero+abs(numero)==0:
        resultado= -1
    elif numero-abs(numero)==0:
        resultado= 1
    return resultado

def principal ():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    """
    print ("Ingrese un numero")
    numero=int (input('--> numero: '))
    print("Recuerde\n 0--> Cero\n 1--> Positivo\n-1--> Negativo")
    resultado=signo(numero)
    print(f'El resultado es {resultado}')

if __name__ =='__main__':
    principal ()
