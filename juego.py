import pygame
import random
from utils import render_texto, guardar_puntaje_txt
from acciones import pedir_nombre

ANCHO, ALTO = 800, 600
COLOR_FONDO = (15, 15, 15)
COLOR_DISPARO = (255, 255, 0)

def cargar_imagen(path, ancho, alto):
    imagen = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(imagen, (ancho, alto))

def crear_enemigo(zombie_img):
    y = random.randint(0, ALTO - zombie_img.get_height())
    rect = pygame.Rect(ANCHO, y, zombie_img.get_width(), zombie_img.get_height())
    return {
        "rect": rect,
        "vel": -4,
        "img": zombie_img
    }

def crear_disparo(jugador):
    x = jugador.right
    y = jugador.centery - 3
    rect = pygame.Rect(x, y, 10, 5)
    return {
        "rect": rect,
        "vel": 8,
        "color": COLOR_DISPARO
    }

def jugar(pantalla):
    reloj = pygame.time.Clock()
    fuente = pygame.font.SysFont("arial", 28)

    # Cargar imágenes
    jugador_img = cargar_imagen("recursos/player.png", 40, 40)
    zombie_img = cargar_imagen("recursos/zombie.png", 40, 40)

    # 🎵 Música del juego
    pygame.mixer.music.load("recursos/horror-258261.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    jugador = pygame.Rect(50, ALTO // 2, jugador_img.get_width(), jugador_img.get_height())
    enemigos = []
    disparos = []

    puntaje = 0
    vidas = 3
    tiempo_disparo = 0

    corriendo = True
    while corriendo:
        pantalla.fill(COLOR_FONDO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                return

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP] and jugador.top > 0:
            jugador.y -= 5
        if teclas[pygame.K_DOWN] and jugador.bottom < ALTO:
            jugador.y += 5
        if teclas[pygame.K_SPACE] and pygame.time.get_ticks() - tiempo_disparo > 300:
            disparos.append(crear_disparo(jugador))
            tiempo_disparo = pygame.time.get_ticks()

        for d in disparos:
            d["rect"].x += d["vel"]
        disparos = [d for d in disparos if d["rect"].x <= ANCHO]

        if random.random() < 0.03:
            enemigos.append(crear_enemigo(zombie_img))

        for e in enemigos[:]:
            e["rect"].x += e["vel"]
            if e["rect"].colliderect(jugador):
                vidas -= 1
                enemigos.remove(e)
            elif e["rect"].right < 0:
                enemigos.remove(e)

        for d in disparos[:]:
            for e in enemigos[:]:
                if d["rect"].colliderect(e["rect"]):
                    puntaje += 100
                    enemigos.remove(e)
                    disparos.remove(d)
                    break

        pantalla.blit(jugador_img, jugador.topleft)
        for e in enemigos:
            pantalla.blit(e["img"], e["rect"].topleft)
        for d in disparos:
            pygame.draw.rect(pantalla, d["color"], d["rect"])

        render_texto(pantalla, f"Puntaje: {puntaje}", 10, 10, fuente)
        render_texto(pantalla, f"Vidas: {vidas}", 10, 40, fuente)

        pygame.display.flip()
        reloj.tick(60)

        if vidas <= 0:
            pygame.mixer.music.stop()
            nombre = pedir_nombre(pantalla)
            guardar_puntaje_txt(nombre, puntaje)
            corriendo = False
