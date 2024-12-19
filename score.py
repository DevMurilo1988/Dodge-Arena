# score.py
import pygame
import time

class Score:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)  # Define a fonte para o texto
        self.time_start = time.time()  # Inicia o contador de tempo
        self.score = 0  # Inicia a pontuação com 0
        self.best_time = 0
        self.best_score = 0

    def update_score(self):
        """Atualiza a pontuação do jogador."""
        self.score += 1  # Incrementa a pontuação a cada frame, por exemplo

    def update_time(self):
        """Atualiza o tempo decorrido."""
        self.time_elapsed = time.time() - self.time_start  # Tempo desde o início do jogo
        return self.time_elapsed

    def show_score(self):
        """Exibe a pontuação e o tempo na tela."""
        time_elapsed = self.update_time()
        score_text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
        time_text = self.font.render(f"Time: {int(time_elapsed)}s", True, (0, 0, 0))

        self.screen.blit(score_text, (10, 10))  # Exibe o score no canto superior esquerdo
        self.screen.blit(time_text, (10, 50))   # Exibe o tempo no canto superior esquerdo

    def check_best_score(self):
        """Verifica se o jogador obteve o melhor score ou melhor tempo."""
        time_elapsed = self.update_time()

        if self.score > self.best_score:
            self.best_score = self.score

        if time_elapsed > self.best_time:
            self.best_time = time_elapsed

    def show_best_score(self):
        """Exibe o melhor tempo e pontuação na tela."""
        best_score_text = self.font.render(f"Best Score: {self.best_score}", True, (255, 0, 0))
        best_time_text = self.font.render(f"Best Time: {int(self.best_time)}s", True, (255, 0, 0))

        self.screen.blit(best_score_text, (self.screen.get_width() - 200, 10))  # Exibe no canto superior direito
        self.screen.blit(best_time_text, (self.screen.get_width() - 200, 50))   # Exibe no canto superior direito
