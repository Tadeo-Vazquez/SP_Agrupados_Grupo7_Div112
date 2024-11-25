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
            boton["Estado"] = True
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

def agregar_categoria_seleccionada(lista_botones,categorias_seleccionadas):
    elementos_seleccionados = 0
    for boton in lista_botones:
        if boton["Estado"] and boton["Acertado"] == False:
            categorias_seleccionadas.add(boton["Contenido"][1])
            elementos_seleccionados += 1
    return elementos_seleccionados

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

# def obtener_primera_fila_sin_acertar(matriz_botones):
#     fila_target = []
#     for fila in matriz_botones:
#         for boton in fila:
#             if not boton["Acertado"]:
#                 fila_target.append(boton)
#     return fila_target[:4]

def intercambiar_posiciones_elemento(elemento1,elemento2):
    auxPOS = elemento1["Posicion"]
    auxRECT = elemento1["Rectangulo"]
    elemento1["Posicion"] = copy.deepcopy(elemento2["Posicion"])
    elemento1["Rectangulo"] = copy.deepcopy(elemento2["Rectangulo"])
    elemento2["Posicion"] = auxPOS
    elemento2["Rectangulo"] = auxRECT

def actualizar_posicion_botones(matriz_botones,filas_ordenadas): #FUNCION MAL HECHA REVISAR
    elementos_ordenados = 0
    for i in range(len(matriz_botones)):
        for j in range(len(matriz_botones[0])):
            if matriz_botones[i][j]["Acertado"]:
                intercambiar_posiciones_elemento(matriz_botones[filas_ordenadas][elementos_ordenados],matriz_botones[i][j])
                elementos_ordenados += 1
                if elementos_ordenados == 4:
                    return

def comprobar_seleccionados_y_actualizar(matriz_botones,filas_ordenadas):
    seleccionados = obtener_botones_seleccionados(matriz_botones)
    categorias_seleccionadas = set()
    resultado = False
    for fila in matriz_botones:
        agregar_categoria_seleccionada(fila,categorias_seleccionadas)

    if len(categorias_seleccionadas) == 1:
        print("correcto")
        resultado = True
        for boton in seleccionados:
            boton["Color Fondo"] =  (0, 247, 255)
            boton["Acertado"] = True
            boton["Estado"] = False
        # actualizar_posicion_botones(matriz_botones,filas_ordenadas)
    else:
        deseleccionar_botones(matriz_botones)

    return resultado
        
