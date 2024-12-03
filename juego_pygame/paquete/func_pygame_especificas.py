import pygame



def crear_boton(pantalla, posicion, dimension, texto=None, fuente=None, path_imagen=None,accion = None):
    boton = {}
    boton["Pantalla"] = pantalla
    boton["Posicion"] = posicion
    boton["Dimension"] = dimension
    boton["Estado"] = False
    boton["Acertado"] = False
    boton["Color Fondo"] = "Grey"
    boton["Accion"] = accion
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
    if boton["Color Fondo"] != None:
        pygame.draw.rect(ventana_principal, boton["Color Fondo"], boton["Rectangulo"],border_radius=5)
    boton["Pantalla"].blit(boton["Superficie"], boton["Rectangulo"])

def dibujar_boton_texto(boton_texto):
    pygame.draw.rect(boton_texto["Pantalla"],"Red",boton_texto["Rectangulo"])
    boton_texto["Pantalla"].blit(boton_texto["Superficie"],boton_texto["Rectangulo"])

def reproducir_sonido(path_sonido,veces):
    pygame.mixer.init()
    sonido = pygame.mixer.Sound(path_sonido)
    sonido.play(veces)

def reproducir_musica(path_musica,veces):
    pygame.mixer.init()
    pygame.mixer.music.load(path_musica)
    pygame.mixer.music.play(veces)

def subir_volumen():
    actual = pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(actual + 0.07)

def bajar_volumen():
    actual = pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(actual - 0.07)

def mutear_volumen():
    pygame.mixer.music.set_volume(0)

def desmutear_volumen():
    pygame.mixer.music.set_volume(0.3)


def checkear_accion_botones(lista_botones, evento):
    for boton in lista_botones:
        if boton["Rectangulo"].collidepoint(evento.pos):
            boton["Accion"]()

def mostrar_botones_fila(fila,pantalla):
    for boton in fila:
        dibujar_boton(boton,pantalla)  

def mostrar_botones(matriz_botones,pantalla):
    for fila in matriz_botones:
        mostrar_botones_fila(fila,pantalla)    

def actualizar_fondo_boton(boton):
    if boton["Estado"]:
        boton["Color Fondo"] = (56, 255, 245)
    else:
        boton["Color Fondo"] = "Grey"

def mostrar_imagen(ruta_imagen, ventana_principal, tamaño,posicion):
    imagen = pygame.image.load(ruta_imagen)
    imagen = pygame.transform.scale(imagen,tamaño)  # Escalar la imagen al tamaño deseado
    ventana_principal.blit(imagen, posicion)  # Dibujar la imagen en la ventana

def deseleccionar_botones_fila(fila):
    for boton in fila:
        if boton["Acertado"] == False:
            boton["Estado"] = False
            boton["Color Fondo"] = "Grey"
            boton["Rectangulo"].topleft = boton["Posicion"]

def deseleccionar_botones(matriz_botones):
    for fila in matriz_botones:
        deseleccionar_botones_fila(fila)

def comprobar_colision_y_actualizar(lista_botones,evento):
    for boton in lista_botones:
        if boton["Rectangulo"].collidepoint(evento.pos) and boton["Acertado"] == False:
            boton["Estado"] = not boton["Estado"]
            actualizar_fondo_boton(boton)

def actualizar_estado_botones(matriz_botones:list,evento):
    for fila in matriz_botones:
        comprobar_colision_y_actualizar(fila,evento)

def contar_seleccionados_fila(fila,elementos_seleccionados):
    for boton in fila:
        if boton["Estado"]:
            elementos_seleccionados+=1
    return elementos_seleccionados

def contar_seleccionados(matriz_botones):
    elementos_seleccionados = 0
    for fila in matriz_botones:
        elementos_seleccionados = contar_seleccionados_fila(fila,elementos_seleccionados)
    return elementos_seleccionados

def agregar_categorias_fila(fila,categorias_seleccionadas):
    for boton in fila:
        if boton["Estado"] and boton["Acertado"] == False:
            categorias_seleccionadas.add(boton["Contenido"][1])
    return categorias_seleccionadas

def agregar_categorias_seleccionadas(matriz_botones):
    categorias_seleccionadas = set()
    for fila in matriz_botones:
        categorias_seleccionadas = agregar_categorias_fila(fila,categorias_seleccionadas)
    return categorias_seleccionadas

def obtener_botones_seleccionados_fila(botones_seleccionados,fila):
    for boton in fila:
        if boton["Estado"]:
            botones_seleccionados.append(boton)
    return botones_seleccionados

def obtener_botones_seleccionados(matriz_botones):
    botones_seleccionados = []
    for fila in matriz_botones:
        botones_seleccionados = obtener_botones_seleccionados_fila(botones_seleccionados,fila)
    return botones_seleccionados

def actualizar_botones_acierto(matriz_botones):
    seleccionados = obtener_botones_seleccionados(matriz_botones)
    print("correcto")
    for boton in seleccionados:
        boton["Color Fondo"] =  (21, 255, 0)
        boton["Acertado"] = True
    return matriz_botones

def agregar_pos_usada_fila(fila,set_pos_usadas):
    for boton in fila:
        set_pos_usadas.add(boton["Posicion"])
    return set_pos_usadas

def obtener_posiciones_usadas(matriz_botones):
    set_pos_usadas = set()
    for fila in matriz_botones:
        set_pos_usadas = agregar_pos_usada_fila(fila,set_pos_usadas)
    return set_pos_usadas

