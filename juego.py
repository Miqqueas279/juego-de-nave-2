import pygame
import random
from utils import render_texto, guardar_puntaje_txt
from acciones import pedir_nombre

ANCHO, ALTO = 800, 600
COLOR_DISPARO = (255, 255, 0)

def cargar_imagen(path, ancho, alto):
    imagen = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(imagen, (ancho, alto))

def crear_enemigo(zombie_img):
    y = random.randint(0, ALTO - zombie_img.get_height())
    rect = pygame.Rect(ANCHO, y, zombie_img.get_width(), zombie_img.get_height())
    return {
        "rect": rect,
        "vel": -2,
        "img": zombie_img
    }

def crear_disparo(jugador):
    x = jugador.right
    y = jugador.centery - 3
    rect = pygame.Rect(x, y, 10, 5)
    return {
        "rect": rect,
        "vel": 5,
        "color": COLOR_DISPARO
    }

def jugar(pantalla):
    reloj = pygame.time.Clock()
    fuente = pygame.font.SysFont("arial", 28)

    # 🎵 Música del juego
    pygame.mixer.music.load("recursos/horror-258261.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    # 🖼️ Cargar fondo
    fondo = pygame.image.load("recursos/calle.png").convert()
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

    # 🧍‍♂️ Cargar sprites
    jugador_img = cargar_imagen("recursos/player.png", 40, 40)
    zombie_img = cargar_imagen("recursos/zombie.png", 40, 40)
    corazon_img = cargar_imagen("recursos/corrazon.png", 32, 32)

    jugador = pygame.Rect(50, ALTO // 2, jugador_img.get_width(), jugador_img.get_height())
    enemigos = []
    disparos = []

    puntaje = 0
    vidas = 3
    tiempo_disparo = 0

    corriendo = True
    while corriendo:
        # 🖼️ Dibujar fondo
        pantalla.blit(fondo, (0, 0))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                return

        # Movimiento jugador
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP] and jugador.top > 0:
            jugador.y -= 5
        if teclas[pygame.K_DOWN] and jugador.bottom < ALTO:
            jugador.y += 5
        if teclas[pygame.K_SPACE] and pygame.time.get_ticks() - tiempo_disparo > 300:
            disparos.append(crear_disparo(jugador))
            tiempo_disparo = pygame.time.get_ticks()

        # Mover disparos
        for d in disparos:
            d["rect"].x += d["vel"]
        disparos = [d for d in disparos if d["rect"].x <= ANCHO]

        # Crear enemigos
        if random.random() < 0.03:
            enemigos.append(crear_enemigo(zombie_img))

        # Mover enemigos
        for e in enemigos[:]:
            e["rect"].x += e["vel"]
            if e["rect"].colliderect(jugador):
                vidas -= 1
                enemigos.remove(e)
            elif e["rect"].right < 0:
                enemigos.remove(e)

        # Colisiones disparo-enemigo
        for d in disparos[:]:
            for e in enemigos[:]:
                if d["rect"].colliderect(e["rect"]):
                    puntaje += 100
                    enemigos.remove(e)
                    disparos.remove(d)
                    break

        # Dibujar jugador
        pantalla.blit(jugador_img, jugador.topleft)

        # Dibujar enemigos
        for e in enemigos:
            pantalla.blit(e["img"], e["rect"].topleft)

        # Dibujar disparos
        for d in disparos:
            pygame.draw.rect(pantalla, d["color"], d["rect"])

        # Puntaje
        render_texto(pantalla, f"Puntaje: {puntaje}", 10, 10, fuente)

        # Vidas con corazones
        for i in range(vidas):
            pantalla.blit(corazon_img, (10 + i * 40, 50))

        pygame.display.flip()
        reloj.tick(60)

        # Fin del juego
        if vidas <= 0:
            pygame.mixer.music.stop()
            nombre = pedir_nombre(pantalla)
            guardar_puntaje_txt(nombre, puntaje)
            corriendo = False
