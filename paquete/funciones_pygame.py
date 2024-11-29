import pygame
from paquete.funciones_generales import *
from paquete.func_pygame_especificas import *
from paquete.funciones_especificas import *

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
    ancho_boton = 70
    alto_boton = 70
    espacio = 60 # Espacio entre botones (la mitad del margen)
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

def comprobar_colision_y_actualizar(lista_botones,evento):
    for boton in lista_botones:
        if boton["Rectangulo"].collidepoint(evento.pos) and boton["Acertado"] == False:
            boton["Estado"] = not boton["Estado"]
            actualizar_fondo_boton(boton)

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
    lista_posiciones = obtener_lista_posiciones((70,70),(800,800),100)
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
    print("correcto")
    for boton in seleccionados:
        boton["Color Fondo"] =  (21, 255, 0)
        boton["Acertado"] = True
    return matriz_botones

def obtener_posiciones_usadas(matriz_botones):
    set_pos_usadas = set()
    for fila in matriz_botones:
        for boton in fila:
            set_pos_usadas.add(boton["Posicion"])
    return set_pos_usadas

def obtener_posiciones_sin_usar(matriz_botones,lista_posiciones): #se devuelve la diferencia entre las posiciones que usa la matriz y todas las posiciones
    set_posiciones = set(lista_posiciones)
    set_pos_usadas = obtener_posiciones_usadas(matriz_botones)

    posiciones_libres = set_posiciones.difference(set_pos_usadas)
    lista_posiciones_libres = list(posiciones_libres)
    return lista_posiciones_libres

def asignar_posicion_libre_fila(posiciones_libres,nuevas_posiciones_acierto,fila):
    for boton in fila:
        if contiene(nuevas_posiciones_acierto,boton["Posicion"]) and boton["Acertado"] == False:
            boton["Posicion"] = posiciones_libres.pop(0) 
    return posiciones_libres

def asignar_posiciones_libres(matriz_botones,lista_posiciones,nuevas_posiciones_acierto): #si la posicion de algun elemento no acertado es igual a la de uno q si, se le asigna una ubicacion libre con pop
    posiciones_libres = obtener_posiciones_sin_usar(matriz_botones,lista_posiciones)
    for fila in matriz_botones:
        posiciones_libres = asignar_posicion_libre_fila(posiciones_libres,nuevas_posiciones_acierto,fila)
        print(posiciones_libres)
    return matriz_botones

def ordenar_botones_acertados(botones_acertados,lista_posiciones,aciertos_previos): #asigna las nuevas posiciones a los elementos correcto y devuelve esas posiciones tomadas en una lista
    nuevas_posiciones_acierto = []
    for i,boton in enumerate(botones_acertados):
        boton["Posicion"] = lista_posiciones[aciertos_previos * 4 + i]
        boton["Rectangulo"].topleft = boton["Posicion"]
        boton["Estado"] = False
        nuevas_posiciones_acierto.append(boton["Posicion"])
    return nuevas_posiciones_acierto

def reordenar_botones_acierto(matriz_botones,aciertos_previos,pantalla):

    botones_acierto = obtener_botones_seleccionados(matriz_botones)
    lista_posiciones_seleccionados = []
    for boton in botones_acierto:
        lista_posiciones_seleccionados.append(boton["Posicion"])
    lista_posiciones = obtener_lista_posiciones((70,70),pantalla,60)

    nuevas_posiciones_acierto = ordenar_botones_acertados(botones_acierto,lista_posiciones,aciertos_previos)
    
    matriz_botones = asignar_posiciones_libres(matriz_botones,lista_posiciones,nuevas_posiciones_acierto)

    return matriz_botones

def pedir_nombre_en_pantalla(tamaño_pantalla,ventana_principal):
    fuente = pygame.font.Font(None, 35)
    entrada_usuario = ""
    max_caracteres = 10
    mi_rect = pygame.Rect(0, 0, 150, 40)
    centro_pantalla = (tamaño_pantalla[0] // 2, tamaño_pantalla[1] // 2)
    mi_rect.center = centro_pantalla
    activar_entrada = False
    resultado = False
    while True:
        ventana_principal.fill("Black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mi_rect.collidepoint(event.pos):
                    activar_entrada = True
                else:
                    activar_entrada = False
            if event.type == pygame.KEYDOWN and activar_entrada:
                if event.key == pygame.K_BACKSPACE:
                    entrada_usuario = entrada_usuario[:-1]
                elif event.key == pygame.K_RETURN:
                    resultado = True 
                elif event.key == pygame.K_ESCAPE:
                    resultado = False
                elif len(entrada_usuario) < max_caracteres:
                    entrada_usuario += event.unicode

        if resultado:
            pygame.display.flip() 
            return entrada_usuario       
        
        pygame.draw.rect(ventana_principal, (255, 255, 255), mi_rect)
        
        print_texto = fuente.render(entrada_usuario, True, "Black")
        ventana_principal.blit(print_texto, (mi_rect.x + 5, mi_rect.y + 10))

        mensaje_inicio = fuente.render("Ingresa tu nombre", True, "Black", "White")
        rect_mensaje_inicio = mensaje_inicio.get_rect()
        rect_mensaje_inicio.center = (tamaño_pantalla[0] // 2 , (tamaño_pantalla[1] // 2) - 60)
        ventana_principal.blit(mensaje_inicio, rect_mensaje_inicio)
        pygame.display.flip()

def continuar_siguiente_nivel(tamaño_pantalla,ventana_principal,stats):
    fuente = pygame.font.Font(None, 35)

    centro_pantalla = (tamaño_pantalla[0] // 2, tamaño_pantalla[1] // 2)
    boton_continuar = crear_boton(ventana_principal,centro_pantalla,(70,70),path_imagen="imagenes/siguiente nivel.png")
    resultado = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_continuar["Rectangulo"].collidepoint(event.pos):
                    resultado = True                

        if resultado:
            pygame.display.flip() 
            return        
        boton_continuar["Color Fondo"] = (98, 255, 89)
        boton_continuar["Rectangulo"].center = boton_continuar["Posicion"]
        dibujar_boton(boton_continuar,ventana_principal)
        mensaje_inicio = fuente.render(f"Genial. Pasaste al nivel {stats["nivel"]}", True, "Black", "White")
        rect_mensaje_inicio = mensaje_inicio.get_rect()
        rect_mensaje_inicio.center = (tamaño_pantalla[0] // 2 , (tamaño_pantalla[1] // 2) - 60)
        ventana_principal.blit(mensaje_inicio, rect_mensaje_inicio)
        pygame.display.flip()  

def mostrar_stats_fin_juego():
    pass
