import pygame
from paquete.funciones_generales import *
def crear_boton(pantalla, posicion, dimension, texto=None, fuente=None, path_imagen=None):
    boton = {}
    boton["Pantalla"] = pantalla
    boton["Posicion"] = posicion
    boton["Dimension"] = dimension
    boton["Estado"] = False
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

def dibujar_boton(boton):
    boton["Pantalla"].blit(boton["Superficie"], boton["Rectangulo"])

def dibujar_boton_texto(boton_texto):
    pygame.draw.rect(boton_texto["Pantalla"],"Red",boton_texto["Rectangulo"])
    boton_texto["Pantalla"].blit(boton_texto["Superficie"],boton_texto["Rectangulo"])

def reproducir_sonido(path_sonido):
    pygame.mixer.init()
    pygame.mixer.music.load(path_sonido)
    pygame.mixer.music.play(1)

# def crear_matriz_botones(matriz_juego:list,pantalla,tamaño_pantalla:tuple)->list:
#     posX = tamaño_pantalla[0] / 7 * 2
#     posY = tamaño_pantalla[1] / 7 * 2
#     matriz_botones = crear_matriz(4,4,None)
#     for i in range(len(matriz_botones)):
#         for j in range(len(matriz_botones[i])):
#             matriz_botones[i][j] = crear_boton(pantalla,(posX,posY),(60,60),path_imagen=f"imagenes/eiffel.png")
#             # matriz_botones[i][j] = crear_boton(pantalla,(posX,posY),(70,70),"aaaa",{"Fuente":"arial",
#             #                         "Tamaño": 20,
#             #                         "Color": "Red",
#             #                         "Color fondo": "White"})
#             posX += tamaño_pantalla[0] / 7
#         posX = tamaño_pantalla[0] / 7 * 2
#         posY += tamaño_pantalla[1] / 7 * 2
   
#     return matriz_botones

def crear_matriz_botones(matriz_juego:list, pantalla, tamaño_pantalla:tuple) -> list:
    ancho_boton = 60
    alto_boton = 60
    espacio = tamaño_pantalla[0] / 7 / 2 # Espacio entre botones (la mitad del margen)
    # Calcular el espacio total ocupado por los botones
    total_boton_ancho = 4 * ancho_boton + 3 * espacio  # 4 botones + 3 espacios entre ellos
    total_boton_alto = 4 * alto_boton + 3 * espacio   # 4 botones + 3 espacios entre ellos
    
    # Calcular la posición inicial para centrar la matriz
    inicio_X = (tamaño_pantalla[0] - total_boton_ancho) // 2  # Centrar horizontalmente
    inicio_Y = (tamaño_pantalla[1] - total_boton_alto) // 2  

    matriz_botones = crear_matriz(4, 4, None)
    
    for i in range(len(matriz_botones)):
        for j in range(len(matriz_botones[i])):
            posX = inicio_X + j * (ancho_boton + espacio)
            posY = inicio_Y + i * (alto_boton + espacio)
            
            # Crear el botón (esto depende de cómo implementes crear_boton)
            matriz_botones[i][j] = crear_boton(pantalla, (posX, posY), (ancho_boton, alto_boton), path_imagen="imagenes/eiffel.png")
            
    return matriz_botones


def mostrar_botones(matriz_botones,pantalla):
    for fila in matriz_botones:
        for columna in fila:
            dibujar_boton(columna)