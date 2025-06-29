import pygame
from menu import ejecutar_menu

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("A definir")
    ejecutar_menu(pantalla)
    pygame.quit()

if __name__ == "__main__":
    main()