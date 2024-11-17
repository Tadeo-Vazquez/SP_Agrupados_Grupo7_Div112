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
