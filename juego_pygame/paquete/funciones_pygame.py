import pygame
import time
from paquete.func_pygame_especificas import *
from paquete.funciones_generales import *
from paquete.funciones_especificas import *
from paquete.func_msj_pantalla import *

def inicializar_juego(tamaño_pantalla:tuple,ventana_principal) -> dict:
    flag_juego = True
    comodines = inicializar_comodines()
    inicio_juego = time.time()
    nombre_user = pedir_nombre_en_pantalla(tamaño_pantalla,ventana_principal) #cambiar por funcion de pygame
    secuencias = convertir_csv_lista("secuencias.csv")
    matriz = cargar_matriz_ordenada(secuencias, 4)
    matriz_desordenada = crear_matriz_4x4_desordenada(matriz)
    stats = crear_dict_stats(nombre_user)
    return {
        "flag_juego": flag_juego,
        "comodines": comodines,
        "inicio_juego": inicio_juego,
        "nombre_user": nombre_user,
        "secuencias": secuencias,
        "matriz": matriz,
        "matriz_desordenada": matriz_desordenada,
        "stats": stats
    }

def obtener_posiciones_fila(i:int,inicio_X:int,inicio_Y:int,tamaño_boton:tuple,espacio:int,lista_posiciones:list):
    for j in range(4):
        posX = inicio_X + j * (tamaño_boton[0] + espacio)
        posY = inicio_Y + i * (tamaño_boton[1] + espacio) 
        lista_posiciones.append((posX,posY))
    return lista_posiciones

def obtener_lista_posiciones(tamaño_boton:tuple,tamaño_pantalla:tuple,espacio:int):
    lista_posiciones = []
    total_boton_ancho = 4 * tamaño_boton[0] + 3 * espacio  # 4 botones + 3 espacios entre ellos
    total_boton_alto = 4 * tamaño_boton[1] + 3 * espacio
    inicio_X = (tamaño_pantalla[0] - total_boton_ancho) // 2  # Centrar horizontalmente
    inicio_Y = (tamaño_pantalla[1] - total_boton_alto) // 2 
    for i in range(4):
        lista_posiciones = obtener_posiciones_fila(i,inicio_X,inicio_Y,tamaño_boton,espacio,lista_posiciones)
    return lista_posiciones

def crear_fila_botones(matriz_botones,i,pantalla,ancho_boton, alto_boton,posiciones,pos,matriz_juego):
    for j in range(len(matriz_botones[i])):
        # Crear el botón (esto depende de cómo implementes crear_boton)
        matriz_botones[i][j] = crear_boton(pantalla, posiciones[pos], (ancho_boton, alto_boton), path_imagen=f"imagenes/{matriz_juego[i][j][1]}/{matriz_juego[i][j][0]}.png")
        matriz_botones[i][j]["Contenido"] = matriz_juego[i][j]
        pos += 1
    return matriz_botones

def crear_matriz_botones(matriz_juego:list, pantalla, tamaño_pantalla:tuple) -> list:
    ancho_boton = 100
    alto_boton = 100
    espacio = 50 # Espacio entre botones
    posiciones = obtener_lista_posiciones((ancho_boton,alto_boton),tamaño_pantalla,espacio)
    pos = 0
    matriz_botones = crear_matriz(4, 4, None)
    for i in range(len(matriz_botones)):
        matriz_botones = crear_fila_botones(matriz_botones, i, pantalla, ancho_boton, alto_boton, posiciones, pos, matriz_juego)
        pos += 4
    return matriz_botones

def actualizar_posicion_seleccionados(botones_seleccionados,lista_posiciones,grupos_ordenados):
    for i, boton in enumerate(botones_seleccionados):
        nueva_posicion = lista_posiciones[grupos_ordenados * 4 + i]
        boton["Posicion"] = nueva_posicion
        boton["Rectangulo"].topleft = nueva_posicion

def actualizar_posicion_fila_objetivo(matriz_botones,lista_posiciones_seleccionados,fila_objetivo):
    for i in range(4):
        matriz_botones[fila_objetivo][i]["Posicion"] = lista_posiciones_seleccionados[i]
        matriz_botones[fila_objetivo][i]["Rectangulo"].topleft = lista_posiciones_seleccionados[i]

def actualizar_posicion_botones(matriz_botones,grupos_ordenados): 
    lista_posiciones = obtener_lista_posiciones((100,100),(900,900),50)
    botones_seleccionados = obtener_botones_seleccionados(matriz_botones)
    lista_posiciones_seleccionados = []
    for boton in botones_seleccionados:
        lista_posiciones_seleccionados.append(boton["Posicion"])
    if botones_seleccionados != None and len(botones_seleccionados) == 4:
        actualizar_posicion_seleccionados(botones_seleccionados,lista_posiciones,grupos_ordenados)
        fila_objetivo = grupos_ordenados
        actualizar_posicion_fila_objetivo(matriz_botones,lista_posiciones_seleccionados,fila_objetivo)

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
    lista_posiciones = obtener_lista_posiciones((100,100),pantalla,50)
    nuevas_posiciones_acierto = ordenar_botones_acertados(botones_acierto,lista_posiciones,aciertos_previos)
    matriz_botones = asignar_posiciones_libres(matriz_botones,lista_posiciones,nuevas_posiciones_acierto)

    return matriz_botones

