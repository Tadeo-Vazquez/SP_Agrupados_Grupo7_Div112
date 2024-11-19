from paquete.funciones_especificas import *
from paquete.funciones_input import *
from os import system
import time

RED_TEXTO = '\033[91m'
GREEN_TEXTO = '\033[92m'
YELLOW_TEXTO = '\033[93m'
BLUE_TEXTO = '\033[94m'
MAGENTA_TEXTO = '\033[95m'
CYAN_TEXTO = '\033[96m'
RESET = '\033[0m'

def cargar_matriz_ordenada(secuencias:list,cantidad_secuencias:int)->list:
    matriz_secuencias_ordenadas = []
    for _ in range(cantidad_secuencias):
        secuencia_agregar = secuencias[random.randint(0,len(secuencias)-1)]
        while verificar_append_lista(matriz_secuencias_ordenadas,secuencia_agregar):
            secuencia_agregar = secuencias[random.randint(0,len(secuencias)-1)]
        matriz_secuencias_ordenadas.append(secuencia_agregar)
    return matriz_secuencias_ordenadas

def crear_matriz_secuencias(secuencias,cantidad_secuencias:int)->list:
    # secuencias = convertir_csv_lista(path)
    matriz_secuencias_ordenadas = cargar_matriz_ordenada(secuencias,cantidad_secuencias)
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

def averiguar_4categorias_ingresadas(matriz_juego:int,numeros_ingresados:list)->list:
    contador = 0
    lista_categorias_ingresadas = []
    for i in range(len(matriz_juego)):
        for j in range(len(matriz_juego[0])):
            contador += 1
            for numero in numeros_ingresados:
                if contador == numero:   
                    lista_categorias_ingresadas.append(matriz_juego[i][j][1])
    return lista_categorias_ingresadas

def averiguar_coincidencia_4cat(categorias_ingresadas:list)->bool:
    coincidencia = True
    for i in range(1,len(categorias_ingresadas)):
        if categorias_ingresadas[i] != categorias_ingresadas[i-1]:
            coincidencia = False
    return coincidencia
    
def pedir_4_posiciones(minimo:int,maximo:int)->list:
    lista_posiciones_int = []
    posiciones_pedidas = 4
    for _ in range(posiciones_pedidas):
        posicion = get_number_int("Ingresa una posición del grupo: ",minimo,maximo)
        while verificar_append_lista(lista_posiciones_int,posicion):
            print("Posición ya ingresada")
            posicion = get_number_int("Ingresa una posición del grupo: ",minimo,maximo)
        if posicion > 16:
            lista_posiciones_int = [posicion]
            break
        lista_posiciones_int.append(posicion)
    return lista_posiciones_int

matriz = crear_matriz_secuencias("secuencias.csv",4)
# for fila in matriz:
#     for i in range(0,len(matriz)):
#         for j in range(0,len(matriz[0])):
#             print(matriz[i][j], end="\t")
#         print()

def mostrar_stats(nivel:int,vidas_nivel:int,reinicios:int,score:int,espacios)->None:
    print(f"\033[91mNivel: {nivel:<{espacios}}Vidas: {vidas_nivel:<{espacios}}Reinicios: {reinicios:<{espacios}}Puntaje: {score:<{espacios}} \033[0m")

def mostrar_comodines()->None:
    print(f"\033[95m[17]\033[0m Comodín: Mostrar 1 categoría", end = " ")
    print(f"\033[95m[18]\033[0m Comodín: Emparejar 2 Elementos", end = " ")
    print(f"\033[95m[19]\033[0m Comodín: Mostrar 4 categorias 3seg")

def imprimir_interfaz_matriz(matriz:list,espacios:int,score:int,vidas_nivel:int,reinicios:int,aciertos:int,nivel:int):
    numerador = 1
    for fila in matriz:
        for columna in fila:
            if aciertos > 0:
                print(f"\033[1;36m[{numerador}]\033[0m \033[92m{columna[0]:{espacios}}\033[0m", end = "\t")
            else:
                print(f"\033[1;36m[{numerador}]\033[0m {columna[0]:{espacios}}", end = "\t")
            numerador += 1
        aciertos -= 1
        print()
    mostrar_comodines()
    mostrar_stats(nivel,vidas_nivel,reinicios,score,espacios)

