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

def seleccionar_x_elementos_random_de_una_lista(lista_de_elementos:list, cantidad:int, modificar_lista: bool = False)->list:
    if not modificar_lista:
        lista_de_elementos = list(lista_de_elementos)
    lista_random = []
    for _ in range(cantidad):
        elemento_random = random.randint(0, len(lista_de_elementos) - 1)
        lista_random.append(lista_de_elementos.pop(elemento_random))
    return lista_random

def desempaquetar_listas_a_tuplas(lista_de_listas:list, modificar_lista: bool = False)->list:
    if not modificar_lista:
        lista_de_listas = copy.deepcopy(lista_de_listas)
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

def mostrar_matriz(matriz):
    for fila in matriz:
        for columna in fila:
            print(columna, end = "\t")
        print()

def agregar_posiciones_de_matriz_a_diccionario(dimensiones_matriz:tuple, diccionario:dict):
    string_matriz = f"{dimensiones_matriz[0]}X{dimensiones_matriz[1]}"
    diccionario["Estructura"][string_matriz] = {}
    contador_posicion = 1
    for fila in range(dimensiones_matriz[0]):
        for columna in range(dimensiones_matriz[1]):
            diccionario["Estructura"][string_matriz][str(contador_posicion)] = (fila, columna)
            contador_posicion += 1

def verificador_de_categorias(lista_de_tuplas:list)->bool:
    for tupla in lista_de_tuplas:
        if lista_de_tuplas[0][0] != tupla[0]:
            return False
    return True

def seleccionar_palabra_de_matriz(matriz:list, diccionario:dict, numero:str)->any:
    coordenadas = diccionario[numero]
    elemento = matriz[coordenadas[0]][coordenadas[1]]
    return elemento

def verificar_input_principal(cadena_ingresada:str, elementos_a_seleccionar:dict, elementos_ya_seleccionados:list, especiales:list, completados:int)->bool:
    if falso_in(cadena_ingresada, especiales):
        return True
    if falso_in(cadena_ingresada, elementos_a_seleccionar) and falso_in(cadena_ingresada, elementos_ya_seleccionados) == False:
        if int(cadena_ingresada) > completados:
            return True
    return False

def desempaquetar_matriz_a_set(matriz:list)->set:
    set_final = set()
    for fila in matriz:
        for columna in fila:
            set_final.add(columna)
    return set_final

def seleccionar_elementos_no_coincidentes_entre_matrices(matriz_1:list, matriz_2:list)->list:
    set_matriz_1 = desempaquetar_matriz_a_set(matriz_1)
    set_matriz_2 = desempaquetar_matriz_a_set(matriz_2)
    elementos_no_coincidentes = set_matriz_1.union(set_matriz_2)
    return list(elementos_no_coincidentes)


def armar_matriz_con_filas_correctas(matriz:list, elementos_a_agregar:list, filas_correctas:int, dimensiones:tuple):
    matriz_resultante = []
    if filas_correctas == 0:
        matriz_resultante.append(elementos_a_agregar)
    else:
        for i in range(filas_correctas):
            matriz_resultante.append(matriz[i])
        matriz_resultante.append(elementos_a_agregar)
    if len(matriz_resultante) != dimensiones[0]:
        elementos_no_coincidentes = seleccionar_elementos_no_coincidentes_entre_matrices(matriz, matriz_resultante)
        for _ in range(filas_correctas, dimensiones[0]):
            pass



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
    for elemento in lugar_donde_buscar:
        if elemento_a_buscar == elemento:
            return True
    return False


#agregar_posiciones_de_matriz_a_diccionario((4, 4), game_data)

#print(game_data)

#lista = convertir_csv_a_lista("secuencias.csv")
#lista_2 = crear_lista_segun_nivel(lista, "2")
#lista_3 = seleccionar_x_elementos_random_de_una_lista(lista_2, 4)
#lista_4 = desempaquetar_listas_a_tuplas(lista_3)

#matriz_1 = armar_matriz_inicial_juego(lista_4, (4,4))
#mostrar_matriz(matriz_1)
#interfaz_matriz(matriz_1, 17)


#print(lista_4)

def main():
    game_data = {
            "Estructura": {
            },
            }
    agregar_posiciones_de_matriz_a_diccionario((4,4), game_data)
    secuencias = convertir_csv_a_lista("secuencias.csv")
    nivel = 1
    # secuencias_de_nivel = crear_lista_segun_nivel(secuencias, "1")
    secuencias_seleccionadas = seleccionar_x_elementos_random_de_una_lista(secuencias, 4)
    elementos_para_matriz = desempaquetar_listas_a_tuplas(secuencias_seleccionadas)
    matriz_de_juego = armar_matriz_inicial_juego(elementos_para_matriz, (4,4))
    imprimir_interfaz_matriz(matriz_de_juego, 17)
    tuplas_seleccionadas = []
    input_principal_ingresados = []
    especiales = []
    while True:
        input_principal = input("Seleccione un elemento:")
        while not(verificar_input_principal(input_principal, game_data["Estructura"]["4X4"], input_principal_ingresados, especiales, 0)):
            print("valor invalido")
            input_principal = input("Seleccione un elemento:")
        input_principal_ingresados.append(input_principal)
        coordenadas_elemento_seleccionado = game_data["Estructura"]["4X4"][input_principal]
        tuplas_seleccionadas.append(matriz_de_juego[coordenadas_elemento_seleccionado[0]][coordenadas_elemento_seleccionado[1]])
        if len(tuplas_seleccionadas) > 1 and not(verificador_de_categorias(tuplas_seleccionadas)):
            print("Perdiste una vida")
            tuplas_seleccionadas.pop()
            continue
        if len(tuplas_seleccionadas) == 4 and verificador_de_categorias(tuplas_seleccionadas):
            print("victoria")
            break
            
        print(tuplas_seleccionadas)
        system("cls")

    


main()
