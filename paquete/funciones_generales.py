from paquete.funciones_especificas import *
from paquete.funciones_input import *
from paquete.funciones_pygame import *
from os import system
import time

RED_TEXTO = '\033[91m'
GREEN_TEXTO = '\033[92m'
YELLOW_TEXTO = '\033[93m'
BLUE_TEXTO = '\033[94m'
MAGENTA_TEXTO = '\033[95m'
CYAN_TEXTO = '\033[96m'
RESET = '\033[0m'

def obtener_elemento_para_cargar(secuencias,matriz_secuencias_ordenadas):
    secuencia_agregar = secuencias[random.randint(0,len(secuencias)-1)]
    while contiene(matriz_secuencias_ordenadas,secuencia_agregar):
        secuencia_agregar = secuencias[random.randint(0,len(secuencias)-1)]
    # matriz_secuencias_ordenadas.append(secuencia_agregar)
    return secuencia_agregar

def cargar_matriz_ordenada(secuencias:list,cantidad_secuencias:int)->list:
    matriz_secuencias_ordenadas = []
    for _ in range(cantidad_secuencias):
        secuencia_agregar = obtener_elemento_para_cargar(secuencias,matriz_secuencias_ordenadas)
        matriz_secuencias_ordenadas.append(secuencia_agregar)
    return matriz_secuencias_ordenadas

def cargar_matriz_desordenada(matriz_a_cargar:list,matriz_ordenada_origen:list,cantidad_elementos:int,cant_filas:int,cant_columnas:int)->list:
    for _ in range(cantidad_elementos):
        elemento_agregar = obtener_elemento_no_repetido(matriz_ordenada_origen,matriz_a_cargar)
        fila,columna = encontrar_posicion_disponible_matriz_random(matriz_a_cargar,cant_filas,cant_columnas)
        matriz_a_cargar[fila][columna] = elemento_agregar
    return matriz_a_cargar

def crear_matriz_4x4_desordenada(matriz_secuencias_ordenadas:list)->list:
    matriz_desordenada = crear_matriz(4,4)
    matriz_desordenada = cargar_matriz_desordenada(matriz_desordenada,matriz_secuencias_ordenadas,16,4,4)
    return matriz_desordenada


def agregar_categoria_ingresada(contador,lista_categorias_ingresadas,numeros_ingresados,fila):
    for elemento in fila:        
        contador += 1
        if contiene(numeros_ingresados,contador):
            lista_categorias_ingresadas.append(elemento[1])
    return lista_categorias_ingresadas

def averiguar_4categorias_ingresadas(matriz_juego:int,numeros_ingresados:list)->list:
    contador = 0
    lista_categorias_ingresadas = []
    for fila in matriz_juego:
        lista_categorias_ingresadas = agregar_categoria_ingresada(contador,lista_categorias_ingresadas,numeros_ingresados,fila)
        contador += 4
    return lista_categorias_ingresadas

def averiguar_coincidencia_4cat(categorias_ingresadas:list)->bool:
    set_categorias_ingresadas = set(categorias_ingresadas)
    coincidencia = True
    if len(set_categorias_ingresadas) > 1:
        coincidencia = False
    return coincidencia
    

def pedir_posicion(lista_posiciones_int,minimo,maximo):
    uso_comodin = False
    posicion = get_number_int("Ingresa una posición del grupo: ",minimo,maximo)
    while contiene(lista_posiciones_int,posicion):
        print("Posición ya ingresada")
        posicion = get_number_int("Ingresa una posición del grupo: ",minimo,maximo)
    if posicion > 16:
        uso_comodin = True
    return posicion,uso_comodin

def pedir_4_posiciones(minimo:int,maximo:int)->list:
    lista_posiciones_int = []
    posiciones_pedidas = 4
    for _ in range(posiciones_pedidas):
        posicion,uso_comodin = pedir_posicion(lista_posiciones_int,minimo,maximo)
        if uso_comodin:
            lista_posiciones_int = [posicion]
            break
        lista_posiciones_int.append(posicion)
    return lista_posiciones_int

def mostrar_columna_matriz(columna,aciertos,numerador,espacios):
    if aciertos > 0:
        print(f"\033[1;36m[{numerador}]\033[0m \033[92m{columna[0]:{espacios}}\033[0m", end = "\t")
    else:
        print(f"\033[1;36m[{numerador}]\033[0m {columna[0]:{espacios}}", end = "\t")

def mostrar_fila_matriz(fila,aciertos,numerador,espacios):
    for columna in fila:
        mostrar_columna_matriz(columna,aciertos,numerador,espacios)
        numerador += 1

def imprimir_interfaz_matriz(matriz:list,espacios:int,stats:dict):
    numerador = 1
    aciertos = stats["aciertos"]
    for fila in matriz:
        mostrar_fila_matriz(fila,aciertos,numerador,espacios)
        numerador += 4
        aciertos -= 1
        print()
    mostrar_comodines()
    mostrar_stats(stats,espacios)


