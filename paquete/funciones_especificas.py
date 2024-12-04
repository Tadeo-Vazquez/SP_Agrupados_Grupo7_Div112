import re
import random
import json
from os import system
import time
def contiene(lista:list,elemento)->bool:
    """verifica si un elemento esta cargado dentro de una lista
    Args:
        lista (list): lista a revisar 
        elemento (_type_): elemento a verificar su existencia en la lista
    Returns:
        bool: True si el elemento ya está en la lista y False si el elemento no está en la lista
    """
    resultado = False
    for elem in lista:
        if elemento == elem:
            resultado = True
            break
    return resultado

def verificar_elemento_matriz(matriz:list,elemento:any)->bool:
    """verifica si un elemento ya esta cargado dentro de una matriz
    Args:
        matriz (list): matriz a revisar
        elemento (any): elemento a buscar dentro de la matriz
    Returns:
        bool: True si el elemento ya está en la matriz y False si el elemento no está en la matriz
    """
    resultado = None
    for fila in matriz:
        resultado = contiene(fila,elemento) 
        if resultado:
            break
    return resultado

def convertir_csv_lista(path:str)->list:
    """recibe la ruta a un archivo csv y lo transforma a una lista, separando los elementos por comas
    Args:
        path (str): ruta del archivo csv
    Returns:
        list: lista creada segun el archivo
    """
    with open(path, "r", encoding="utf8") as archivo:
        secuencias = []
        for fila in archivo:
            secuencia = re.split(",|\n",fila)
            secuencia.pop()
            secuencias.append(secuencia)
    return secuencias

def encontrar_posicion_disponible_matriz_random(matriz:list,cant_filas:int,cant_columnas:int) -> tuple:
    """encuentra una posicion (fila,columna) random en la que el elemento sea None en una matriz
    Args:
        matriz (list): matriz a buscar la posicion
        cant_filas (int): filas de la matriz
        cant_columnas (int): columnas de la matriz
    Returns:
        tuple: devuelve una tupla con el numero de fila y columna de la matriz en la que el elemento sea None
    """
    while True:
        fila = random.randint(0, cant_filas-1)
        columna = random.randint(0, cant_columnas-1)
        if matriz[fila][columna] == None:
            return fila, columna

def obtener_elemento_no_repetido(matriz_cargada:list, matriz_a_cargar:list)->tuple:
    """obtiene un elemento random de una matriz cargada con para cargar en otra matriz verificando que no haya sido cargado ya
    Args:
        matriz_cargada (list): matriz de tuplas cargada
        matriz_a_cargar (list): matriz donde se quiere cargar el elemento de la primera matriz
    Returns:
        tuple: elemento de la primera matriz, que no está en la segunda
    """
    while True:
        fila = random.randint(0, 3)
        columna = random.randint(1, 4)
        elemento = matriz_cargada[fila][columna], matriz_cargada[fila][0]
        if verificar_elemento_matriz(matriz_a_cargar, elemento) == False:
            return elemento
        
def crear_matriz(filas:int,columnas:int,valor_inicial:any=None)->list:
    """crea una matriz vacia o con un valor inicial especificado
    Args:
        filas (int): cantidad de filas de la matriz a crear
        columnas (int): cantidad de columnas de la matriz a crear
        valor_inicial (any): valor inicial de cada elemento de la matriz. Por defecto None
    Returns:
        list: matriz creada
    """
    matriz = []
    for _ in range(filas):
        fila = [valor_inicial] * columnas
        matriz += [fila]
    return matriz

def obtener_elemento_fila(fila,posicion,contador):
    elemento = None
    for columna in fila:
        if contador == posicion:
            elemento = columna
        contador += 1
    return elemento

def obtener_elemento_segun_posicion(posicion:int, matriz_juego:list)->tuple:
    contador = 1
    for fila in matriz_juego:
        elemento = obtener_elemento_fila(fila,posicion,contador)
        if elemento != None:
            break
        contador += 4
    return elemento

def guardar_stats_json(stats:dict,tiempo:float,path:str)->None:
    usuario = {}
    usuario["Nombre Usuario"] = stats["nombre usuario"]
    usuario["Puntaje"] = stats["puntaje"]
    usuario["Nivel Alcanzado"] = stats["nivel"]
    usuario["Tiempo Promedio por Nivel"] = tiempo
    with open(path,"r") as archivo:
        datos = json.load(archivo)
    if type(datos) != list:
        datos = [datos]
    datos.append(usuario)
    with open(path,"w") as archivo:
        json.dump(datos,archivo,indent=4)

def reasigna_stats_pasar_nivel(stats)->dict:
    stats["vidas nivel"] = 3
    stats["nivel"] += 1
    stats["puntaje"] += 20
    stats["aciertos"] = 0
    return stats

def reasignar_stats_acierto(stats):
    stats["aciertos"] += 1
    stats["puntaje"] += 16
    return stats
    
def reasignar_stats_error(stats):
    stats["vidas nivel"] -= 1
    stats["puntaje"] -= 8
    return stats

def reasignar_stats_perdida(stats):
    stats["vidas nivel"] = 3
    stats["reinicios"] -= 1
    stats["aciertos"] = 0 
    return stats

def reasignacion_stats(acierto:bool,stats:dict)->dict: #sin usar: acortar codigo main
    """segun si acertó y la cantidad de aciertos o si falló y las vidas, reasigna las stats
    Args:
        acierto (bool): 
        vidas_nivel (int): 
        nivel (int): 
        score (int): 
        aciertos (int): 
        reinicios (int): 
    Returns:
        tuple: nivel,aciertos,score,vidas_nivel,reinicios
    """
    if acierto and stats["aciertos"] < 4:
        reasignar_stats_acierto(stats)
    elif acierto:
        reasigna_stats_pasar_nivel(stats)
    elif stats["vidas nivel"] > 0:
        reasignar_stats_error(stats)
    else:
        reasignar_stats_perdida(stats)
    return stats

def crear_dict_stats(nombre_user)->dict:
    """
    Crea el objeto "stats" como diccionario con las estadisticas de la partida del jugador como atributos
    Args:
        nombre_user(str): Nombre del usuario
    Retorna un diccionario con las estadisticas del jugador durante la partida
    """
    stats = {}
    stats["nombre usuario"] = nombre_user
    stats["puntaje"] = 0
    stats["vidas nivel"] = 3
    stats["reinicios"] = 3
    stats["aciertos"] = 0
    stats["nivel"] = 1
    return stats

def finalizar_juego(valores_juego):
    valores_juego["fin_juego"] = time.time()
    promedio_tiempo_nivel = round((valores_juego["fin_juego"] - valores_juego["inicio_juego"]) / valores_juego["stats"]["nivel"])
    guardar_stats_json(valores_juego["stats"],promedio_tiempo_nivel,"StatsUser.json")
