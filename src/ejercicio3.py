########
#Nombre - @Agustina-Bover
#UNRN Andina- Introducción a la Ingeniería en Computación
#Precondicion: El ingreso de dos numeros enteros
#Postcondicion: La comparacion de dichos numeros.
########
"""
Escribir una función que utilizando sumas y restas, reciba dos valores y retorne:
Retornar -1 si el primero es menor que el segundo
Retornar 0 si son iguales
Retornar 1 si el primero es mayor que el segundo
"""
def comparar (numero1, numero2):
    """
    Esta variable compara ambos numeros y dedtermina cual es mayor
    o si son iguales
    """
    valor=0
    if numero1-numero2==0:
        return valor
    if numero1-numero2>0:
        valor=1
    else:
        valor=-1
    return valor
def principal ():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    """
    print ("Ingrese dos numeros enteros")
    nro1=int(input('--> nro1: '))
    nro2=int(input('--> nro2: '))
    resultado=comparar(nro1, nro2)
    print ('Recuerde\n-1--> nro1<nro2\n 0--> nro1=nro2\n 1-->nro1>nro2')
    print (f' Resultado: {resultado}')
if __name__ =='__main__':
    principal ()