def intercambiar_elemento_acertado(matriz,categoría_acertada,ordenados,aciertos_previos,i,j):
    if matriz[i][j][1] == categoría_acertada:
        aux = matriz[aciertos_previos][ordenados]
        matriz[aciertos_previos][ordenados] = matriz[i][j]
        matriz[i][j] = aux
        ordenados += 1
    return matriz,ordenados

def reordenar_fila_acierto(matriz,ordenados,categoría_acertada,aciertos_previos,i):
    for j in range(len(matriz[0])):
        matriz,ordenados = intercambiar_elemento_acertado(matriz,categoría_acertada,ordenados,aciertos_previos,i,j)
    return matriz,ordenados

def reordenar_acierto_matriz(matriz:list,aciertos_previos:int,categoría_acertada:str)->list:
    ordenados = 0
    for i in range(len(matriz)):
        matriz,ordenados = reordenar_fila_acierto(matriz,ordenados,categoría_acertada,aciertos_previos,i)
    return matriz


def extraer_categorias_usadas_fila(fila,categorias_usadas):
    for columna in fila:
        if contiene(categorias_usadas,columna[1]) == False:
            categorias_usadas.append(columna[1])
    return categorias_usadas

def extraer_4_categorias_usadas(matriz_usada:list)->list:
    categorias_usadas = []
    for fila in matriz_usada:
        categorias_usadas = extraer_categorias_usadas_fila(fila,categorias_usadas)
    return categorias_usadas


def borrar_categoria_lista(categorias_usadas,secuencia,lista_secuencias):
    for categoria in categorias_usadas:
        if secuencia[0] == categoria:
            lista_secuencias.remove(secuencia)
    return lista_secuencias

def borrar_4_categorias_lista(categorias_usadas:list,lista_secuencias:list)->list:
    for secuencia in lista_secuencias:
        lista_secuencias = borrar_categoria_lista(categorias_usadas,secuencia,lista_secuencias)
    return lista_secuencias
   

def pedir_nombre_user(minimo_len:int,maximo_len:int)->str:
    nombre_user = input("Ingrese su nombre de usuario: ")
    while len(nombre_user) < minimo_len or len(nombre_user) > maximo_len:
        print("Longitud no permitida")
        nombre_user = input("Ingrese su nombre de usuario: ")
    return nombre_user


def mostrar_elemento_categoria(elemento_mostrar,fila,contador):
    for columna in fila:
        if contador == elemento_mostrar:
            print(f"El elemento {columna[0]} es de la categoria {columna[1]}")
        contador += 1

def comodin_mostrar_categoria(matriz_juego:list,aciertos:int)->None:
    elemento_mostrar = random.randint(aciertos*4+1,16)
    contador = 1
    for fila in matriz_juego:
        mostrar_elemento_categoria(elemento_mostrar,fila,contador)
        contador += 4


def buscar_emparejado_fila(fila,elemento1):
    elemento2 = None
    for columna in fila:
        if columna[1] == elemento1[1] and columna != elemento1:
            elemento2 = columna
    return elemento2

def comodin_emparejar_dos(matriz_juego:list, aciertos:int)->None:
    posicion_mostrar1 = random.randint(aciertos*4+1,16)
    elemento1 = obtener_elemento_segun_posicion(posicion_mostrar1,matriz_juego)
    for fila in matriz_juego:
        elemento2 = buscar_emparejado_fila(fila,elemento1)
        if elemento2 != None:
            break

    print(f"'{elemento1[0]}' y '{elemento2[0]}' son parte del mismo grupo")

def comodin_mostrar_elementos_1fila(matriz_juego:list, aciertos:int)->None:
    system("cls")
    for i in range(4):
        elemento_mostrar = obtener_elemento_segun_posicion(aciertos*4+i+1,matriz_juego)
        print(f"{elemento_mostrar[0]} es de la categoría {elemento_mostrar[1]}")
    time.sleep(3)
    system("cls")

def reasignacion_matriz_juego(matriz_usada:list,lista_secuencias:list,matriz_ordenada:list)->tuple:
    categorias_usadas = extraer_4_categorias_usadas(matriz_usada)
    secuencias = borrar_4_categorias_lista(categorias_usadas,lista_secuencias)
    matriz_ordenada = cargar_matriz_ordenada(secuencias,4)
    matriz_desordenada = crear_matriz_4x4_desordenada(matriz_ordenada)
    return secuencias,matriz_ordenada,matriz_desordenada

def ejecutar_comodin(comodin,matriz_juego:list,stats:dict,comodines:dict): #refactorizado usando dicts con funciones como valores
    posicion_comodin = comodin - 17
    if comodines[posicion_comodin]["Usado"]:
        print("Comodin ya usado")
    else:
        comodines[posicion_comodin]["Comodin"](matriz_juego,stats["aciertos"])
        comodines[posicion_comodin]["Usado"] = True

