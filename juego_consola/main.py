from paquete.funciones_generales import *

def jugar_agrupados()->None:
    valores_juego = inicializar_juego() #CREA UN DICT CON TODAS LAS ESTADISTICAS Y DATOS DEL JUEGO
    matriz_desordenada,secuencias,matriz = valores_juego["matriz_desordenada"], valores_juego["secuencias"], valores_juego["matriz"] #DESEMPAQUETAMOS ESTOS DATOS DEL DICT POR LEGIBILIDAD
    while valores_juego["flag_juego"]:
        imprimir_interfaz_matriz(matriz_desordenada,18,valores_juego["stats"]) #MUESTRA LA MATRIZ DEL JUEGO    
        lista_posiciones,ejecuto_comodin = pedir_posiciones_y_ejecutar_comodin(valores_juego,matriz_desordenada) #PIDE 4 POSICIONES Y SI ALGUNA ES UN COMODIN, LO EJECUTA
        if ejecuto_comodin: #SI SE EJECUTO UN COMODIN SE PASA AL SIGUIENTE BUCLE
            continue
        lista_cat_ingresadas,acierto = listar_categorias_y_comparar(matriz_desordenada,lista_posiciones) #COMPARA LAS CATEGORIAS INGRESADAS Y DEVUELVE SI ACERTO Y QUE CATEGORIAS INGRESO
        secuencias,matriz,matriz_desordenada = manejar_acierto_o_error(acierto,matriz_desordenada,secuencias,matriz,valores_juego,lista_cat_ingresadas) #REORDENA O CREA UNA MATRIZ NUEVA DEPENDIENDO LA CIRCUNSTANCIAS
        pausar_y_limpiar_terminal()
    finalizar_juego(valores_juego)#FIN DEL JUEGO. SACA PROMEDIO DE TIEMPO Y GUARDA DATOS EN JSON

jugar_agrupados()
