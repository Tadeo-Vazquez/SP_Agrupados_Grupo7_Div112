from paquete.funciones_generales import *
from os import system

RED_TEXTO = '\033[91m'
GREEN_TEXTO = '\033[92m'
YELLOW_TEXTO = '\033[93m'
BLUE_TEXTO = '\033[94m'
MAGENTA_TEXTO = '\033[95m'
CYAN_TEXTO = '\033[96m'
RESET = '\033[0m'


def jugar_agrupados()->None:
    secuencias = convertir_csv_lista("secuencias.csv")
    matriz = crear_matriz_secuencias(secuencias,4)
    vidas_nivel = 3
    reinicios = 3
    aciertos = 0
    nivel = 1
    matriz_desordenada = crear_matriz_4x4_desordenada(matriz)
    while True:
        imprimir_interfaz_matriz(matriz_desordenada,18)
        if aciertos == 0:
            lista_posiciones = pedir_4_posiciones(1,16)
        else:
            lista_posiciones = pedir_4_posiciones(aciertos*4,16)
        lista_cat_ingresadas = averiguar_4categorias_ingresadas(matriz_desordenada,lista_posiciones)
        acierto = averiguar_coincidencia_4cat(lista_cat_ingresadas)
        if acierto:
            categoria_acertada = lista_cat_ingresadas[0]
            matriz_desordenada = reordenar_acierto_matriz(matriz_desordenada,aciertos,categoria_acertada)
            aciertos += 1
            print(GREEN_TEXTO + "Acertaste un grupo!" + RESET)
            if aciertos == 4:
                nivel += 1
                if nivel == 6:
                    print("Has ganado el juego")
                    break
                aciertos = 0
                secuencias = borrar_secuencias_usadas(secuencias,matriz_desordenada)
                matriz = crear_matriz_secuencias(secuencias,4)
                matriz_desordenada = crear_matriz_4x4_desordenada(matriz)
                print(f"Ganaste. Pasaste al nivel {nivel}")
        else:
            vidas_nivel -= 1
            if vidas_nivel == 0:
                print("Perdiste el nivel")
                reinicios -= 1
                break
            print(f"Perdiste una vida. Te quedan {vidas_nivel}")
        
        system("pause")
        system("cls")







jugar_agrupados()
# matriz = crear_matriz_secuencias("secuencias.csv",4)
# print(matriz)
# matriz_desordenada = crear_matriz_4x4_desordenada(matriz)
# print(matriz_desordenada)

# matriz = borrar_secuencias_usadas(matriz,matriz_desordenada)
# print(matriz)

# matriz_desordenada = crear_matriz_4x4_desordenada(matriz)
# print(matriz_desordenada)


# [1] Pizza               [2] Hamburguesa         [3] Sándwich            [4] Taco
# [5] Microondas          [6] Tostadora           [7] Nevera              [8] Lavadora
# [9] Natación            [10] Baloncesto         [11] Tenis              [12] Fútbol
# [13] Acción             [14] Comedia            [15] Terror             [16] Drama

# [1] Apple               [2] Samsung             [3] HP                  [4] Dell
# [5] Hidrógeno           [6] Oro                 [7] Plata               [8] Oxígeno
# [9] Pino                [10] Roble              [11] Secuoya            [12] Abeto
# [13] Samus              [14] Mario              [15] Link               [16] Sonic

# [1] Sudáfrica           [2] Nigeria             [3] Egipto              [4] Argelia
# [5] Marte               [6] Júpiter             [7] Mercurio            [8] Venus
# [9] Matemáticas         [10] Lengua             [11] Historia           [12] Geografía
# # [13] PortAventura       [14] Six Flags          [15] Disneyland         [16] Universal Studios

# [1] Torre Eiffel        [2] Gran Muralla        [3] Coliseo             [4] Cabildo
# [5] Hígado              [6] Cerebro             [7] Pulmón              [8] Corazón
# [9] Barco               [10] Tren               [11] Helicóptero        [12] Submarino
# [13] Hermana            [14] Padre              [15] Hermano            [16] Madre