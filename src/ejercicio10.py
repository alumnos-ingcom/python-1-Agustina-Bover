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
def es_palindromo (palabra):
    '''
    Esta funcion determina si las palabras son consideradas palindromos
    '''
    invertida=''
    i=len(palabra)
    while i>0:
        invertida+=palabra[i-1]
        i=i-1
    if invertida==palabra:
        return True
    return False
def principal():
    """
     Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    """
    palabra=input('Ingrese una palabra--> ')
    palabra=palabra.lower()
    resultado=es_palindromo(palabra)
    print (f'La palabra es un palindromo? {resultado}')
if __name__ =='__main__':
    principal ()
