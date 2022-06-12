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

def sexadecimal_a_decimal (horas,minutos,segundos):
    '''
    Esta funcion pasa un numero de notacion sexadecimal a decimal
    '''
    if minutos>60 or segundos>60:
        print('Ingreso erroneo de minutos o segundos, intente de nuevo.')
        resultado=000
    elif horas<0 or minutos<0 or segundos<0:
        print('Ingreso erroneo de minutos o segundos, intente de nuevo')
        resultado=000
    else:
        suma_de_horas_y_minutos=(((horas*60)+minutos)*60)
        segundos_totales=(suma_de_horas_y_minutos + segundos)
        resultado=segundos_totales
    return resultado

def decimal_a_sexadecimal(numero):
    '''
    Esta funcion pasa un numero de notacion decimal a sexadecimal
    '''
    if numero<0:
        print('Ingreso erroneo del decimal, intente de nuevo')
        resultado=(0,0,0)
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
    print ("Pasaje de decimal a sexadecimal:")
    numero=int(input('ingrese un numero natural: '))
    print("")
    resultado=sexadecimal_a_decimal(horas, minutos, segundos)
    print (f'La conversion a segundos es: {resultado}')
    print("")
    resultado2=decimal_a_sexadecimal(numero)
    print (f'La conversion a horas, minutos y segundos es:{resultado2}')

if __name__ =='__main__':
    principal ()
