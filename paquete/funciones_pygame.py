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
            matriz_botones[i][j]["Contenido"] = matriz_juego[i][j]
            
    return matriz_botones


def mostrar_botones(matriz_botones,pantalla):
    for fila in matriz_botones:
        for columna in fila:
            dibujar_boton(columna,pantalla)    

def actualizar_fondo_boton(boton):
    if boton["Estado"]:
        boton["Color Fondo"] = "Green"
    else:
        boton["Color Fondo"] = "Grey"

def comprobar_colision_y_actualizar(lista_botones,evento):
    for boton in lista_botones:
        if boton["Rectangulo"].collidepoint(evento.pos):
            boton["Estado"] = not boton["Estado"]
            actualizar_fondo_boton(boton)
            print(boton["Contenido"])

def actualizar_estado_botones(matriz_botones:list,evento):
    for fila in matriz_botones:
        comprobar_colision_y_actualizar(fila,evento)

def deseleccionar_botones(matriz_botones):
    for fila in matriz_botones:
        for boton in fila:
            boton["Estado"] = False
            boton["Color Fondo"] = "Grey"

def agregar_categoria_seleccionada(lista_botones,categorias_seleccionadas):
    elementos_seleccionados = 0
    for boton in lista_botones:
        if boton["Estado"]:
            categorias_seleccionadas.add(boton["Contenido"][1])
            elementos_seleccionados += 1
    return elementos_seleccionados

def verificar_seleccion_correcta_y_actualizar(matriz_botones,stats):
    elementos_seleccionados = 0
    categorias_seleccionadas = set()
    for fila in matriz_botones:
        elementos_seleccionados += agregar_categoria_seleccionada(fila,categorias_seleccionadas)
    if len(categorias_seleccionadas) > 1:
        print("error")
        deseleccionar_botones(matriz_botones)
    elif elementos_seleccionados == 4:
        print("grupo acertado")
        deseleccionar_botones(matriz_botones)
        
