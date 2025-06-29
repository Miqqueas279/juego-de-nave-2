import pygame
import sys
from utils import render_texto, guardar_puntaje_txt, leer_ranking_txt

def esperar_escape():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                return

def iniciar_juego(pantalla):
    pantalla.fill((0, 0, 0))
    render_texto(pantalla, "Jugando...", 300, 250)
    pygame.display.flip()
    pygame.time.wait(2000)

    import random
    puntaje = random.randint(100, 1000)
    nombre = pedir_nombre(pantalla)
    guardar_puntaje_txt(nombre, puntaje)

def pedir_nombre(pantalla):
    fuente = pygame.font.SysFont("arial", 32)
    nombre = ""
    reloj = pygame.time.Clock()

    while True:
        pantalla.fill((0, 0, 0))
        render_texto(pantalla, "¡Fin del juego!", 280, 100)
        render_texto(pantalla, "Tu puntaje será guardado", 220, 150)
        render_texto(pantalla, "Ingresá tu nombre:", 260, 250)
        render_texto(pantalla, nombre, 260, 300)
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN and nombre.strip():
                    return nombre.strip()
                elif evento.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                elif len(nombre) < 15:
                    nombre += evento.unicode

        reloj.tick(60)

def mostrar_ranking(pantalla):
    pantalla.fill((0, 0, 0))
    ranking = leer_ranking_txt()

    render_texto(pantalla, "Ranking de Jugadores", 220, 30)
    y = 100
    for i, (nombre, puntaje) in enumerate(ranking[:5], start=1):
        render_texto(pantalla, f"{i}. {nombre} - {puntaje} pts", 200, y)
        y += 40

    render_texto(pantalla, "Presiona ESC para volver", 220, 520)
    pygame.display.flip()
    esperar_escape()

def mostrar_como_jugar(pantalla):
    fuente = pygame.font.SysFont("arial", 28)
    teclas_img = pygame.image.load("recursos/teclas.png")
    espacio_img = pygame.image.load("recursos/barra espaciadora.png")
    teclas_img = pygame.transform.scale(teclas_img, (200, 100))
    espacio_img = pygame.transform.scale(espacio_img, (200, 60))
    reloj = pygame.time.Clock()

    while True:
        pantalla.fill((0, 0, 0))
        render_texto(pantalla, "CÓMO JUGAR", 270, 50, fuente)
        render_texto(pantalla, "Mueve con flechas o WASD:", 200, 150, fuente)
        pantalla.blit(teclas_img, teclas_img.get_rect(center=(400, 240)))
        render_texto(pantalla, "Dispara con la barra espaciadora", 160, 340, fuente)
        pantalla.blit(espacio_img, espacio_img.get_rect(center=(400, 410)))
        render_texto(pantalla, "Presiona ESC para volver", 220, 530, fuente)
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                return

        reloj.tick(60)

def mostrar_creditos(pantalla):
    pantalla.fill((0, 0, 0))
    render_texto(pantalla, "Créditos", 320, 50)
    render_texto(pantalla, "Hecho por ", 180, 200)
    render_texto(pantalla, "", 120, 250)
    render_texto(pantalla, "Presiona ESC para volver", 220, 500)
    pygame.display.flip()
    esperar_escape()