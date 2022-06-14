########
#Nombre - @Agustina-Bover
#UNRN Andina- Introducción a la Ingeniería en Computación
#Precondicon: Ingresar 3 numeros sexadecimales y 1 numero decimal.
#Postcondicion: Obtener el pasaje de sexadecimal a decimal y de decimal
# a sexadecimal de los numeros ingresados
########
'''
Escribir un programa que permita transformar un número solicitado
expresado en grados, minutos y segundos a segundos a segundos.
Y otra que haga el cambio en el sentido contrario, devolviendo una tuple.
Recuerden que un grado son 60 minutos y un minuto son 60 segundos.
'''
class FechaException(Exception):
    '''
    Esta excepcion fue creada para controlar el buen ingreso de las variables.
    No se podran ingresar nros negativos, segundos>60 o minutos>60
    '''
    pass
def sexadecimal_a_decimal (horas,minutos,segundos):
    '''
    Esta funcion pasa un numero de notacion sexadecimal a decimal.
    En el caso de que el usuario ingrese un valor de manera erronea
    se interrumpira el programa
    '''
    if minutos>60:
        raise FechaException ('Minutos sobrepasan su limite (60)')
    elif segundos>60:
        raise FechaException ('Segundos sobrepasan su limite (60)')
    elif horas<0 or minutos<0 or segundos<0:
        raise FechaException ('Todos los numeros ingresados deberan ser positivos')
    suma_de_horas_y_minutos=(((horas*60)+minutos)*60)
    segundos_totales=(suma_de_horas_y_minutos + segundos)
    resultado=segundos_totales
    return resultado

def decimal_a_sexadecimal(numero):
    '''
    Esta funcion pasa un numero de notacion decimal a sexadecimal.
    En el caso de que el usuario ingrese un valor de manera erronea
    se interrumpira el programa
    '''
    if numero<0:
        raise FechaException ('El numero decimal ingresado debera ser positivos')
    else:
        segundos=(numero%60)
        minutos=((numero//60)%60)
        horas=(((numero//60)//60)%60)
        tupla=(horas, minutos, segundos)
        resultado=tupla
    return resultado
def principal():
    """
     Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    """
    print ("Pasaje de sexadecimal a decimal:")
    horas= int(input('Ingrese horas (numeros naturales)->'))
    minutos= int(input('Ingrese minutos->((numeros naturales))'))
    segundos= int(input('Ingrese segundos(numeros naturales)->'))
    print('')
    print ("Pasaje de decimal a sexadecimal:")
    numero=int(input('ingrese un numero natural: '))
    resultado=sexadecimal_a_decimal(horas, minutos, segundos)
    print ('')
    print (f'La conversion a segundos es: {resultado}')
    resultado2=decimal_a_sexadecimal(numero)
    print (f'La conversion a horas, minutos y segundos es:{resultado2}')

if __name__ =='__main__':
    principal ()
