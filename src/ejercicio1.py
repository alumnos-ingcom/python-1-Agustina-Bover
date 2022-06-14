########
#Nombre - @Agustina-Bover
#UNRN Andina- Introducción a la Ingeniería en Computación
#Precondicion: El ingreso de dos numeros decimales
#Postcondicion: El pasaje de esos numeros a grados fahrrenheit y centigraods
########
"""
Se quiere transformar temperaturas en grados fahrenheit a grados centígrados y viceversa.
Escribir las funciones para convertir la temperatura en grados centigrados en fahrenheit
como un número decimal,utilice esta formula para calcular los grados centígrados y retorne
el resultado obtenido. Y viceversa.
"""
class CeroAbsolutoException(Exception):
    '''
    Esta excepcion esta creada para el caso de que el usuario ingrese un valor menor
    al cero absoluto. (-273.5 en grados centigrados y -459.67 en grados fahrrenheit)
    '''
    pass

def convertir_a_fahrrenheit (centigrados):
    """
    Esta funcion se encarga de convertir una temperatura
    de grados centigrados a grados fahrentheit. En el caso de que la temperatura sea menor
    al cero absoluto el programa parará
    """
    if centigrados<-273.5:
        raise CeroAbsolutoException ('Los grados centigrados ingresados son menor al cero absoluto(-273.5). Intente de nuevo')
    resultado= (centigrados*9/5)+32
    return resultado


def convertir_a_centigrados (fahrenheit):
    """
    Esta funcion se encarga de convertir una temperatura
    de grados fahrentheit a grados centigrados. En el caso de que la temperatura sea menor
    al cero absoluto el programa parará
    """
    if fahrenheit<-459.67:
        raise CeroAbsolutoException ('Los grados fahrenheit ingresados son menor al cero absoluto(-459.67). Intente de nuevo')
    resultado= (fahrenheit-32)*5/9
    return resultado

def principal ():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    Se rendondean los valores para que no sean muy largos.
    """
    grados_centigrados=float(input(' --> Ingrese grados centigrados: '))
    grados_fahrenheit=float(input(' --> Ingrese grados fahrenheit: '))
    conversion0=convertir_a_fahrrenheit(grados_centigrados)
    conversion1=convertir_a_centigrados(grados_fahrenheit)
    print (f'La conversion a fahrrenheit es: {conversion0}')
    print (f'La conversion a grados es: {conversion1}')

if __name__ =='__main__':
    principal ()
    