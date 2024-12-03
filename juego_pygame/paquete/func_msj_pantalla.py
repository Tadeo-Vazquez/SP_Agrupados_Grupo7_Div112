from paquete.func_pygame_especificas import * 

def pedir_nombre_en_pantalla(tamaño_pantalla, ventana_principal):
    mostrar_imagen("imagenes/fondo3.jpg",ventana_principal,tamaño_pantalla,(0,0))
    fuente = pygame.font.Font(None, 35)
    fuente_msj = pygame.font.Font("fuentes/letra_pixelada2.ttf", 35)
    entrada, max_caracteres = "", 10
    rect = pygame.Rect(0, 0, 150, 40)
    rect.center = (tamaño_pantalla[0] // 2, tamaño_pantalla[1] // 2)
    activar, resultado = False, None

    while resultado == None:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit(), exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                activar = rect.collidepoint(evento.pos)
            if evento.type == pygame.KEYDOWN and activar:
                if evento.key == pygame.K_RETURN and len(entrada) >= 3:
                    return entrada
                if evento.key == pygame.K_BACKSPACE:
                    entrada = entrada[:-1]
                elif len(entrada) < max_caracteres:
                    entrada += evento.unicode

        color_rect = (98, 242, 255) if activar else (209, 213, 213)
        pygame.draw.rect(ventana_principal, color_rect, rect,border_radius=10)
        ventana_principal.blit(fuente.render(entrada, True, "Black"), (rect.x + 5, rect.y + 10))
        mensaje = fuente_msj.render("Ingresa tu nombre", True, (255, 255, 255))
        ventana_principal.blit(mensaje, (tamaño_pantalla[0] // 2 - mensaje.get_width() // 2, rect.y - 60))
        pygame.display.flip()

def mensaje_pantalla_continuar(tamaño_pantalla,ventana_principal,mensaje,color,fondo):
    mostrar_imagen(fondo,ventana_principal,tamaño_pantalla,(0,0))
    fuente = pygame.font.Font("fuentes/letra_pintura.ttf", 55)
    centro_pantalla = (tamaño_pantalla[0] // 2, tamaño_pantalla[1] // 2 + 40)
    boton_continuar = crear_boton(ventana_principal,centro_pantalla,(110,110),path_imagen="imagenes/siguiente nivel3.png")
    resultado = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_continuar["Rectangulo"].collidepoint(event.pos):
                    resultado = True                
        if resultado:
            mostrar_imagen(fondo,ventana_principal,tamaño_pantalla,(0,0))
            pygame.display.flip() 
            break        
        boton_continuar["Color Fondo"] = None
        boton_continuar["Rectangulo"].center = boton_continuar["Posicion"]
        dibujar_boton(boton_continuar,ventana_principal)
        mensaje_inicio = fuente.render(mensaje, True, "Black")
        sombra_superficie = fuente.render(mensaje, True, color)
        rect_mensaje_inicio = mensaje_inicio.get_rect()
        rect_mensaje_inicio.center = (tamaño_pantalla[0] // 2 , (tamaño_pantalla[1] // 2) - 60)
        rect_sombra = sombra_superficie.get_rect()
        rect_sombra.center = rect_mensaje_inicio.centerx - 3 , rect_mensaje_inicio.centery + 3
        ventana_principal.blit(mensaje_inicio, rect_mensaje_inicio)
        ventana_principal.blit(sombra_superficie, rect_sombra)
        pygame.display.flip()  

def mostrar_mensaje_pantalla(texto,posicion,ventana_principal,ruta_fuente,tamaño,color_letra,color_fondo=None):
    fuente = pygame.font.Font(ruta_fuente, tamaño)
    texto_superficie = fuente.render(texto, False, color_letra,color_fondo)
    texto_rect = texto_superficie.get_rect(center=posicion)
    ventana_principal.blit(texto_superficie,texto_rect)
