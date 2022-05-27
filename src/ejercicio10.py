########
#Nombre - @Agustina-Bover
#UNRN Andina- Introducción a la Ingeniería en Computación
#Precondicion: El ingreso de una palabra.
#Postcondicion: Determinar si la palabra ingresada es o no un palindromo.
########
'''
Escribir una función que indique con True si una palabra o frase
ingresada se trata de un palindromo. Palíndromo, es si se lee
igual de derecha a izquierda que de izquierda a derecha.
'''
def palindromo (palabra):
    '''
    Esta funcion determina si las palabras son consideradas palindromos
    '''
    lista=list(palabra)
    lista2=lista[::-1]#Invierte la lista.
    resultado=' '
    if lista==lista2:
        resultado='True'
    else:
        resultado='False'
    return resultado
def principal():
    """
     Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    """
    palabra=input('Ingrese una palabra--> ')
    palabra=palabra.lower()
    print (f' La palabra es un palindromo? {palindromo(palabra)}')
if __name__ =='__main__':
    principal ()
