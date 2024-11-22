import re
import random
import copy
from os import system

def convertir_csv_a_lista(path:str)->list:
    with open(path, "r", encoding="utf8") as archivo:
        lista_secuencias = []
        for fila in archivo:
            secuencia = re.split(",|\n",fila)
            secuencia.pop()
            lista_secuencias.append(secuencia)
    return lista_secuencias

def seleccionar_x_elementos_random_de_una_lista(lista_de_elementos:list, cantidad:int)->list:
    lista_random = []
    for _ in range(cantidad):
        elemento_random = random.randint(0, len(lista_de_elementos) - 1)
        lista_random.append(lista_de_elementos.pop(elemento_random))
    return lista_random

def desempaquetar_listas_a_tuplas(lista_de_listas:list)->list:
    lista_de_tuplas = []
    for lista in lista_de_listas:
        categoria = lista.pop(0)
        for elemento in lista:
            lista_de_tuplas.append((categoria, elemento))
    return lista_de_tuplas

def armar_matriz_inicial_juego(lista_de_tuplas:list, dimensiones_matriz)->list:
    matriz_juego = []
    lista_de_tuplas_copy = copy.deepcopy(lista_de_tuplas)
    for _ in range(dimensiones_matriz[0]):
        fila = seleccionar_x_elementos_random_de_una_lista(lista_de_tuplas_copy, dimensiones_matriz[1], True)
        matriz_juego.append(fila)
    return matriz_juego

# Interfaz

def calcular_dimensiones_matriz(matriz:list)->tuple:
    filas = len(matriz)
    columnas = len(matriz[0])
    return (filas, columnas)

def calcular_longitud_de_la_palabra_mas_larga_de_matriz(matriz:list)->int:
    palabra_mas_larga = len(matriz[0][1])
    for fila in matriz:
        for columna in fila:
            if len(columna[1]) > palabra_mas_larga:
                palabra_mas_larga = len(columna[1])
    return palabra_mas_larga

def imprimir_interfaz_matriz(matriz:list, espacios_ocupados:int, resueltas:list = [], seleccionadas:list = []):
    numerador = 1
    for fila in matriz:
        for columna in fila:
            print(f"\033[1;36m[{numerador}]\033[0m {columna[1]:{espacios_ocupados}}", end = "\t")
            numerador += 1
        print()


### Otras funciones

def falso_in(elemento_a_buscar:any, lugar_donde_buscar:any)->bool:
    resultado = False
    for elemento in lugar_donde_buscar:
        if elemento_a_buscar == elemento:
            resultado = True
    return resultado
