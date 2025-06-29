import pygame
import sys
from acciones import (
    iniciar_juego,
    mostrar_ranking,
    mostrar_como_jugar,
    mostrar_creditos,
)
from utils import cargar_fondo, render_texto

def ejecutar_menu(pantalla):
    # 🎵 Música del MENÚ
    pygame.mixer.music.load("recursos/Infested City.ogg")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    opciones = ["Jugar", "Ver Ranking", "Cómo Jugar", "Créditos", "Salir"]
    seleccion = 0
    reloj = pygame.time.Clock()
    fuente = pygame.font.SysFont("Ghastly Panic.ttf", 40)
    fondo = cargar_fondo("recursos/fondo_menu.png", pantalla)

    ejecutando = True
    while ejecutando:
        pantalla.blit(fondo, (0, 0)) if fondo else pantalla.fill((255, 255, 255))

        # Título
        titulo = fuente.render("Mata o muere", True, (0, 0, 0))
        titulo_rect = titulo.get_rect(center=(pantalla.get_width() // 2, 80))
        pantalla.blit(titulo, titulo_rect)

        # Opciones del menú
        for i, texto in enumerate(opciones):
            color = (255, 0, 0) if i == seleccion else (0, 0, 0)
            opcion_render = fuente.render(texto, True, color)
            opcion_rect = opcion_render.get_rect(center=(pantalla.get_width() // 2, 200 + i * 60))
            pantalla.blit(opcion_render, opcion_rect)

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    seleccion = (seleccion - 1) % len(opciones)
                elif evento.key == pygame.K_DOWN:
                    seleccion = (seleccion + 1) % len(opciones)
                elif evento.key == pygame.K_RETURN:
                    opcion = opciones[seleccion]
                    if opcion == "Jugar":
                        pygame.mixer.music.stop()  # 🛑 Detener música del menú
                        iniciar_juego(pantalla)
                        # 🎵 Volver a activar música del menú al terminar el juego
                        pygame.mixer.music.load("recursos/Infested City.ogg")
                        pygame.mixer.music.set_volume(0.5)
                        pygame.mixer.music.play(-1)
                    elif opcion == "Ver Ranking":
                        mostrar_ranking(pantalla)
                    elif opcion == "Cómo Jugar":
                        mostrar_como_jugar(pantalla)
                    elif opcion == "Créditos":
                        mostrar_creditos(pantalla)
                    elif opcion == "Salir":
                        pygame.mixer.music.stop()
                        ejecutando = False

        reloj.tick(60)
