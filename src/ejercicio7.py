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
    suma_de_horas_y_minutos= (((horas*60)+minutos)*60)
    segundos_totales=(suma_de_horas_y_minutos + segundos)
    return segundos_totales
def decimal_a_sexadecimal(numero):
    '''
    Esta funcion pasa un numero de decimal a sexadecimal
    '''
    segundos=(numero%60)
    minutos=((numero//60)%60)
    horas=(((numero//60)//60)%60)
    tupla=(horas, minutos, segundos)
    return tupla
def principal():
    """
     Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    """
    print ("Pasaje de sexadecimal a decimal:")
    print('' '')
    horas= int(input('Ingrese horas (numeros naturales)->'))
    minutos= int(input('Ingrese minutos->((numeros naturales))'))
    assert minutos <60, "Error, 60 minutos o + ya son considerados horas"
    segundos= int(input('Ingrese segundos(numeros naturales)->'))
    assert segundos <60, "Error, 60 segundos o + ya son considerados minutos"
    print (f'La cantidad de segundos es: {sexadecimal_a_decimal(horas, minutos, segundos)}')
    print('' '')
    print ("Pasaje de decimal a sexadecimal:")
    numero=int(input('ingrese un numero natural: '))
    assert numero>0, "Debe ingresar un numero nartural"
    print (f'La cantidad de horas, minutos y segundos son: {decimal_a_sexadecimal(numero)}')
if __name__ =='__main__':
    principal ()
