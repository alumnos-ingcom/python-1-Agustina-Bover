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
    estado=""
    if numero==0:
        estado='Cero'
    elif numero+abs(numero)==0:
        estado="Negativo"
    elif numero-abs(numero)==0:
        estado="Positivo"
    return estado

def principal ():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    """
    print ("Ingrese un numero")
    numero=int (input('--> numero: '))
    print (f' El numero es {signo(numero)}')

if __name__ =='__main__':
    principal ()
