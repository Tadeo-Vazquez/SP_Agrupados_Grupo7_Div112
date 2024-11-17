from paquete.funciones_especificas import *
from paquete.funciones_input import *

def crear_matriz_secuencias(path:str,cantidad_secuencias:int)->list:
    secuencias = convertir_csv_lista(path)
    matriz_secuencias_ordenadas = cargar_matriz_ordenada(secuencias,cantidad_secuencias)
    return matriz_secuencias_ordenadas

def cargar_matriz_ordenada(secuencias:list,cantidad_secuencias:int)->list:
    matriz_secuencias_ordenadas = []
    for _ in range(cantidad_secuencias):
        secuencia_agregar = secuencias[random.randint(0,len(secuencias)-1)]
        while verificar_append_lista(matriz_secuencias_ordenadas,secuencia_agregar):
            secuencia_agregar = secuencias[random.randint(0,len(secuencias)-1)]
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
    for _ in range(4):
        posicion = get_number_int("Ingresa una posición del grupo: ",minimo,maximo)
        while verificar_append_lista(lista_posiciones_int,posicion):
            print("Posición ya ingresada")
            posicion = get_number_int("Ingresa una posición del grupo: ",minimo,maximo)
        lista_posiciones_int.append(posicion)
    return lista_posiciones_int

matriz = crear_matriz_secuencias("secuencias.csv",4)
# for fila in matriz:
#     for i in range(0,len(matriz)):
#         for j in range(0,len(matriz[0])):
#             print(matriz[i][j], end="\t")
#         print()

def imprimir_interfaz_matriz(matriz:list, espacios_ocupados:int, resueltas:list = [], seleccionadas:list = []):
    numerador = 1
    for fila in matriz:
        for columna in fila:
            print(f"\033[1;36m[{numerador}]\033[0m {columna[0]:{espacios_ocupados}}", end = "\t")
            numerador += 1
        print()

def reordenar_acierto_matriz(matriz:list,aciertos_previos:int,categoría_acertada:str)->list:
    elementos_ordenados = 0
    




