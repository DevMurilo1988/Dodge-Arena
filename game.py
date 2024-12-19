import pygame
import random

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Configurações da arena
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SIZE = 30
BALL_SIZE = 20

class DodgeArena:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()

        # Carregar sons
        self.collision_sound = pygame.mixer.Sound("assets/collision.wav")
        self.phase_up_sound = pygame.mixer.Sound("assets/phase_up.wav")

    def run(self, mode):
        # Configurações iniciais
        player1 = pygame.Rect(100, 300, PLAYER_SIZE, PLAYER_SIZE)
        player2 = pygame.Rect(700, 300, PLAYER_SIZE, PLAYER_SIZE) if mode == "2player" else None
        balls = [pygame.Rect(random.randint(0, SCREEN_WIDTH - BALL_SIZE),
                             random.randint(0, SCREEN_HEIGHT - BALL_SIZE),
                             BALL_SIZE, BALL_SIZE)]
        ball_speeds = [(random.choice([-5, 5]), random.choice([-5, 5]))]

        player1_alive = True
        player2_alive = mode == "2player"
        running = True
        time_elapsed = 0
        phase = 1

        while running:
            self.screen.fill(WHITE)

            # Verifica eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Movimentação do jogador 1 (WASD)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] and player1.top > 0:
                player1.move_ip(0, -5)
            if keys[pygame.K_s] and player1.bottom < SCREEN_HEIGHT:
                player1.move_ip(0, 5)
            if keys[pygame.K_a] and player1.left > 0:
                player1.move_ip(-5, 0)
            if keys[pygame.K_d] and player1.right < SCREEN_WIDTH:
                player1.move_ip(5, 0)

            # Movimentação do jogador 2 (Setas)
            if mode == "2player" and player2_alive:
                if keys[pygame.K_UP] and player2.top > 0:
                    player2.move_ip(0, -5)
                if keys[pygame.K_DOWN] and player2.bottom < SCREEN_HEIGHT:
                    player2.move_ip(0, 5)
                if keys[pygame.K_LEFT] and player2.left > 0:
                    player2.move_ip(-5, 0)
                if keys[pygame.K_RIGHT] and player2.right < SCREEN_WIDTH:
                    player2.move_ip(5, 0)

            # Movimentação das bolas
            for i, ball in enumerate(balls):
                ball.move_ip(ball_speeds[i])
                if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
                    ball_speeds[i] = (-ball_speeds[i][0], ball_speeds[i][1])
                if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
                    ball_speeds[i] = (ball_speeds[i][0], -ball_speeds[i][1])

                # Colisão com jogadores
                if player1_alive and ball.colliderect(player1):
                    player1_alive = False
                    self.collision_sound.play()  # Toca som de colisão
                if player2_alive and ball.colliderect(player2):
                    player2_alive = False
                    self.collision_sound.play()

            # Atualiza tela
            pygame.draw.rect(self.screen, BLUE, player1)
            if mode == "2player" and player2_alive:
                pygame.draw.rect(self.screen, GREEN, player2)

            for ball in balls:
                pygame.draw.ellipse(self.screen, RED, ball)

            pygame.display.flip()

            # Checa condições de derrota
            if not player1_alive and not player2_alive:
                running = False

            # Atualiza tempo e adiciona bolas em intervalos
            time_elapsed += self.clock.tick(60)
            if time_elapsed > 5000:  # A cada 5 segundos
                time_elapsed = 0
                balls.append(pygame.Rect(random.randint(0, SCREEN_WIDTH - BALL_SIZE),
                                         random.randint(0, SCREEN_HEIGHT - BALL_SIZE),
                                         BALL_SIZE, BALL_SIZE))
                ball_speeds.append((random.choice([-5, 5]), random.choice([-5, 5])))

                # Aumenta a fase e velocidade
                phase += 1
                self.phase_up_sound.play()  # Toca som de fase
                for i in range(len(ball_speeds)):
                    ball_speeds[i] = (ball_speeds[i][0] * 1.1, ball_speeds[i][1] * 1.1)  # Acelera bolas

        return {"winner": "player1" if player1_alive else "player2" if player2_alive else "none",
                "time": pygame.time.get_ticks() // 1000, "phase": phase}
