import pygame
from paquete.funciones_generales import *
import copy
def crear_boton(pantalla, posicion, dimension, texto=None, fuente=None, path_imagen=None):
    boton = {}
    boton["Pantalla"] = pantalla
    boton["Posicion"] = posicion
    boton["Dimension"] = dimension
    boton["Estado"] = False
    boton["Acertado"] = False
    boton["Color Fondo"] = "Grey"
    if path_imagen != None:
        imagen = pygame.image.load(path_imagen)
        boton["Superficie"] = pygame.transform.scale(imagen,boton["Dimension"])
    else:
        fuente_texto = pygame.font.SysFont(fuente["Fuente"],fuente["Tamaño"])
        boton["Superficie"] = fuente_texto.render(texto, False, fuente["Color"], fuente["Color fondo"],)
    boton["Rectangulo"] = boton["Superficie"].get_rect()
    boton["Rectangulo"].topleft = boton["Posicion"]
    return boton

def dibujar_boton(boton,ventana_principal):
    pygame.draw.rect(ventana_principal, boton["Color Fondo"], boton["Rectangulo"])
    boton["Pantalla"].blit(boton["Superficie"], boton["Rectangulo"])

def dibujar_boton_texto(boton_texto):
    pygame.draw.rect(boton_texto["Pantalla"],"Red",boton_texto["Rectangulo"])
    boton_texto["Pantalla"].blit(boton_texto["Superficie"],boton_texto["Rectangulo"])

def reproducir_sonido(path_sonido):
    pygame.mixer.init()
    pygame.mixer.music.load(path_sonido)
    pygame.mixer.music.play(1)

def obtener_lista_posiciones(tamaño_boton,tamaño_pantalla,espacio):
    lista_posiciones = []
    total_boton_ancho = 4 * tamaño_boton[0] + 3 * espacio  # 4 botones + 3 espacios entre ellos
    total_boton_alto = 4 * tamaño_boton[1] + 3 * espacio
    inicio_X = (tamaño_pantalla[0] - total_boton_ancho) // 2  # Centrar horizontalmente
    inicio_Y = (tamaño_pantalla[1] - total_boton_alto) // 2 
    for i in range(4):
        for j in range(4):
            posX = inicio_X + j * (tamaño_boton[0] + espacio)
            posY = inicio_Y + i * (tamaño_boton[1] + espacio) 
            lista_posiciones.append((posX,posY))
    return lista_posiciones

def crear_matriz_botones(matriz_juego:list, pantalla, tamaño_pantalla:tuple) -> list:
    ancho_boton = 60
    alto_boton = 60
    espacio = 100 # Espacio entre botones (la mitad del margen)
    posiciones = obtener_lista_posiciones((ancho_boton,alto_boton),tamaño_pantalla,espacio)
    pos = 0
    matriz_botones = crear_matriz(4, 4, None)
    for i in range(len(matriz_botones)):
        for j in range(len(matriz_botones[i])):
            # Crear el botón (esto depende de cómo implementes crear_boton)
            matriz_botones[i][j] = crear_boton(pantalla, posiciones[pos], (ancho_boton, alto_boton), path_imagen=f"imagenes/{matriz_juego[i][j][1]}/{matriz_juego[i][j][0]}.png")
            matriz_botones[i][j]["Contenido"] = matriz_juego[i][j]
            pos += 1
    return matriz_botones


def mostrar_botones(matriz_botones,pantalla):
    for fila in matriz_botones:
        for boton in fila:
            dibujar_boton(boton,pantalla)    

def actualizar_fondo_boton(boton):
    if boton["Estado"]:
        boton["Color Fondo"] = "Green"
    else:
        boton["Color Fondo"] = "Grey"

def comprobar_colision_y_actualizar(lista_botones,evento):
    for boton in lista_botones:
        if boton["Rectangulo"].collidepoint(evento.pos) and boton["Acertado"] == False:
            print(boton)
            boton["Estado"] = not boton["Estado"]
            actualizar_fondo_boton(boton)
            print(boton["Contenido"])


def actualizar_estado_botones(matriz_botones:list,evento):
    for fila in matriz_botones:
        comprobar_colision_y_actualizar(fila,evento)

