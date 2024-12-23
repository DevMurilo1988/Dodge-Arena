import pygame
import sys
import time
import random

class DodgeArena:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.start_time = time.time()
        self.best_time_p1 = 0
        self.best_time_p2 = 0
        self.players = [pygame.Rect(200, 300, 30, 30)]
        self.balls = []
        self.ball_speed = []
        self.mode = 1

        # Sons
        pygame.mixer.init()
        self.collision_sound = pygame.mixer.Sound('assets/collision.wav')
        self.phase_up_sound = pygame.mixer.Sound('assets/phase_up.wav')
        pygame.mixer.music.load('assets/thema.wav')
        pygame.mixer.music.play(-1)  # Toca em loop

        # Configurações iniciais
        self.init_balls()

    def init_balls(self):
        """Inicializa o jogo com uma bola."""
        self.balls.append(self.create_ball())
        self.ball_speed.append(self.random_speed())

    def create_ball(self):
        """Cria uma nova bola em posição aleatória."""
        return pygame.Rect(random.randint(0, 770), random.randint(0, 570), 20, 20)

    def random_speed(self):
        """Gera uma velocidade aleatória para a bola."""
        return [random.choice([-3, 3]), random.choice([-3, 3])]

    def move_balls(self):
        """Move as bolas e faz com que quique nas bordas."""
        for i, ball in enumerate(self.balls):
            ball.x += self.ball_speed[i][0]
            ball.y += self.ball_speed[i][1]

            if ball.left <= 0 or ball.right >= 800:
                self.ball_speed[i][0] *= -1
            if ball.top <= 0 or ball.bottom >= 600:
                self.ball_speed[i][1] *= -1

    def check_collision(self, player):
        """Verifica colisão entre o jogador e as bolas."""
        for ball in self.balls:
            if player.colliderect(ball):
                self.collision_sound.play()
                return True
        return False

    def add_difficulty(self):
        """Aumenta a dificuldade ao longo do tempo."""
        elapsed_time = time.time() - self.start_time

        if len(self.balls) < 10 and elapsed_time // 5 > len(self.balls):  # Adiciona bolas a cada 5 segundos
            self.balls.append(self.create_ball())
            self.ball_speed.append(self.random_speed())
            self.phase_up_sound.play()

    def run(self, mode):
        """Loop principal do jogo."""
        self.mode = mode
        if mode == 2:
            self.players.append(pygame.Rect(600, 300, 30, 30))

        self.running = True
        while self.running:
            self.clock.tick(60)
            self.screen.fill((0, 0, 0))
            elapsed_time = time.time() - self.start_time

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            # Movimenta os jogadores
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and self.players[0].left > 0:
                self.players[0].x -= 5
            if keys[pygame.K_RIGHT] and self.players[0].right < 800:
                self.players[0].x += 5
            if keys[pygame.K_UP] and self.players[0].top > 0:
                self.players[0].y -= 5
            if keys[pygame.K_DOWN] and self.players[0].bottom < 600:
                self.players[0].y += 5

            if mode == 2:
                if keys[pygame.K_a] and self.players[1].left > 0:
                    self.players[1].x -= 5
                if keys[pygame.K_d] and self.players[1].right < 800:
                    self.players[1].x += 5
                if keys[pygame.K_w] and self.players[1].top > 0:
                    self.players[1].y -= 5
                if keys[pygame.K_s] and self.players[1].bottom < 600:
                    self.players[1].y += 5

            # Movimenta as bolas
            self.move_balls()

            # Verifica colisões
            for i, player in enumerate(self.players):
                if self.check_collision(player):
                    self.running = False
                    if i == 0:
                        self.best_time_p1 = max(self.best_time_p1, elapsed_time)
                    elif mode == 2:
                        self.best_time_p2 = max(self.best_time_p2, elapsed_time)
                    return

            # Aumenta a dificuldade
            self.add_difficulty()

            # Desenha os jogadores e as bolas
            colors = [(0, 255, 0), (0, 0, 255)]  # Verde e azul
            for i, player in enumerate(self.players):
                pygame.draw.rect(self.screen, colors[i], player)

            for ball in self.balls:
                pygame.draw.ellipse(self.screen, (255, 0, 0), ball)

            # Renderiza o cronômetro
            font = pygame.font.Font(None, 36)
            timer_text = font.render(f"Tempo: {elapsed_time:.2f}s", True, (255, 255, 255))
            self.screen.blit(timer_text, (10, 10))
            if mode == 2:
                best_p1 = font.render(f"P1 Melhor: {self.best_time_p1:.2f}s", True, (255, 255, 255))
                best_p2 = font.render(f"P2 Melhor: {self.best_time_p2:.2f}s", True, (255, 255, 255))
                self.screen.blit(best_p1, (10, 50))
                self.screen.blit(best_p2, (10, 90))
            else:
                best_p1 = font.render(f"Melhor: {self.best_time_p1:.2f}s", True, (255, 255, 255))
                self.screen.blit(best_p1, (10, 50))

            pygame.display.flip()
