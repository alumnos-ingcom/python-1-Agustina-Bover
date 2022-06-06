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
def convertir_a_fahrrenheit (centigrados):
    """
    Esta funcion se encarga de convertir una temperatura
    de grados centigrados a grados fahrentheit
    """
    resultado= (centigrados*9/5)+32
    return resultado

def convertir_a_centigrados (fahrenheit):
    """
    Esta funcion se encarga de convertir una temperatura
    de grados fahrentheit a grados centigrados
    """
    resultado= (fahrenheit-32)*5/9
    return resultado

def principal ():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    Se rendondean los valores para que no sean muy largos.
    """
    print('Ingrese °C (utilizando expresion decimal)')
    grados_centigrados=float(input(' --> Grados centigrados: '))
    print('Ingrese grados °F (utilizando expresion decimal)')
    grados_fahrenheit=float(input(' --> Grados fahrenheit: '))
    try:
        assert grados_fahrenheit>-459.67 and grados_centigrados>-273.5, "numero invalido"
        conversion0=convertir_a_fahrrenheit(grados_centigrados)
        conversion1=convertir_a_centigrados(grados_fahrenheit) 
        print(f'{grados_centigrados} °C son:{conversion0:.2f} °F')
        print(f'{grados_fahrenheit} °F son:{conversion1:.2f} °C')
    except:
        print ("Ese numero es menor al cero absoluto. Ingrese numero valido ")
        principal()

if __name__ =='__main__':
    principal ()
    