def deseleccionar_botones(matriz_botones):
    for fila in matriz_botones:
        for boton in fila:
            if boton["Acertado"] == False:
                boton["Estado"] = False
                boton["Color Fondo"] = "Grey"
                boton["Rectangulo"].topleft = boton["Posicion"]

def contar_categorias_seleccionadas(matriz_botones):
    categorias_seleccionadas = set()
    for fila in matriz_botones:
        for boton in fila:
            if boton["Estado"] and boton["Acertado"] == False:
                categorias_seleccionadas.add(boton["Contenido"][1])
    return categorias_seleccionadas

def contar_seleccionados(matriz_botones):
    elementos_seleccionados = 0
    for fila in matriz_botones:
        for boton in fila:
            if boton["Estado"]:
                elementos_seleccionados+=1
    return elementos_seleccionados

def obtener_botones_seleccionados(matriz_botones):
    botones_seleccionados = []
    for fila in matriz_botones:
        for boton in fila:
            if boton["Estado"]:
                botones_seleccionados.append(boton)
    if len(botones_seleccionados) != 4:
        botones_seleccionados = None
    return botones_seleccionados

def actualizar_posicion_botones(matriz_botones,grupos_ordenados): #FUNCION MAL HECHA REVISAR
    lista_posiciones = obtener_lista_posiciones((60,60),(800,800),100)
    botones_seleccionados = obtener_botones_seleccionados(matriz_botones)
    lista_posiciones_seleccionados = []
    for boton in botones_seleccionados:
        lista_posiciones_seleccionados.append(boton["Posicion"])
    if botones_seleccionados != None and len(botones_seleccionados) == 4:
        for i, boton in enumerate(botones_seleccionados):
            nueva_posicion = lista_posiciones[grupos_ordenados * 4 + i]

            boton["Posicion"] = nueva_posicion
            boton["Rectangulo"].topleft = nueva_posicion

        fila_objetivo = grupos_ordenados
        for i in range(4):
            matriz_botones[fila_objetivo][i]["Posicion"] = lista_posiciones_seleccionados[i]
            matriz_botones[fila_objetivo][i]["Rectangulo"].topleft = lista_posiciones_seleccionados[i]



def actualizar_botones_acierto(matriz_botones):
    seleccionados = obtener_botones_seleccionados(matriz_botones)
    resultado = False
    if len(seleccionados) != 4:
        return False
    print("correcto")
    resultado = True
    for boton in seleccionados:
        boton["Color Fondo"] =  (0, 247, 255)
        boton["Acertado"] = True
    return resultado

def obtener_posiciones_sin_usar(matriz_botones,lista_posiciones):
    set_posiciones = set(lista_posiciones)
    set_pos_usadas = set()
    for fila in matriz_botones:
        for boton in fila:
            set_pos_usadas.add(boton["Posicion"])

    posiciones_libres = set_posiciones.difference(set_pos_usadas)
    lista_posiciones_libres = list(posiciones_libres)
    return lista_posiciones_libres


def reordenar_botones_acierto(matriz_botones,aciertos_previos):
    botones_acierto = obtener_botones_seleccionados(matriz_botones)
    lista_posiciones_seleccionados = []
    for boton in botones_acierto:
        lista_posiciones_seleccionados.append(boton["Posicion"])
    lista_posiciones = obtener_lista_posiciones((60,60),(800,800),100)
    nuevas_posiciones_acierto = []
    for i,boton in enumerate(botones_acierto):
        boton["Posicion"] = lista_posiciones[aciertos_previos * 4 + i]
        boton["Rectangulo"].topleft = boton["Posicion"]
        boton["Estado"] = False
        nuevas_posiciones_acierto.append(boton["Posicion"])
    
    posiciones_libres = obtener_posiciones_sin_usar(matriz_botones,lista_posiciones)

    for fila in matriz_botones:
        for boton in fila:
            if contiene(nuevas_posiciones_acierto,boton["Posicion"]) and boton["Acertado"] == False:
                boton["Posicion"] = posiciones_libres.pop(0)   

    return True