def paso_nivel(stats:dict):
    resultado = False
    if stats["aciertos"] == 4:
        resultado = True
    return resultado

def verificar_paso_nivel(stats):
    if stats["nivel"] == 5:
        print("Has ganado el juego")
        resultado = 2
    else:
        reasignacion_stats(True,stats)
        print(f"Ganaste. Pasaste al nivel {stats['nivel']}")
        resultado = 1
    return resultado

def manejar_aciertos(stats):
    reasignacion_stats(True,stats)
    print(GREEN_TEXTO + "Acertaste un grupo!" + RESET)
    resultado = 0
    if paso_nivel(stats):
        resultado = verificar_paso_nivel(stats)
    return resultado


def verificar_derrota_nivel(stats):
    print("Perdiste el nivel")
    resultado = 1
    if stats["reinicios"] == 0:
        print("Perdiste el juego")
        resultado = 2
    reasignacion_stats(False,stats)
    return resultado

def manejar_errores(stats):
    resultado = 0
    reasignacion_stats(False,stats)
    if stats["vidas nivel"] == 0:
        resultado = verificar_derrota_nivel(stats)
    else:
        print(f"{RED_TEXTO}Perdiste una vida. Te quedan {stats["vidas nivel"]}{RESET}")
    return resultado

#modularizar de aca a abajo
def inicializar_comodines():
    comodines = [{},{},{}]
    comodines[0]["Comodin"] = comodin_mostrar_categoria
    comodines[0]["Usado"] = False
    comodines[1]["Comodin"] = comodin_emparejar_dos
    comodines[1]["Usado"] = False
    comodines[2]["Comodin"] = comodin_mostrar_elementos_1fila
    comodines[2]["Usado"] = False
    return comodines


def inicializar_juego() -> dict:
    flag_juego = True
    comodines = inicializar_comodines()
    inicio_juego = time.time()
    nombre_user = pedir_nombre_user(3,15) #cambiar por funcion de pygame
    secuencias = convertir_csv_lista("secuencias.csv")
    matriz = cargar_matriz_ordenada(secuencias, 4)
    matriz_desordenada = crear_matriz_4x4_desordenada(matriz)
    stats = crear_dict_stats(nombre_user)
    return {
        "flag_juego": flag_juego,
        "comodines": comodines,
        "inicio_juego": inicio_juego,
        "nombre_user": nombre_user,
        "secuencias": secuencias,
        "matriz": matriz,
        "matriz_desordenada": matriz_desordenada,
        "stats": stats
    }

#funciones para reducir

def ejecutar_acierto(secuencias,matriz,matriz_usada,valores_juego,lista_cat_ingresadas):
    matriz_desordenada = reordenar_acierto_matriz(matriz_usada,valores_juego["stats"]["aciertos"],lista_cat_ingresadas[0])
    valor_acierto = manejar_aciertos(valores_juego["stats"])
    if valor_acierto == 1:
        secuencias,matriz,matriz_desordenada = reasignacion_matriz_juego(matriz_desordenada,secuencias,matriz)
    elif valor_acierto == 2:
        valores_juego["fin_juego"] = time.time()
        valores_juego["flag_juego"] = False

    return matriz_desordenada,secuencias,matriz

def ejecutar_error(valores_juego,secuencias,matriz,matriz_desordenada):
    valor_error = manejar_errores(valores_juego["stats"])
    if valor_error == 2:
        valores_juego["fin_juego"] = time.time()
        valores_juego["flag_juego"] = False
    elif valor_error == 1:
        secuencias,matriz,matriz_desordenada = reasignacion_matriz_juego(matriz_desordenada,secuencias,matriz)
    
    return secuencias,matriz,matriz_desordenada

def pedir_posiciones_y_ejecutar_comodin(valores_juego,matriz_desordenada):
    lista_posiciones = pedir_4_posiciones(valores_juego["stats"]["aciertos"]*4+1,19) #PEDIR LAS 4 POSICIONES
    ejecuto_comodin = False
    if lista_posiciones[0] > 16:
        ejecutar_comodin(lista_posiciones[0],matriz_desordenada,valores_juego["stats"],valores_juego["comodines"])
        pausar_y_limpiar_terminal()
        ejecuto_comodin = True              
    return lista_posiciones,ejecuto_comodin

def manejar_acierto_o_error(acierto,matriz_desordenada,secuencias,matriz,valores_juego,lista_cat_ingresadas):
    if acierto:
        matriz_desordenada,secuencias,matriz = ejecutar_acierto(secuencias,matriz,matriz_desordenada,valores_juego,lista_cat_ingresadas)
    else:
        secuencias,matriz,matriz_desordenada = ejecutar_error(valores_juego,secuencias,matriz,matriz_desordenada)

    return secuencias,matriz,matriz_desordenada