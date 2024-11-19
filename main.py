from paquete.funciones_generales import *
from os import system

def jugar_agrupados()->None:
    comodines = [17,18,19]
    inicio_juego = time.time()
    nombre_user = pedir_nombre_user(3,20)
    secuencias = convertir_csv_lista("secuencias.csv")
    matriz = cargar_matriz_ordenada(secuencias,4)
    matriz_desordenada = crear_matriz_4x4_desordenada(matriz)
    puntaje = 0
    vidas_nivel = 3
    reinicios = 3
    aciertos = 0
    nivel = 1
    while True:
        imprimir_interfaz_matriz(matriz_desordenada,18,puntaje,vidas_nivel,reinicios,aciertos,nivel)
        lista_posiciones = pedir_4_posiciones(aciertos*4+1,19)
        
        if lista_posiciones[0] > 16:
            comodines = ejecutar_comodin(lista_posiciones[0],matriz_desordenada,aciertos,comodines)
            system("pause")
            system("cls")
            continue

        lista_cat_ingresadas = averiguar_4categorias_ingresadas(matriz_desordenada,lista_posiciones)
        acierto = averiguar_coincidencia_4cat(lista_cat_ingresadas)
        if acierto:
            categoria_acertada = lista_cat_ingresadas[0]
            matriz_desordenada = reordenar_acierto_matriz(matriz_desordenada,aciertos,categoria_acertada)
            aciertos += 1
            puntaje += 16
            print(GREEN_TEXTO + "Acertaste un grupo!" + RESET)
            if aciertos == 4:
                if nivel == 5:
                    fin_juego = time.time()
                    print("Has ganado el juego")
                    break
                vidas_nivel = 3
                nivel += 1
                puntaje += 20
                aciertos = 0
                secuencias,matriz,matriz_desordenada = reasignacion_matriz_juego(matriz_desordenada,secuencias)
                print(f"Ganaste. Pasaste al nivel {nivel}")
        else:
            vidas_nivel -= 1
            puntaje -= 8
            if vidas_nivel == 0:
                print("Perdiste el nivel")
                if reinicios == 0:
                    print("Perdiste el juego")
                    fin_juego = time.time()
                    break
                vidas_nivel = 3
                reinicios -= 1
                aciertos = 0
                puntaje -= 16
                secuencias,matriz,matriz_desordenada = reasignacion_matriz_juego(matriz_desordenada,secuencias)
            else:
                print(f"{RED_TEXTO}Perdiste una vida. Te quedan {vidas_nivel}{RESET}")
            
        system("pause")
        system("cls")
    promedio_tiempo_nivel = round((fin_juego - inicio_juego) / nivel)
    guardar_stats_json(nombre_user,puntaje,nivel,promedio_tiempo_nivel,"StatsUser.json")

jugar_agrupados()


