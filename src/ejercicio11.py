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
    if numero<0 or multiplo<0:
        valor="Se deben ingresar numeros positivos. Intente nuevamente"
    else:
        valor=False
        resultado=0
        while not valor:
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
    resultado=es_multiplo(nro1,nro2)
    print(f'{nro2} es multiplo de {nro1}? {resultado}')
if __name__ =='__main__':
    principal ()
