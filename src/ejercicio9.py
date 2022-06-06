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
    Esta funcion determina los factores primos de un numero
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
    try:
        assert nro>0
        resultado=factores_primos(nro)
        print (f'Sus factores primos son: {resultado}')
    except AssertionError as exc:
        print ('Debe ingresar un numero positivo')
        principal()
if __name__ =='__main__':
    principal ()
