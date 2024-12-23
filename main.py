import pygame
from menu import Menu

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))  # Criação da tela
    pygame.display.set_caption("Dodge Arena")  # Título da janela

    menu = Menu(screen)  # Inicializa o menu
    while menu.running:  # Permite voltar ao menu após uma partida
        menu.show_menu()

    pygame.quit()

if __name__ == "__main__":
    main()
