# coding=utf-8
"""
Problema No. 3
Convertir un valor numérico base 10 a su equivalente en base 2 (binario).

Autor: Jorge Luis Pérez Canto
Carné: 201024865
"""

#Entrada
num = int(input("Ingrese un número: "))
lista = []

#Proceso
while num >= 1:
    lista.insert(0, num%2)
    num = num //2
resultado = "".join(str(i) for i in lista)

#Salida
print("Número equivalente en binario: ", resultado)