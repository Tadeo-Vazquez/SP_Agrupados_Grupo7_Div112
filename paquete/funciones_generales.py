import re
import random

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

def verificar_append_lista(lista:list,elemento)->bool:
    resultado = None
    for elem in lista:
        if elemento == elem:
            resultado = True
            break
        else:
            resultado = False
    return resultado

def convertir_csv_lista(path:str)->list:
    with open(path, "r", encoding="utf8") as archivo:
        secuencias = []
        for fila in archivo:
            secuencia = re.split(",|\n",fila)
            secuencia.pop()
            secuencias.append(secuencia)
    return secuencias

def crear_lista_segun_dificultad(lista_secuencias:list,dificultad:str)->list:
    secuencias_dificultad = []
    for palabra in lista_secuencias:
        if palabra[0] == dificultad:
            secuencias_dificultad.append(palabra)
    return secuencias_dificultad

def cargar_matriz_ordenada(secuencias_dificultad:list,cantidad_secuencias:int)->list:
    matriz_secuencias_ordenadas = []
    for _ in range(cantidad_secuencias):
        secuencia_agregar = secuencias_dificultad[random.randint(0,len(secuencias_dificultad)-1)]
        while verificar_append_lista(matriz_secuencias_ordenadas,secuencia_agregar):
            secuencia_agregar = secuencias_dificultad[random.randint(0,len(secuencias_dificultad)-1)]
        matriz_secuencias_ordenadas.append(secuencia_agregar)
    return matriz_secuencias_ordenadas

def crear_matriz_secuencias(path:str,dificultad:str,cantidad_secuencias:int)->list:
    secuencias = convertir_csv_lista(path)
    secuencias_dificultad = crear_lista_segun_dificultad(secuencias,dificultad)
    matriz_secuencias_ordenadas = cargar_matriz_ordenada(secuencias_dificultad,cantidad_secuencias)
    return matriz_secuencias_ordenadas

def crear_matriz(filas:int,columnas:int,valor_inicial:any)->list:
    matriz = []
    for _ in range(filas):
        fila = [valor_inicial] * columnas
        matriz += [fila]
    return matriz

def encontrar_posicion_disponible_matriz(matriz:list,cant_filas:int,cant_columnas:int) -> tuple:
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

def cargar_matriz_desordenada(matriz_a_cargar:list,matriz_ordenada_origen:list,cantidad_elementos:int,cant_filas:int,cant_columnas:int)->list:
    for _ in range(cantidad_elementos):
        elemento_agregar = obtener_elemento_no_repetido(matriz_ordenada_origen,matriz_a_cargar)
        fila,columna = encontrar_posicion_disponible_matriz(matriz_a_cargar,cant_filas,cant_columnas)
        matriz_a_cargar[fila][columna] = elemento_agregar
    return matriz_a_cargar

def crear_matriz_4x4_desordenada(matriz_secuencias_ordenadas:list)->list:
    matriz_desordenada = crear_matriz(4,4,None)
    matriz_desordenada = cargar_matriz_desordenada(matriz_desordenada,matriz_secuencias_ordenadas,16,4,4)
    return matriz_desordenada

matriz = crear_matriz_secuencias("secuencias.csv","2",4)
for fila in matriz:
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
            print(matriz[i][j], end="\t")
        print()

matriz_desordenada = crear_matriz_4x4_desordenada(matriz)
for i in range(0,len(matriz_desordenada)):
    for j in range(0,len(matriz_desordenada[0])):
        print(f"Elem: {matriz_desordenada[i][j][0]} | Cat: {matriz_desordenada[i][j][1]}", end=" ||| ")
    print()




