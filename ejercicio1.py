"""
Problema No. 1
Solicitar un valor numérico entero y luego mostrar en pantalla las tablas de multiplicar
de informa inversa, desde el valor ingresado hasta el 1

Autor: Jorge Luis Pérez Canto
Carné: 201024865
"""
import sys

try:
    numero = int(input("Ingrese un número entero: "))
    while numero > 0:
        for i in range(10, 0, -1):
            print(numero, " * ", i, " = ", numero*i)
        print("")
        numero -= 1
except (ValueError, TypeError, IndexError):
    print("Tienes un error al introducir el número")
    print("El error fue: ", sys.exc_info()[0])
