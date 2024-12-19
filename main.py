import pygame
from menu import Menu  # Certifique-se de que o arquivo do menu se chama main_menu.py

def main():
    pygame.init()  # Inicializa o Pygame
    screen = pygame.display.set_mode((800, 600))  # Criação da tela de 800x600 pixels
    menu = Menu(screen)  # Passando a tela como parâmetro para o Menu
    menu.show_menu()  # Exibindo o menu
    pygame.quit()  # Finaliza o Pygame após o menu

if __name__ == "__main__":  # Garantindo que o código só será executado se for o script principal
    main()
