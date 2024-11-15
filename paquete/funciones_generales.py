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

def crear_matriz_4x4_desordenada(matriz_secuencias_ordenadas:list)->list:
    matriz_desordenada = crear_matriz(4,4,None)
    for _ in range(16):
        fila_agregar = random.randint(0,3)
        columna_agregar = random.randint(2,5)
        elemento_agregar = matriz_secuencias_ordenadas[fila_agregar][columna_agregar],matriz_secuencias_ordenadas[fila_agregar][1]
        while verificar_elemento_matriz(matriz_desordenada,elemento_agregar):
            fila_agregar = random.randint(0,3)
            columna_agregar = random.randint(2,5)
            elemento_agregar = matriz_secuencias_ordenadas[fila_agregar][columna_agregar],matriz_secuencias_ordenadas[fila_agregar][1]

        fila_agregar_desorden = random.randint(0,3)
        columna_agregar_desorden = random.randint(0,3)
        while matriz_desordenada[fila_agregar_desorden][columna_agregar_desorden] != None:
            fila_agregar_desorden = random.randint(0,3)
            columna_agregar_desorden = random.randint(0,3)
        matriz_desordenada[fila_agregar_desorden][columna_agregar_desorden] = elemento_agregar 
    return matriz_desordenada



matriz = crear_matriz_secuencias("secuencias.csv","2",4)
for fila in matriz:
    print(fila)

    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
            print(matriz[i][j], end="\t")
        print()

matriz_desordenada = crear_matriz_4x4_desordenada(matriz)
for i in range(0,len(matriz_desordenada)):
    for j in range(0,len(matriz_desordenada[0])):
        print(f"Elem: {matriz_desordenada[i][j][0]} | Cat: {matriz_desordenada[i][j][1]}", end=" ||| ")
    print()




