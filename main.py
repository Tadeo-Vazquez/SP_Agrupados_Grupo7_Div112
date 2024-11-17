from paquete.funciones_generales import *

def jugar_agrupados()->None:
    matriz = crear_matriz_secuencias("secuencias.csv",4)
    vidas_nivel = 3
    reinicios = 3
    while True:
        matriz_desordenada = crear_matriz_4x4_desordenada(matriz)
        imprimir_interfaz_matriz(matriz_desordenada,18)
        lista_posiciones = pedir_4_posiciones(1,16)
        lista_cat_ingresadas = averiguar_4categorias_ingresadas(matriz_desordenada,lista_posiciones)
        acierto = averiguar_coincidencia_4cat(lista_cat_ingresadas)
        if acierto:
            print("ganaste")
        else:
            print("perdiste")

        break






#     pass    

# cadena = "hola"
# print(f"{cadena:{20}} a")
# print(f"|{'Texto':{10}}| a")  # Resultado: |     Texto|
# print(f"|{'Textooooo':{10}}| a")  # Resultado: |     Texto|

