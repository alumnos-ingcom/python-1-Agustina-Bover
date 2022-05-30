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
def convertir_fahrrenheit (centigrados):
    """
    Esta funcion se encarga de convertir una temperatura
    de grados centigrados a grados fahrentheit
    """
    if centigrados <-273.15:
        resultado="No existe temperatura"
        return resultado
    resultado= (centigrados*9/5)+32
    return resultado

def convertir_centigrados (fahrenheit):
    """
    Esta funcion se encarga de convertir una temperatura
    de grados fahrentheit a grados centigrados
    """
    if fahrenheit <-459.67:
        resultado="No existe temperatura"
        return resultado
    resultado= (fahrenheit-32)*5/9
    return round ((resultado),2)

def principal ():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    """
    print('Ingrese °C (utilizando expresion decimal)')
    grados_centigrados=float(input(' --> Grados centigrados: '))
    print('Ingrese grados °F (utilizando expresion decimal)')
    grados_fahrenheit=float(input(' --> Grados fahrenheit: '))

    print(f'{grados_centigrados} °C son: {convertir_fahrrenheit(grados_centigrados)} °F')
    print(f'{grados_fahrenheit} °F son: {convertir_centigrados(grados_fahrenheit)} °C')

if __name__ =='__main__':
    principal ()
    