def reordenar_acierto_matriz(matriz:list,aciertos_previos:int,categoría_acertada:str)->list:
    elementos_ordenados = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j][1] == categoría_acertada:
                aux = matriz[aciertos_previos][elementos_ordenados]
                matriz[aciertos_previos][elementos_ordenados] = matriz[i][j]
                matriz[i][j] = aux
                elementos_ordenados += 1
    return matriz

def extraer_4_categorias_usadas(matriz_usada:list)->list:
    categorias_usadas = []
    for fila in matriz_usada:
        for columna in fila:
            if verificar_append_lista(categorias_usadas,columna[1]) == False:
                categorias_usadas.append(columna[1])
    return categorias_usadas

def borrar_4_categorias_lista(categorias_usadas:list,lista_secuencias:list)->list:
    for secuencia in lista_secuencias:
        for categoria in categorias_usadas:
            if secuencia[0] == categoria:
                lista_secuencias.remove(secuencia)
    return lista_secuencias
   
def pedir_nombre_user(minimo_len:int,maximo_len:int)->str:
    nombre_user = input("Ingrese su nombre de usuario: ")
    while len(nombre_user) < minimo_len or len(nombre_user) > maximo_len:
        print("Longitud no permitida")
        nombre_user = input("Ingrese su nombre de usuario: ")
    return nombre_user

def comodin_mostrar_categoria(matriz_juego:list,aciertos:int)->None:
    elemento_mostrar = random.randint(aciertos*4+1,16)
    contador = 1
    for fila in matriz_juego:
        for columna in fila:
            if contador == elemento_mostrar:
                print(f"El elemento {columna[0]} es de la categoria {columna[1]}")
            contador += 1

def comodin_emparejar_dos(matriz_juego:list, aciertos:int)->None:
    posicion_mostrar1 = random.randint(aciertos*4+1,16)
    elemento1 = obtener_elemento_segun_posicion(posicion_mostrar1,matriz_juego)
    for fila in matriz_juego:
        for columna in fila:
            if columna[1] == elemento1[1] and columna != elemento1:
                elemento2 = columna
    print(f"'{elemento1[0]}' y '{elemento2[0]}' son parte del mismo grupo")

def comodin_mostrar_elementos_1fila(matriz_juego:list,cant_segundos:int, aciertos:int)->None:
    system("cls")
    for i in range(4):
        elemento_mostrar = obtener_elemento_segun_posicion(aciertos*4+i+1,matriz_juego)
        print(f"{elemento_mostrar[0]} es de la categoría {elemento_mostrar[1]}")
    time.sleep(cant_segundos)
    system("cls")

def reasignacion_matriz_juego(matriz_usada:list,lista_secuencias:list)->tuple:
    categorias_usadas = extraer_4_categorias_usadas(matriz_usada)
    secuencias = borrar_4_categorias_lista(categorias_usadas,lista_secuencias)
    matriz = crear_matriz_secuencias(secuencias,4)
    matriz_desordenada = crear_matriz_4x4_desordenada(matriz)
    return secuencias,matriz,matriz_desordenada

def ejecutar_comodin(comodin:int,matriz_juego:list,aciertos:int,comodines:list):
    match comodin:
        case 17:
            if verificar_append_lista(comodines,17):
                comodin_mostrar_categoria(matriz_juego,aciertos)
                comodines.remove(17)
            else:
                print("Comodín ya usado")
        case 18:
            if verificar_append_lista(comodines,18):
                comodin_emparejar_dos(matriz_juego,aciertos)
                comodines.remove(18)
            else:
                print("Comodín ya usado")
        case 19:
            if verificar_append_lista(comodines,19):
                comodin_mostrar_elementos_1fila(matriz_juego,3,aciertos)
                comodines.remove(19)
            else:
                print("Comodín ya usado")
    return comodines





