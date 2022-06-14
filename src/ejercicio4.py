########
#Nombre - @Agustina-Bover
#UNRN Andina- Introducción a la Ingeniería en Computación
#Precondicion: La entrada de dos numeros enteros
#Postcondicion: Mostrar la suma lenta entre esos numeros y su resultado
########
"""
Escribir una función que haga la suma entre dos números enteros sin hacer
la operación de manera directa. Esto quiere decir que para hacer la suma
entre 4 y 3, las operaciones resultantes deberán ser 4+1+1+1. La funcion debe
ser capaz de sumar cualquier numero entero positivo y negativo.
"""
def suma_lenta (numero1, numero2):
    """
    Esta funcion realiza la suma lenta tanto para numeros
    positivos como negativos
    """
    contador=0
    resultado=numero1
    print (numero1)
    while contador<abs(numero2):
        if numero2>0:
            print ('+1')
            resultado+=1
            contador+=1
        else:
            print ('-1')
            resultado-=1
            contador+=1
    return resultado
def principal():
    """
     Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    """
    print ("Ingrese dos numeros enteros")
    nro1=int(input('--> nro1: '))
    nro2=int(input('--> nro2: '))
    resultado=suma_lenta(nro1, nro2)
    print (f'El resultado es:{resultado}')
if __name__ =='__main__':
    principal ()
