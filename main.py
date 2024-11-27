from paquete.funciones_generales import *
from paquete.funciones_pygame import *
from os import system
import pygame

def jugar_agrupados()->None:
    valores_juego = inicializar_juego() #CREA UN DICT CON TODAS LAS ESTADISTICAS Y DATOS DEL JUEGO
    matriz_desordenada,secuencias,matriz = valores_juego["matriz_desordenada"], valores_juego["secuencias"], valores_juego["matriz"] #DESEMPAQUETAMOS ESTOS DATOS DEL DICT POR LEGIBILIDAD
    while valores_juego["flag_juego"]:
        imprimir_interfaz_matriz(matriz_desordenada,18,valores_juego["stats"]) #MUESTRA LA MATRIZ DEL JUEGO    
        lista_posiciones,ejecuto_comodin = pedir_posiciones_y_ejecutar_comodin(valores_juego,matriz_desordenada) #PIDE 4 POSICIONES Y SI ALGUNA ES UN COMODIN, LO EJECUTA
        if ejecuto_comodin: #SI SE EJECUTO UN COMODIN SE PASA AL SIGUIENTE BUCLE
            continue
        lista_cat_ingresadas = averiguar_4categorias_ingresadas(matriz_desordenada,lista_posiciones) #LISTA LAS CATEGORIAS INGRESADAS SEGUN LAS POSICIONES
        acierto = averiguar_coincidencia_4cat(lista_cat_ingresadas) #COMPARA LAS CATEGORIAS Y DEVUELVE SI ACERTO
        secuencias,matriz,matriz_desordenada = manejar_acierto_o_error(acierto,matriz_desordenada,secuencias,matriz,valores_juego,lista_cat_ingresadas) #REORDENA O CREA UNA MATRIZ NUEVA DEPENDIENDO LA CIRCUNSTANCIAS
        pausar_y_limpiar_terminal()
    finalizar_juego(valores_juego)#FIN DEL JUEGO. SACA PROMEDIO DE TIEMPO Y GUARDA DATOS EN JSON

jugar_agrupados()






























# PANTALLA = 800,800
# flag_juego = True
# pygame.init()

# ventana_principal = pygame.display.set_mode(PANTALLA)
# pygame.display.set_caption("Juego prueba")

# valores_juego = inicializar_juego()
# nombre_user = pedir_nombre_en_pantalla(PANTALLA,ventana_principal) #llamar funcion nombre user
# print(nombre_user)
# matriz_desordenada,secuencias,matriz = valores_juego["matriz_desordenada"], valores_juego["secuencias"], valores_juego["matriz"]
# stats = valores_juego["stats"]
# matriz_botones = crear_matriz_botones(matriz_desordenada,ventana_principal,PANTALLA)
# filas_ordenadas = 0
# fondo = pygame.image.load("imagenes/fondo.jpg")
# fondo = pygame.transform.scale(fondo,(PANTALLA))

# while flag_juego:
#     ventana_principal.blit(fondo,(0,0))
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             flag_juego = False
#         elif evento.type == pygame.MOUSEBUTTONDOWN:
#             actualizar_estado_botones(matriz_botones,evento)
#     # verificar_seleccion_correcta_y_actualizar
#     if contar_seleccionados(matriz_botones) == 4 and len(contar_categorias_seleccionadas(matriz_botones)) == 1:
#         matriz_botones = actualizar_botones_acierto(matriz_botones)
#         matriz_botones = reordenar_botones_acierto(matriz_botones,filas_ordenadas,PANTALLA)
#         filas_ordenadas += 1
#         deseleccionar_botones(matriz_botones)

#     if len(contar_categorias_seleccionadas(matriz_botones)) > 1:
#         print("Error")
#         deseleccionar_botones(matriz_botones)

#     if filas_ordenadas == 4:
#         filas_ordenadas = 0
#         secuencias,matriz,matriz_desordenada = reasignacion_matriz_juego(matriz_desordenada,secuencias,matriz)
#         matriz_botones = crear_matriz_botones(matriz_desordenada,ventana_principal,PANTALLA)
#         if stats["nivel"] == 5:
#             mostrar_stats_fin_juego()
#             flag_juego = False
#         else:
#             stats["nivel"] += 1
#             continuar_siguiente_nivel(PANTALLA,ventana_principal,stats)

#     mostrar_botones(matriz_botones,ventana_principal)
#     pygame.display.update()
    
    