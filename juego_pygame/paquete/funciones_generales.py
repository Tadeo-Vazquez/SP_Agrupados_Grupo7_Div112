from paquete.funciones_pygame import *
from paquete.func_pygame_especificas import *
from paquete.funciones_especificas import *
from os import system
import time

def mostrar_mensaje_pantalla(texto,posicion,ventana_principal,ruta_fuente,tamaño):
    fuente = pygame.font.Font(ruta_fuente, tamaño)
    texto_superficie = fuente.render(texto, False, "Black", "White")
    texto_rect = texto_superficie.get_rect(center=posicion)
    ventana_principal.blit(texto_superficie,texto_rect)

def obtener_elemento_para_cargar(secuencias,matriz_secuencias_ordenadas):
    secuencia_agregar = secuencias[random.randint(0,len(secuencias)-1)]
    while contiene(matriz_secuencias_ordenadas,secuencia_agregar):
        secuencia_agregar = secuencias[random.randint(0,len(secuencias)-1)]
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

def reasignacion_matriz_juego(matriz_usada:list,lista_secuencias:list,matriz_ordenada:list)->tuple:
    categorias_usadas = extraer_4_categorias_usadas(matriz_usada)
    secuencias = borrar_4_categorias_lista(categorias_usadas,lista_secuencias)
    matriz_ordenada = cargar_matriz_ordenada(secuencias,4)
    matriz_desordenada = crear_matriz_4x4_desordenada(matriz_ordenada)
    return secuencias,matriz_ordenada,matriz_desordenada

def mostrar_elemento_categoria(elemento_mostrar,fila,contador,ventana_principal,matriz_juego):
    resultado = None
    for boton in fila:
        if contador == elemento_mostrar and boton["Acertado"] == False:
            resultado = True
            deseleccionar_botones(matriz_juego)
            boton["Estado"] = True
            actualizar_fondo_boton(boton)
            mostrar_mensaje_pantalla(f"El elemento es de la categoria {boton['Contenido'][1]}",(400,10),ventana_principal,"fuentes/letra_pintura.ttf",35)
        contador += 1
    return resultado

def comodin_mostrar_categoria(matriz_juego:list,stats,ventana_principal)->None:
    posicion_mostrar = random.randint(1,16)
    boton_mostrar = obtener_elemento_segun_posicion(posicion_mostrar,matriz_juego)
    while boton_mostrar["Acertado"]:
        posicion_mostrar = random.randint(1,16)
        boton_mostrar = obtener_elemento_segun_posicion(posicion_mostrar,matriz_juego)
    deseleccionar_botones(matriz_juego)
    boton_mostrar["Estado"] = True
    actualizar_fondo_boton(boton_mostrar)
    mostrar_mensaje_pantalla(f"El elemento es de la categoria {boton_mostrar['Contenido'][1]}",(450,780),ventana_principal,"fuentes/letra_pintura.ttf",25)
    

def seleccionar_elemento_segun_categoria(fila,categoria_mostrar,boton):
    resultado = False
    for elemento in fila:
        if elemento["Contenido"][1] == categoria_mostrar and elemento != boton:
            elemento["Estado"] = True
            actualizar_fondo_boton(elemento)
            resultado = True
            break
    return resultado


def seleccionar_elemento_emparejado(boton,categoria_mostrar,matriz_botones):
    for fila in matriz_botones:
        resultado = seleccionar_elemento_segun_categoria(fila,categoria_mostrar,boton)
        if resultado:
            break

def seleccionar_elemento_segun_posicion_fila(contador,fila,posicion_mostrar1):
    resultado = False
    for boton in fila:
        if contador == posicion_mostrar1:
            boton["Estado"] = True
            resultado = True
            break
        contador += 1
    if resultado:
        return boton
    
def seleccionar_elemento_segun_posicion(matriz_juego,posicion_mostrar1):
    contador = 1
    boton = None
    for fila in matriz_juego:
        if seleccionar_elemento_segun_posicion_fila(contador,fila,posicion_mostrar1) != None:
            boton = seleccionar_elemento_segun_posicion_fila(contador,fila,posicion_mostrar1)
            actualizar_fondo_boton(boton)
            break
        contador += 4
    return boton

def comodin_emparejar_dos(matriz_juego:list, stats:int,ventana_principal)->None:
    posicion_mostrar1 = random.randint(stats["aciertos"]*4+1,16)
    boton_mostrar1 = obtener_elemento_segun_posicion(posicion_mostrar1,matriz_juego)
    while boton_mostrar1["Acertado"]:
        posicion_mostrar1 = random.randint(1,16)
        boton_mostrar1 = obtener_elemento_segun_posicion(posicion_mostrar1,matriz_juego)
    deseleccionar_botones(matriz_juego)
    boton = seleccionar_elemento_segun_posicion(matriz_juego,posicion_mostrar1)
    seleccionar_elemento_emparejado(boton,boton["Contenido"][1],matriz_juego)


def comodin_vida_extra(matriz_juego,stats,ventana_principal):
    stats["vidas nivel"] += 1

def crear_comodin(accion,nombre):
    comodin = {}
    comodin["Comodin"] = accion
    comodin["Usado"] = False
    comodin["Nombre"] = nombre
    comodin["Seleccionado"] = False
    return comodin

def inicializar_comodines():
    comodines = [{},{},{}]
    comodines[0] = crear_comodin(comodin_mostrar_categoria,"Mostrar categoría")
    comodines[1] = crear_comodin(comodin_emparejar_dos,"Emparejar 2")
    comodines[2] = crear_comodin(comodin_vida_extra,"Vida extra")
    return comodines



