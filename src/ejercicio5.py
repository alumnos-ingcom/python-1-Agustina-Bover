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
def division_lenta(dividendo, divisor):
    """
    Esta funcion, a traves de restas, nos devuelve el resto de la division
    """
    if dividendo>0 and divisor>0:
        resto=dividendo
        cociente=0
        while resto>=divisor:
            resto-=divisor
            cociente+=1
        return cociente, resto
    if dividendo>0 and divisor<0:
        resto=dividendo
        cociente=0
        while resto>=abs(divisor):
            resto+=divisor
            cociente-=1
        return cociente, resto
    if dividendo<0 and divisor>0:
        resto=dividendo
        cociente=0
        while resto<=(divisor*-1):
            resto+=divisor
            cociente-=1
        return cociente, resto
    if dividendo<0 and divisor<0:
        resto=dividendo
        cociente=0
        while resto<=divisor:
            resto-=divisor
            cociente+=1
        return cociente, resto
      
def principal ():
    """
     Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    """
    print ("Ingrese dos numeros enteros")
    nro1=int(input('--> nro1: '))
    nro2=int(input('--> nro2: '))
    try:
        assert nro2!=0, 'No es posible dividir por 0'
        resultado=division_lenta(nro1,nro2)
        print (f'El cociente y resto es: {resultado}')
    except:
        print ('No es posible dividir por 0')
        principal()
if __name__ =='__main__':
    principal ()
