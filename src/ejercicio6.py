########
#Nombre - @Agustina-Bover
#UNRN Andina- Introducción a la Ingeniería en Computación
#Precondicion: Que se ingresen 3 numeros enteros
#Poscondicion: Obtener el orden de mayor a menor y viceversa
########
"""
Escribir una función que a partir de tres variables de tipo entero retorne
una tupla con dichos valores ordenados de menor a mayor. Y Viceversa
"""
def ordenar_mayor_a_menor(uno,dos,tres):
    """
    Esta funcion ordena los numeros de mayor a menor
    """
    mayor=0
    menor=0
    medio=0
    if dos<uno and uno>tres:
        if dos>tres:
            medio=dos
            menor=tres
            mayor=uno
        else:
            medio=tres
            menor=dos
            mayor=uno
    if dos<uno and uno<tres:
        mayor=tres
        medio=uno
        menor=dos
    if dos>uno and uno>tres:
        mayor=dos
        medio=uno
        menor=tres
    if dos>uno and uno<tres:
        menor=uno
        if dos>tres:
            mayor=dos
            medio=tres
        else:
            mayor=tres
            medio=dos
    tupla=(mayor, medio, menor)
    return tupla
def ordenar_menor_a_mayor(uno,dos,tres):
    '''
    Esta funcion ordena los numeros de menor a mayor
    '''
    mayor=0
    menor=0
    medio=0
    if dos<uno and uno>tres:
        if dos>tres:
            medio=dos
            menor=tres
            mayor=uno
        else:
            medio=tres
            menor=dos
            mayor=uno
    if dos<uno and uno<tres:
        mayor=tres
        medio=uno
        menor=dos
    if dos>uno and uno>tres:
        mayor=dos
        medio=uno
        menor=tres
    if dos>uno and uno<tres:
        menor=uno
        if dos>tres:
            mayor=dos
            medio=tres
        else:
            mayor=tres
            medio=dos
    tupla=(menor, medio, mayor)
    return tupla
def principal ():
    """
     Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    """
    print ("Ingrese tres numeros enteros ")
    nro1=int(input('--> nro1: '))
    nro2=int(input('--> nro2: '))
    nro3=int(input('--> nro3: '))
    resultado1=ordenar_mayor_a_menor(nro1, nro2, nro3)
    resultado2=ordenar_menor_a_mayor(nro1, nro2, nro3)
    print (f'El orden de mayor a menor es {resultado1}')
    print (f'El orden de menor a mayor es {resultado2}')
if __name__ =='__main__':
    principal ()
