from paquete.funciones_generales import *
from paquete.funciones_pygame import *
from os import system
import pygame

def jugar_agrupados()->None:
    valores_juego = inicializar_juego()
    matriz_desordenada,secuencias,matriz = valores_juego["matriz_desordenada"], valores_juego["secuencias"], valores_juego["matriz"]
    while valores_juego["flag_juego"]:
        imprimir_interfaz_matriz(matriz_desordenada,18,valores_juego["stats"]) #MOSTRAR LA MATRIZ DE ELEMENTOS
        lista_posiciones = pedir_4_posiciones(valores_juego["stats"]["aciertos"]*4+1,19) #PEDIR LAS 4 POSICIONES
        if verificar_ingreso_comodin(lista_posiciones[0],matriz_desordenada,valores_juego["stats"],valores_juego["comodines"]): #EJECUTAR COMODIN SI CORRESPONDE
            continue                                                                                                            #si se ejecuta se continua al siguiente bucle
        lista_cat_ingresadas = averiguar_4categorias_ingresadas(matriz_desordenada,lista_posiciones) #crear una lista con las categorias correspondientes segun las 4 posiciones ingresadas
        acierto = averiguar_coincidencia_4cat(lista_cat_ingresadas) #verifica si las 4 categorias coinciden (True) o si no (False)
#############################################MANEJAR EL ACIERTO O ERROR###############################################################
        if acierto:
            matriz_desordenada = reordenar_acierto_matriz(matriz_desordenada,valores_juego["stats"]["aciertos"],lista_cat_ingresadas[0])
            valor_acierto = manejar_aciertos(valores_juego["stats"])
            if valor_acierto == 1:
                secuencias,matriz,matriz_desordenada = reasignacion_matriz_juego(matriz_desordenada,secuencias,matriz)
            elif valor_acierto == 2:
                fin_juego = time.time()
                break
        else:
            valor_error = manejar_errores(valores_juego["stats"])
            if valor_error == 2:
                fin_juego = time.time()
                valores_juego["flag_juego"] = False
            elif valor_error == 1:
                secuencias,matriz,matriz_desordenada = reasignacion_matriz_juego(matriz_desordenada,secuencias,matriz)
        system("pause")
        system("cls")
###################################FIN DEL JUEGO. SACA PROMEDIO DE TIEMPO Y GUARDA DATOS EN JSON#######################################   
    promedio_tiempo_nivel = round((fin_juego - valores_juego["inicio_juego"]) / valores_juego["stats"]["nivel"])
    guardar_stats_json(valores_juego["stats"],promedio_tiempo_nivel,"StatsUser.json")

# jugar_agrupados()






























PANTALLA = 600,600
flag_juego = True
pygame.init()

ventana_principal = pygame.display.set_mode(PANTALLA)
pygame.display.set_caption("Juego prueba")
# boton_eifel = crear_boton(pantalla= ventana_principal,
#                     posicion= (40,40),
#                     dimension= (70,70),
#                     path_imagen="imagenes/eiffel.png")

# boton_cabildo = crear_boton(pantalla=ventana_principal,
#                             posicion= (200,40),
#                             dimension= (70,70),
#                             path_imagen="imagenes/cabildo.png")

# boton_texto = crear_boton(pantalla=ventana_principal,
#                             posicion= (500,500),
#                             dimension= (50,50),
#                             texto="Good job",
#                             fuente={"Fuente":"arial",
#                                     "Tamaño": 20,
#                                     "Color": "Red",
#                                     "Color fondo": "White"})

fuente = pygame.font.SysFont("arial",20)
texto = fuente.render("Ualala señor frances", False, "Blue", "White")

fondo = pygame.image.load("imagenes/fondo.jpeg").convert()
fondo = pygame.transform.scale(fondo, PANTALLA)

valores_juego = inicializar_juego()
matriz_desordenada,secuencias,matriz = valores_juego["matriz_desordenada"], valores_juego["secuencias"], valores_juego["matriz"]
stats = valores_juego["stats"]
matriz_botones = crear_matriz_botones(matriz_desordenada,ventana_principal,PANTALLA)

while flag_juego:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            flag_juego = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            actualizar_estado_botones(matriz_botones,evento)
    verificar_seleccion_correcta_y_actualizar(matriz_botones,stats)
    mostrar_botones(matriz_botones,ventana_principal)

    pygame.display.update()
    
    