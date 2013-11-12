#Programa que revisa cuales letras no se repiten de manera continua en
#una lista de palabras
#Elaborado por: Juan A. Escalante (10-10227)
#Para Devlabs-USB Tarea 1

import sys
dictionary  = open ("sowpods.txt")
archivo = dictionary.read()

def main():
    result = []
    # 65 hasta 90: Valores ASCII de las letras mayusculas.
    for x in range(65,91):    
        if(not( 2*(unichr(x)) in archivo)):
            result.append(unichr(x))   

    if(result):
        print 'Las letras que no se encuentran repetidas de manera continua son:'
        for letra in result:
            print letra
    else:
        print 'Todas las letras se repiten de manera continua al menos una vez'

main()
dictionary.close()
