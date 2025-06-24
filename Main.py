import pygame
import sys

# Inicialización
pygame.init()
ANCHO, ALTO = 800, 600
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Zombies")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (50, 150, 255)
GRIS = (200, 200, 200)

# Fuente
fuente = pygame.font.SysFont("arial", 40)

# Imagen de fondo
fondo = pygame.image.load("fondo_menu.png")  # Asegurate que este archivo exista
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

# Opciones del menú
opciones = ["Jugar", "Ver Ranking", "Salir", "Créditos"]
opcion_seleccionada = 0

def dibujar_menu():
    PANTALLA.blit(fondo, (0, 0))  # Fondo con imagen
    titulo = fuente.render(" Juego de Zombies ", True, BLANCO)
    PANTALLA.blit(titulo, (100, 10))  # Alineado a la izquierda

    for i, texto in enumerate(opciones):
        color = AZUL if i == opcion_seleccionada else BLANCO
        superficie = fuente.render(texto, True, color)
        PANTALLA.blit(superficie, (100, 200 + i * 50))  # Alineado a la izquierda

    pygame.display.flip()

def ejecutar_menu():
    global opcion_seleccionada
    reloj = pygame.time.Clock()
    ejecutando = True

    while ejecutando:
        dibujar_menu()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    opcion_seleccionada = (opcion_seleccionada - 1) % len(opciones)
                elif evento.key == pygame.K_DOWN:
                    opcion_seleccionada = (opcion_seleccionada + 1) % len(opciones)
                elif evento.key == pygame.K_RETURN:
                    if opciones[opcion_seleccionada] == "Jugar":
                        print("Iniciar juego...")
                        # Ejecutar juego aquí
                    elif opciones[opcion_seleccionada] == "Ver Ranking":
                        print("Mostrar ranking...")
                        # Ejecutar módulo de ranking
                    elif opciones[opcion_seleccionada] == "Salir":
                        pygame.quit()
                        sys.exit()

        reloj.tick(60)

# Iniciar el menú
if __name__ == "__main__":
    ejecutar_menu()