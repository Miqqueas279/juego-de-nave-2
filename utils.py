import pygame
import os

def render_texto(pantalla, texto, x, y, fuente=None, color=(255, 255, 255)):
    if fuente is None:
        fuente = pygame.font.SysFont("arial", 32)
    render = fuente.render(texto, True, color)
    pantalla.blit(render, (x, y))

def cargar_fondo(path, pantalla):
    imagen = pygame.image.load(path)
    return pygame.transform.scale(imagen, pantalla.get_size())

def guardar_puntaje_txt(nombre, puntaje, archivo="ranking.txt"):
    with open(archivo, "a", encoding="utf-8") as f:
        f.write(f"{nombre} - {puntaje}\n")

def leer_ranking_txt(archivo="ranking.txt"):
    if not os.path.exists(archivo):
        return []

    ranking = []
    with open(archivo, "r", encoding="utf-8") as f:
        for linea in f:
            if " - " in linea:
                nombre, puntaje = linea.strip().split(" - ")
                try:
                    ranking.append((nombre, int(puntaje)))
                except ValueError:
                    continue

    return sorted(ranking, key=lambda x: x[1], reverse=True)
