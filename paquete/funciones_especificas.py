import re
import random

def verificar_append_lista(lista:list,elemento)->bool:
    resultado = None
    for elem in lista:
        if elemento == elem:
            resultado = True
            break
        else:
            resultado = False
    return resultado

def verificar_elemento_matriz(matriz:list,elemento:any)->bool:
    resultado = None
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if elemento == matriz[i][j]:
                resultado = True
                break
            else:
                resultado = False
        if resultado:
            break
    return resultado

def convertir_csv_lista(path:str)->list:
    with open(path, "r", encoding="utf8") as archivo:
        secuencias = []
        for fila in archivo:
            secuencia = re.split(",|\n",fila)
            secuencia.pop()
            secuencias.append(secuencia)
    return secuencias

def encontrar_posicion_disponible_matriz_random(matriz:list,cant_filas:int,cant_columnas:int) -> tuple:
    while True:
        fila = random.randint(0, cant_filas-1)
        columna = random.randint(0, cant_columnas-1)
        if matriz[fila][columna] == None:
            return fila, columna

def obtener_elemento_no_repetido(matriz_cargada:list, matriz_a_cargar:list)->tuple:
     while True:
        fila = random.randint(0, 3)
        columna = random.randint(2, 5)
        elemento = matriz_cargada[fila][columna], matriz_cargada[fila][1]
        if verificar_elemento_matriz(matriz_a_cargar, elemento) == False:
            return elemento