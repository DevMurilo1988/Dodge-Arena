import pygame
from game import DodgeArena  # Certifique-se de que o arquivo do jogo se chama game.py

class Menu:
    def __init__(self, screen):
        # Inicializando a tela (screen) passada como argumento
        self.screen = screen
        self.screen_width = 800
        self.screen_height = 600
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

    def show_menu(self):
        pygame.display.set_caption("Menu - Dodge Arena")
        font = pygame.font.Font(None, 50)
        clock = pygame.time.Clock()

        menu_options = ["1 Jogador", "2 Jogadores", "Sair"]
        selected_option = 0
        running = True

        while running:
            self.screen.fill(self.white)
            for i, option in enumerate(menu_options):
                color = self.black if i != selected_option else (0, 255, 0)
                text = font.render(option, True, color)
                self.screen.blit(text, (self.screen_width // 2 - text.get_width() // 2, 200 + i * 60))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    return None

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected_option = (selected_option - 1) % len(menu_options)
                    if event.key == pygame.K_DOWN:
                        selected_option = (selected_option + 1) % len(menu_options)
                    if event.key == pygame.K_RETURN:
                        if selected_option == 0:  # 1 Jogador
                            DodgeArena(self.screen).run("1player")
                        elif selected_option == 1:  # 2 Jogadores
                            DodgeArena(self.screen).run("2player")
                        elif selected_option == 2:  # Sair
                            running = False

            pygame.display.flip()
            clock.tick(30)

        pygame.quit()
