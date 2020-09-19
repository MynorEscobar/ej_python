"""
Problema No. 2
Almacenar en una estructura de datos 10 textos, estos deberán ser ingresados por el usuario,
luego deberealizar lo siguiente:
* Mostrar los textos ingresados de forma inversa. (1 pt)
  Importante: si se ingresa el texto USAC deberá mostrar CASU
* Mostrar todos los textos que cuentan con 6 o más vocales. (1 pt)
* Mostrar el promedio de caracteres existentes en todos los textos. (0.5 pt)

Autor: Jorge Luis Pérez Canto
Carné: 201024865
"""
datos = []
datosInvertidos = []
cantidad_textos = 10

# Solicitar 10 textos
def solicitar_texto():
    for i in range(cantidad_textos): #10
        texto = input("Ingrese un texto: ")
        datos.append(texto)


def invertir_texto():
    print("\n\nTEXTOS INGRESADOS EN FORMA INVERSA: \n")
    for i in range(cantidad_textos):
        textoInvertido = ""
        for j in range(len(datos[i])):
            textoInvertido = datos[i][j] + textoInvertido
        datosInvertidos.append(textoInvertido)
    for i in range(cantidad_textos):
        print(datosInvertidos[i])


def vocales():
    print("\n\nTEXTOS QUE CUENTAN CON 6 O MÁS VOCALES\n")
    vocales = 'aeiouáéíóú'
    cantidad_vocales = 0
    for i in range(cantidad_textos):
        cantidad_vocales = len([c for c in datos[i].lower() if c in vocales])
        if (cantidad_vocales >= 6):
            print(datos[i], " \ttiene: ", cantidad_vocales, " vocales.")

def promedio():
    print("\n\nCantidad de veces que se repite cada caracter en cada texto:\n")
    diccionario = {}
    suma_caracteres = 0
    for i in range(cantidad_textos):
        for caracter in datos[i]:
            if caracter in diccionario:
                diccionario[caracter] = diccionario[caracter]+1
            else:
                diccionario[caracter] = 1
        suma_caracteres = len(datos[i])
        print(diccionario, "Cantidad de caracteres: ", len(datos[i]))
    promedio_caracteres = suma_caracteres / cantidad_textos
    print("PROMEDIO DE CARACTERES EN TODOS LOS TEXTOS: ", promedio_caracteres)

solicitar_texto()
invertir_texto()
vocales()
promedio()
