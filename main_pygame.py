from paquete.funciones_pygame import *
from paquete.funciones_generales import *
import pygame

def main_juego():
    reproducir_musica("sonidos/musica_fondo2.mp3",-1)
    #inicializacion de las variables de la pantalla
    PANTALLA,ventana_principal = inicializar_ventana()
    #region inicializacion de las variables para el juego
    valores_juego = inicializar_juego(PANTALLA,ventana_principal)
    valores_juego = agregar_botones_comodines(valores_juego,ventana_principal)
    matriz_desordenada,secuencias,matriz = valores_juego["matriz_desordenada"], valores_juego["secuencias"], valores_juego["matriz"]
    matriz_botones = crear_matriz_botones(matriz_desordenada,ventana_principal,PANTALLA)
    botones_musica = crear_botones_sonido(ventana_principal)
    filas_ordenadas = 0
    #endregion
    mostrar_imagen("imagenes/fondo3.jpg",ventana_principal,PANTALLA,(0,0)) #mostrar por primera vez el fondo
    dibujar_rectangulo(100,0,700,60,(108, 34, 255),ventana_principal)
    bucle_principal_juego(valores_juego,matriz_botones,secuencias,matriz,matriz_desordenada,filas_ordenadas,ventana_principal,PANTALLA,botones_musica)
    finalizar_juego(valores_juego)

main_juego()