def verificar_acierto(matriz_botones):
    resultado = False
    if contar_seleccionados(matriz_botones) == 4 and len(agregar_categorias_seleccionadas(matriz_botones)) == 1:
        resultado = True
    return resultado

def agregar_botones_comodines(valores_juego,ventana_principal):
    posY = 270
    for i,dict_comodin in enumerate(valores_juego["comodines"]):
        comodin_boton = crear_boton(ventana_principal,(30,posY),(70,70),path_imagen=f"imagenes/{dict_comodin["Nombre"]}.png")
        valores_juego["comodines"][i]["Boton"] = comodin_boton
        valores_juego["comodines"][i]["Boton"]["Color Fondo"] = (136, 255, 231)
        posY += 150
    
    return valores_juego

def mostrar_comodines(valores_juego,ventana_principal):
    for comodin in valores_juego["comodines"]:
        dibujar_boton(comodin["Boton"],ventana_principal)

def seleccionar_comodines(valores_juego,evento):
    for comodin in (valores_juego["comodines"]):
        if comodin["Boton"]["Rectangulo"].collidepoint(evento.pos):
            comodin["Seleccionado"] = True

def verificar_uso_comodin(ventana_principal,valores_juego,matriz_juego):
    for comodin in valores_juego["comodines"]:
        if comodin["Seleccionado"] and comodin["Usado"] == False:
            comodin["Usado"] = True
            comodin["Boton"]["Color Fondo"] = (240, 102, 78)
            comodin["Boton"]["Seleccionado"] = False
            comodin["Comodin"](matriz_juego,valores_juego["stats"],ventana_principal)
        elif comodin["Seleccionado"]:
            comodin["Seleccionado"] = False


def pasar_al_siguiente_nivel(stats,valores_juego,ventana_principal,PANTALLA,matriz_desordenada,secuencias,matriz):
    secuencias,matriz,matriz_desordenada = reasignacion_matriz_juego(matriz_desordenada,secuencias,matriz)
    matriz_botones = crear_matriz_botones(matriz_desordenada,ventana_principal,PANTALLA)
    dibujar_rectangulo(100,0,700,60,(108, 34, 255),ventana_principal)
    if stats["nivel"] == 5:
        mensaje_pantalla_continuar(PANTALLA,ventana_principal,"Has ganado el juego!!!",(182, 255, 13),"imagenes/fondo3.jpg")
        valores_juego["flag_juego"] = False
    else:
        reasignacion_stats(True,stats)
        mensaje_pantalla_continuar(PANTALLA,ventana_principal,f"Genial! Pasaste al nivel {stats["nivel"]}","Green","imagenes/fondo3.jpg")
    
    return matriz_botones,secuencias,matriz,matriz_desordenada

def manejar_error(stats,ventana_principal,PANTALLA,matriz_desordenada,secuencias,matriz,filas_ordenadas,matriz_botones,valores_juego):
    reasignacion_stats(False,stats)
    deseleccionar_botones(matriz_botones)
    reproducir_sonido("sonidos/incorrecto.wav",0)
    dibujar_rectangulo(100,0,700,60,(108, 34, 255),ventana_principal)
    if stats["vidas nivel"] == 0:
        filas_ordenadas = 0
        reasignacion_stats(False,stats)
        mensaje_pantalla_continuar(PANTALLA,ventana_principal,"Has perdido el nivel :(","Red","imagenes/fondo3.jpg")
        secuencias,matriz,matriz_desordenada = reasignacion_matriz_juego(matriz_desordenada,secuencias,matriz)
        matriz_botones = crear_matriz_botones(matriz_desordenada,ventana_principal,PANTALLA)
    if stats["reinicios"] < 0:
        mensaje_pantalla_continuar(PANTALLA,ventana_principal,"Has perdido el juego :(","Red","imagenes/fondo3.jpg")
        valores_juego["flag_juego"] = False
    
    return matriz_botones,secuencias,matriz,matriz_desordenada,filas_ordenadas

def manejar_acierto(stats,valores_juego,ventana_principal,PANTALLA,matriz_desordenada,secuencias,matriz,matriz_botones,filas_ordenadas):
    reasignacion_stats(True,stats)
    matriz_botones = actualizar_botones_acierto(matriz_botones)
    matriz_botones = reordenar_botones_acierto(matriz_botones,filas_ordenadas,PANTALLA)
    filas_ordenadas += 1
    deseleccionar_botones(matriz_botones)
    if filas_ordenadas == 4:
        filas_ordenadas = 0
        matriz_botones,secuencias,matriz,matriz_desordenada = pasar_al_siguiente_nivel(stats,valores_juego,ventana_principal,PANTALLA,matriz_desordenada,secuencias,matriz)
    
    return matriz_botones,secuencias,matriz,matriz_desordenada,filas_ordenadas

