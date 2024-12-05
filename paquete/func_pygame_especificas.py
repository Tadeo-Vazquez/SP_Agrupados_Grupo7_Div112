import pygame

def crear_boton(pantalla, posicion, dimension, texto=None, fuente=None, path_imagen=None,accion = None):
    """
    Crea el "objeto" boton en un diccionario con sus diferentes atributos
    Se retorna el diccionario con los diferentes atributos del boton
    """
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
    """
    Muestra un boton por pantalla
    Args:
        boton(dict): "objeto" boton
        ventana_principal: la pantalla que se utiliza
    """
    if boton["Color Fondo"] != None:
        pygame.draw.rect(ventana_principal, boton["Color Fondo"], boton["Rectangulo"],border_radius=5)
    boton["Pantalla"].blit(boton["Superficie"], boton["Rectangulo"])

def dibujar_boton_texto(boton_texto):
    pygame.draw.rect(boton_texto["Pantalla"],"Red",boton_texto["Rectangulo"])
    boton_texto["Pantalla"].blit(boton_texto["Superficie"],boton_texto["Rectangulo"])

def dibujar_rectangulo(posX,posY,ancho,alto,color,ventana_principal):
    rect = pygame.Rect(posX,posY,ancho,alto)
    pygame.draw.rect(ventana_principal,color,rect)

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
    """
    Comprueba que la colision en cada boton y ejecuta la funcion del atributo "Accion" en caso de haber colision
    Args:
        lista_botones(list): lista de botones
        evento: evento disparado
    """
    for boton in lista_botones:
        if boton["Rectangulo"].collidepoint(evento.pos):
            boton["Accion"]()

def mostrar_botones_fila(fila,pantalla):
    """
    Muestra los botones de una lista de botones por pantalla
    Args:
        fila(list): lista de botones
        pantalla: la pantalla que se utiliza
    """
    for boton in fila:
        dibujar_boton(boton,pantalla)  

def mostrar_botones(matriz_botones,pantalla):
    """
    Muestra todos los botones que contiene una matriz de botones por pantalla
    Args:
        matriz_botones(list): matriz que contiene los botones
        pantalla: la pantalla que se utiliza
    """
    for fila in matriz_botones:
        mostrar_botones_fila(fila,pantalla)    

def actualizar_fondo_boton(boton):
    """
    Cambia el color de fondo de un boton dependiendo su "Estado"
    Args:
        boton(dict): diccionario de "objeto" boton con sus diferentes atributos
    """
    if boton["Estado"]:
        boton["Color Fondo"] = (56, 255, 245)
    else:
        boton["Color Fondo"] = "Grey"

def mostrar_imagen(ruta_imagen, ventana_principal, tamaño,posicion):
    """
    Muestra una imagen de fondo
    Args:
        ruta_imagen(str): path de la imagen
        ventana_principal: superficie donde se blitea la imagen
        tamaño(tuple): dimensiones
        posicion(tuple): posicion en la superficie
    """
    imagen = pygame.image.load(ruta_imagen)
    imagen = pygame.transform.scale(imagen,tamaño)  # Escalar la imagen al tamaño deseado
    ventana_principal.blit(imagen, posicion)  # Dibujar la imagen en la ventana

def deseleccionar_botones_fila(fila):
    """
    Devuelve los botones cuyo atributo "Acertado" es False a su estado inicial
    Args:
        fila(list): lista de botones
    """
    for boton in fila:
        if boton["Acertado"] == False:
            boton["Estado"] = False
            boton["Color Fondo"] = "Grey"
            boton["Rectangulo"].topleft = boton["Posicion"]

def deseleccionar_botones(matriz_botones):
    """
    Devuelve los botones cuyo atributo "Acertado" es False a su estado inicial
    Args:
        matriz_botones(list): matriz que contiene botones
    """
    for fila in matriz_botones:
        deseleccionar_botones_fila(fila)

def comprobar_colision_y_actualizar(lista_botones,evento):
    """
    Se comprueba la colision en cada boton de una lista y se actualiza su color de fondo en caso de haber colision
    Args:
        lista_botones(list): lista de botones
        evento: evento disparado
    """
    for boton in lista_botones:
        if boton["Rectangulo"].collidepoint(evento.pos) and boton["Acertado"] == False:
            boton["Estado"] = not boton["Estado"]
            actualizar_fondo_boton(boton)

