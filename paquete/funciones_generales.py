from paquete.funciones_especificas import *
from paquete.funciones_input import *

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

def cargar_matriz_desordenada(matriz_a_cargar:list,matriz_ordenada_origen:list,cantidad_elementos:int,cant_filas:int,cant_columnas:int)->list:
    for _ in range(cantidad_elementos):
        elemento_agregar = obtener_elemento_no_repetido(matriz_ordenada_origen,matriz_a_cargar)
        fila,columna = encontrar_posicion_disponible_matriz_random(matriz_a_cargar,cant_filas,cant_columnas)
        matriz_a_cargar[fila][columna] = elemento_agregar
    return matriz_a_cargar

def crear_matriz_4x4_desordenada(matriz_secuencias_ordenadas:list)->list:
    matriz_desordenada = crear_matriz(4,4,None)
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
        lista_posiciones_int.append(posicion)
    return lista_posiciones_int

matriz = crear_matriz_secuencias("secuencias.csv","1",4)
# for fila in matriz:
#     for i in range(0,len(matriz)):
#         for j in range(0,len(matriz[0])):
#             print(matriz[i][j], end="\t")
#         print()

matriz_desordenada = crear_matriz_4x4_desordenada(matriz)
contador = 0
for i in range(0,len(matriz_desordenada)):
    for j in range(0,len(matriz_desordenada[0])):
        contador += 1
        print(f"{contador}_Elem: {matriz_desordenada[i][j][0]} | Cat: {matriz_desordenada[i][j][1]}", end=" ||| ")
    print()

lista_posiciones = pedir_4_posiciones(1,16)
print(lista_posiciones)

lista_cat_ingresadas = averiguar_4categorias_ingresadas(matriz_desordenada,lista_posiciones)
print(lista_cat_ingresadas)

acierto = averiguar_coincidencia_4cat(lista_cat_ingresadas)

