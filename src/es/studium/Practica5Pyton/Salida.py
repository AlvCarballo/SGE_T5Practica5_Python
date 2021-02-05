# coding: utf-8
'''
Created on 5 feb. 2021

@author: Alvca
'''
nombreFichero =input("Indique el nombre del fichero a abrir: ")
try:
    fichero = open (nombreFichero,'r')
except OSError:
    print('No se puede abrir el archivo', nombreFichero)
else:
    lines = []
    for line in fichero:
        lines.append(line)
    fichero.close()
    print('Hemos hacedido al archivo', nombreFichero, 'correctamente')