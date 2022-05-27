########
#Nombre - @Agustina-Bover
#UNRN Andina- Introducción a la Ingeniería en Computación
#Precondicion: El ingreso de dos numeros enteros possitivos
#Postcondicion: Obtener el resto y cociente mediante la division lenta
#de estos numeros
########
"""
Escribir una función que mediante restas sucesivas, obtenga el
valor del cociente y resto de dos números enteros.
"""
def division_lenta_resto(dividendo, divisor):
    """
    Esta funcion, a traves de restas, nos devuelve el resto de la division
    """
    resultado=dividendo
    while resultado>=divisor:
        resultado-=divisor
    return resultado
def division_lenta_cociente(dividendo, divisor):
    """
    Esta funcion, a traves de restas, nos devuelve el cociente de la division
    """
    resultado=dividendo
    veces=0
    while resultado>=divisor:
        resultado-=divisor
        veces+=1
    return veces
def principal ():
    """
     Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    """
    print ("Ingrese dos numeros enteros positivos")
    nro1=int(input('--> nro1: '))
    nro2=int(input('--> nro2: '))
    print (f'El cociente es: {division_lenta_cociente(nro1,nro2)}')
    print (f'El resto es: {division_lenta_resto(nro1,nro2)}')
if __name__ =='__main__':
    principal ()
