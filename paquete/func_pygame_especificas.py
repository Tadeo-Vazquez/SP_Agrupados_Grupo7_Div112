import pygame


def dibujar_boton(boton,ventana_principal):
    pygame.draw.rect(ventana_principal, boton["Color Fondo"], boton["Rectangulo"],border_radius=5)
    boton["Pantalla"].blit(boton["Superficie"], boton["Rectangulo"])

def dibujar_boton_texto(boton_texto):
    pygame.draw.rect(boton_texto["Pantalla"],"Red",boton_texto["Rectangulo"])
    boton_texto["Pantalla"].blit(boton_texto["Superficie"],boton_texto["Rectangulo"])

def reproducir_sonido(path_sonido):
    pygame.mixer.init()
    pygame.mixer.music.load(path_sonido)
    pygame.mixer.music.play(1)

def mostrar_botones(matriz_botones,pantalla):
    for fila in matriz_botones:
        for boton in fila:
            dibujar_boton(boton,pantalla)    

def actualizar_fondo_boton(boton):
    if boton["Estado"]:
        boton["Color Fondo"] = (56, 255, 245)
    else:
        boton["Color Fondo"] = "Grey"