def mostrar_interfaz(valores_juego,ventana_principal,matriz_botones,boton_configuracion):
    mostrar_stats(valores_juego["stats"],ventana_principal)
    mostrar_comodines(valores_juego,ventana_principal)
    mostrar_botones(matriz_botones,ventana_principal)
    dibujar_boton(boton_configuracion,ventana_principal)

def mostrar_stat(stat,ruta_imagen,ventana_principal,posX):
    posY = 10
    for _ in range(stat):
        mostrar_imagen(ruta_imagen,ventana_principal,(40,40),(posX,posY))
        posX += 40

def mostrar_stats(stats,ventana_principal):
    mostrar_mensaje_pantalla(f"{stats["puntaje"]} Pts",(180,30),ventana_principal,"fuentes/letra_pixelada2.ttf",20,(187, 255, 0))
    mostrar_stat(stats["vidas nivel"],"imagenes/corazon_vida.png",ventana_principal,280)
    mostrar_stat(stats["reinicios"], "imagenes/reinicio.png",ventana_principal,460)
    mostrar_mensaje_pantalla(f"Nivel {stats["nivel"]}",(690,30),ventana_principal,"fuentes/letra_pixelada2.ttf",20,(187, 255, 0))

def manejar_acierto_o_error(acierto,stats,valores_juego,ventana_principal,PANTALLA,matriz_desordenada,secuencias,matriz,matriz_botones,filas_ordenadas):
    if acierto:
        reproducir_sonido("sonidos/correcto.wav",0)
        mostrar_imagen("imagenes/fondo3.jpg",ventana_principal,PANTALLA,(0,0))
        matriz_botones,secuencias,matriz,matriz_desordenada,filas_ordenadas = manejar_acierto(stats,valores_juego,ventana_principal,PANTALLA,matriz_desordenada,secuencias,matriz,matriz_botones,filas_ordenadas)
    elif len(agregar_categorias_seleccionadas(matriz_botones)) > 1:
        mostrar_imagen("imagenes/fondo3.jpg",ventana_principal,PANTALLA,(0,0))
        matriz_botones,secuencias,matriz,matriz_desordenada,filas_ordenadas = manejar_error(stats,ventana_principal,PANTALLA,matriz_desordenada,secuencias,matriz,filas_ordenadas,matriz_botones,valores_juego)

    return matriz_botones,secuencias,matriz,matriz_desordenada,filas_ordenadas

def inicializar_ventana():
    PANTALLA = 900,900
    pygame.init()
    ventana_principal = pygame.display.set_mode(PANTALLA)
    pygame.display.set_caption("Juego prueba")
    mostrar_imagen("imagenes/fondo3.jpg",ventana_principal,PANTALLA,(0,0))
    return PANTALLA,ventana_principal

def manejar_eventos(valores_juego,matriz_botones,botones_musica,boton_configuracion,ventana_principal):
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            valores_juego["flag_juego"] = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            actualizar_estado_botones(matriz_botones,evento)
            seleccionar_comodines(valores_juego,evento)
            # checkear_accion_botones(botones_musica,evento)
            checkear_apertura_menu(evento,ventana_principal,boton_configuracion,botones_musica)

def bucle_principal_juego(valores_juego,matriz_botones,secuencias,matriz,matriz_desordenada,filas_ordenadas,ventana_principal,PANTALLA,botones_musica,boton_configuracion):
    while valores_juego["flag_juego"]:
        dibujar_rectangulo(100,0,700,60,(108, 34, 255),ventana_principal)
        manejar_eventos(valores_juego,matriz_botones,botones_musica,boton_configuracion,ventana_principal)
        acierto = verificar_acierto(matriz_botones)
        matriz_botones,secuencias,matriz,matriz_desordenada,filas_ordenadas = manejar_acierto_o_error(acierto,valores_juego["stats"],valores_juego,ventana_principal,PANTALLA,matriz_desordenada,secuencias,matriz,matriz_botones,filas_ordenadas)
        mostrar_interfaz(valores_juego,ventana_principal,matriz_botones,boton_configuracion)
        verificar_uso_comodin(ventana_principal,valores_juego,matriz_botones)
        pygame.display.update()

def crear_botones_sonido(pantalla):
    boton_subir_volumen = crear_boton(pantalla,(220,380),(100,100),path_imagen="imagenes/subir_volumen.png",accion=subir_volumen)
    boton_bajar_volumen = crear_boton(pantalla,(350,380),(100,100),path_imagen="imagenes/bajar_volumen.png",accion=bajar_volumen)
    boton_mutear = crear_boton(pantalla,(480,380),(100,100),path_imagen="imagenes/mutear_volumen.png",accion=mutear_volumen)
    boton_desmutear = crear_boton(pantalla,(610,380),(100,100),path_imagen="imagenes/desmutear_volumen.png",accion=desmutear_volumen)

    return [boton_subir_volumen,boton_bajar_volumen,boton_mutear,boton_desmutear]