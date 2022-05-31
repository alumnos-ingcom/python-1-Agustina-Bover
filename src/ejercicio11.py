########
#Nombre - @Agustina-Bover
#UNRN Andina- Introducción a la Ingeniería en Computación
#Precondicion: Ingresar dos numeros enteros
#Precondicion: Determinar si un numero es multiplo de otro
########
'''
Escribir una función que indique con True si un número entero
es multiplo de otro, utilizando sumas y restas.
'''
def es_multiplo (numero, multiplo):
    '''
    Esta funcion define si dos numeros son multiples
    '''
    valor=False
    resultado=0
    while valor is False:
        numero=numero-multiplo
        if numero==0:
            resultado=1
        if resultado>0:
            valor=True
        else:
            valor=False
            if numero<0:
                break
    return valor
def principal():
    """
     Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    """
    print ("Ingresar dos numeros enteros positivos:")
    nro1=int(input('nro1--> '))
    nro2=int(input('nro2--> '))
    assert nro1>0 and nro2>0, "Se deben ingresar numeros positivos"
    print(f'{nro2} es multiplo de {nro1}? {es_multiplo(nro1,nro2)}')
if __name__ =='__main__':
    principal ()