def actualizar_estado_botones(matriz_botones:list,evento):
    """
    Actualiza en estado del boton relacionado con el evento
    Args:
        matriz_botones(list): matriz que contiene los botones
        evento: evento disparado
    """
    for fila in matriz_botones:
        comprobar_colision_y_actualizar(fila,evento)

def contar_seleccionados_fila(fila,elementos_seleccionados):
    """
    Cuenta la cantidad de botones de una fila cuyo atributo "Estado" sea True
    Args:
        fila(list): fila de botones
        elementos_seleccionados(int): contador de elementos seleccionados
    Retorna in un numero que representa la canidad de botones con atributo "Estado" igual a True
    """
    for boton in fila:
        if boton["Estado"]:
            elementos_seleccionados+=1
    return elementos_seleccionados

def contar_seleccionados(matriz_botones):
    """
    Cuenta la cantidad de botones de una matriz de botones cuyo atributo "Estado" es True
    Args:
        matriz_botones(list): matriz que contiene botones
    Devuelve la cantidad de botones seleccionados
    """
    elementos_seleccionados = 0
    for fila in matriz_botones:
        elementos_seleccionados = contar_seleccionados_fila(fila,elementos_seleccionados)
    return elementos_seleccionados

def agregar_categorias_fila(fila,categorias_seleccionadas):
    """
    Agrega la categoria del atributo "Contenido" (cuyo valor es una tupla) de un boton a un set cuando
    el atributo "Estado" del boton sea True
    Args:
        fila(list): fila de botones
        categorias_seleccionadas(set): set a donde se agrega la categoria
    """
    for boton in fila:
        if boton["Estado"] and boton["Acertado"] == False:
            categorias_seleccionadas.add(boton["Contenido"][1])
    return categorias_seleccionadas

def agregar_categorias_seleccionadas(matriz_botones):
    """
    Se agregan las categorias del atributo "Contenido" (cuyo valor es una tupla) de un boton a un set cuando 
    el atributo "Estado" del boton sea True
    Args:
        matriz_botones(list): matriz que contiene botones
    """
    categorias_seleccionadas = set()
    for fila in matriz_botones:
        categorias_seleccionadas = agregar_categorias_fila(fila,categorias_seleccionadas)
    return categorias_seleccionadas

def obtener_botones_seleccionados_fila(botones_seleccionados,fila):
    """
    Se obtienen de una lista los botones cuyo atributo "Estado" sea True
    Args:
        botones_seleccionados(list): lista donde se va a agregar los botones con "Estado" True
        fila(list): lista que contiene los botones
    """
    for boton in fila:
        if boton["Estado"]:
            botones_seleccionados.append(boton)
    return botones_seleccionados

def obtener_botones_seleccionados(matriz_botones):
    """
    Se obtienen de una matriz los botones cuyo atributo "Estado" sea True
    Args:
        matriz_botones(list): matriz que contiene botones
    Se retorna una lista con los botones cuyo atributo "Estado" sea True
    """
    botones_seleccionados = []
    for fila in matriz_botones:
        botones_seleccionados = obtener_botones_seleccionados_fila(botones_seleccionados,fila)
    return botones_seleccionados

def actualizar_botones_acierto(matriz_botones):
    """
    Cambia el color de los botones cuyo atributo "Estado" es True dentro de una matriz
    Args:
        matriz_botones(list): matriz que contiene botones
    """
    seleccionados = obtener_botones_seleccionados(matriz_botones)
    for boton in seleccionados:
        boton["Color Fondo"] =  (21, 255, 0)
        boton["Acertado"] = True
    return matriz_botones

def agregar_pos_usada_fila(fila,set_pos_usadas):
    """
    Se agrega el atributo "Posicion" de los botones de la fila ingresada
    Args:
        fila(list): fila de botones 
        set_pos_usadas(set): set de posiciones ya usadas 
    """
    for boton in fila:
        set_pos_usadas.add(boton["Posicion"])
    return set_pos_usadas

def obtener_posiciones_usadas(matriz_botones):
    """
    Se obtiene un set que contiene las posiciones ya usadas
    Args:
        matriz_botones(list): matriz que contiene botones
    Retorna un set de posiciones usadas
    """
    set_pos_usadas = set()
    for fila in matriz_botones:
        set_pos_usadas = agregar_pos_usada_fila(fila,set_pos_usadas)
    return set_pos_usadas

