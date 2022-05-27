########
#Nombre - @Agustina-Bover
#UNRN Andina- Introducción a la Ingeniería en Computación
#Precondicion: Ingresar un numero entero positivo
#Postcondicion: Obtener  los factores primos de dicho nro
########
'''
Escribir una función que retorne una tuple con factores primos de un numero entero positivo.
'''
def factores_primos (numero):
    '''
    Esta funcion determina los factores primos de un punto
    '''
    primos=[]
    for num in range (2, numero+1):
        while numero%num==0:
            primos.append(num)
            numero=numero/num
    tupla=tuple(primos)
    return tupla

def principal():
    """
     Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    """
    nro=int(input('Ingrese numero entero positivo-->'))
    print (f' Sus factores primos son: {factores_primos(nro)}')
if __name__ =='__main__':
    principal ()
