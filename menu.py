import pygame
from game import DodgeArena

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.running = True

    def show_menu(self):
        while self.running:
            self.screen.fill((0, 0, 0))

            # Renderiza o texto do menu
            singleplayer_text = self.font.render("1. Pressione '1' para Singleplayer", True, (255, 255, 255))
            multiplayer_text = self.font.render("2. Pressione '2' para Multiplayer", True, (255, 255, 255))
            quit_text = self.font.render("Esc: Sair", True, (255, 255, 255))

            self.screen.blit(singleplayer_text, (200, 200))
            self.screen.blit(multiplayer_text, (200, 250))
            self.screen.blit(quit_text, (200, 300))

            pygame.display.flip()

            # Processa eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:  # Inicia o modo singleplayer
                        self.run_game(1)
                    elif event.key == pygame.K_2:  # Inicia o modo multiplayer
                        self.run_game(2)
                    elif event.key == pygame.K_ESCAPE:  # Sai do menu
                        self.running = False

    def run_game(self, mode):
        """Inicia o jogo."""
        game = DodgeArena(self.screen)
        game.run(mode)
