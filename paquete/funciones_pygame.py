import pygame
from paquete.funciones_generales import *
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


def crear_matriz_botones(matriz_juego:list, pantalla, tamaño_pantalla:tuple) -> list:
    ancho_boton = 60
    alto_boton = 60
    espacio = 100 # Espacio entre botones (la mitad del margen)
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
            matriz_botones[i][j] = crear_boton(pantalla, (posX, posY), (ancho_boton, alto_boton), path_imagen=f"imagenes/{matriz_juego[i][j][1]}/{matriz_juego[i][j][0]}.png")
            matriz_botones[i][j]["Contenido"] = matriz_juego[i][j]
            
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
    return botones_seleccionados

def reordenar_grupo_acertado(stats,matriz_botones):
    grupos_ordenados = stats["aciertos"]
    fila_actual = matriz_botones[grupos_ordenados]
    seleccionados = obtener_botones_seleccionados(matriz_botones)
    seleccionados.sort(key=lambda b: b["Posicion"][1])
    #region lambda
    # lambda b: Crea una función anónima que toma un argumento b. En este caso, b es un botón de la lista seleccionados.
    # b["Posicion"][1]: Dentro de la función anónima, se toma la propiedad Posicion del botón b, que se supone es una tupla o lista, y se accede al segundo valor (índice 1), que sería la posición vertical (y) del botón.
    # key=lambda b: b["Posicion"][1]: Este lambda se utiliza como función clave para ordenar. Es decir, cada elemento b de la lista seleccionados se ordenará según su valor en b["Posicion"][1] (la posición vertical).
    #endregion
    for i, boton in enumerate(seleccionados):
        boton["Posicion"], fila_actual[i]["Posicion"] = fila_actual[i]["Posicion"], boton["Posicion"]

        boton["Rectangulo"].topleft = boton["Posicion"]
        fila_actual[i]["Rectangulo"].topleft = fila_actual[i]["Posicion"]

        boton["Acertado"] = True
        boton["Color Fondo"] = "Blue"  # Cambiar el color de fondo
    # for fila in matriz_botones:
    #     for boton in fila:
    #         if boton["Estado"] and boton["Acertado"] == False:
    #             boton["Posicion"],fila_actual[ordenados]["Posicion"] =  fila_actual[ordenados]["Posicion"],boton["Posicion"]
    #             boton["Color Fondo"] = "Blue"
    #             boton["Rectangulo"].topleft = boton["Posicion"]
    #             fila_actual[ordenados]["Rectangulo"].topleft = fila_actual[ordenados]["Posicion"]
    #             boton["Acertado"] = True
    #             boton["Estado"] = False
    #             ordenados += 1
    #             if ordenados == 4:
    #                 break
    stats["aciertos"] += 1


def verificar_seleccion_correcta_y_actualizar(matriz_botones,stats):
    elementos_seleccionados = contar_seleccionados(matriz_botones)
    categorias_seleccionadas = set()
    for fila in matriz_botones:
        agregar_categoria_seleccionada(fila,categorias_seleccionadas)
    if len(categorias_seleccionadas) > 1:
        print("error")
        deseleccionar_botones(matriz_botones)
    elif elementos_seleccionados == 4:
        print("grupo acertado")
        categorias_seleccionadas = set()
        reordenar_grupo_acertado(stats,matriz_botones)
    
    return True
        
