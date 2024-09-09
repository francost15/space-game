import pygame
from player import Player
from enemy import Enemy

class Level2:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()  # Inicializar el mezclador de sonido
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Space Invaders - Aztec Edition - Level 2")
        self.player = Player()
        self.enemies = self.create_enemies()
        self.running = True
        self.score = 0
        self.won = False

        # Cargar y reproducir la música de fondo
        pygame.mixer.music.load("assets/music/game.mp3")
        pygame.mixer.music.play(-1)  # Reproducir en bucle

        # Cargar el sonido de impacto
        self.impact_sound = pygame.mixer.Sound("assets/music/impacto.wav")

    def create_enemies(self):
        enemies = []
        image_paths = [
            ("assets/images/enemy1.png", "assets/images/enemy2.png"),
            ("assets/images/enemy3.png", "assets/images/enemy4.png"),
            ("assets/images/enemy5.png", "assets/images/enemy6.png"),
            ("assets/images/enemy1.png", "assets/images/enemy2.png"),
            ("assets/images/enemy3.png", "assets/images/enemy4.png")
        ]
        for row in range(5):  # 5 filas
            for col in range(10):  # 10 columnas
                x = 80 * col + 10
                y = 50 * row + 10
                enemy = Enemy(x, y, image_paths[row][0], image_paths[row][1])  # Sin el parámetro 'speed'
                enemies.append(enemy)
        return enemies

    def remove_enemy_row(self, row):
        enemies_to_remove = [enemy for enemy in self.enemies if enemy.rect.y == 50 * row + 10]
        for enemy in enemies_to_remove:
            self.enemies.remove(enemy)

    def check_collisions(self):
        for enemy in self.enemies[:]:
            if enemy.check_collision(self.player.rect):
                self.running = False
            for bullet in self.player.bullets[:]:
                if enemy.check_collision(bullet.rect):
                    self.enemies.remove(enemy)
                    self.player.bullets.remove(bullet)
                    self.score += 10  # Incrementar la puntuación en 10 puntos
                    self.impact_sound.play()  # Reproducir el sonido de impacto

                    # Verificar si se debe eliminar una fila
                    if self.score % 100 == 0 and self.score > 0:  # Asegurarse de que la puntuación sea mayor que 0
                        row_to_remove = (self.score // 100) - 1
                        self.remove_enemy_row(row_to_remove)

                    # Verificar si se h
                    # a alcanzado la puntuación de victoria
                    if len(self.enemies) == 0 and self.score >= 470:  # Ajustar la puntuación de victoria
                        self.running = False
                        self.won = True
                        self.show_game_win_screen()
                    break

            # Verificar colisiones entre las balas enemigas y el jugador
            for bullet in enemy.bullets[:]:
                if self.player.check_collision(bullet.rect):
                    enemy.bullets.remove(bullet)
                    if self.player.lose_life():
                        self.running = False

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            self.player.update(keys)

            for enemy in self.enemies:
                enemy.update()

            self.check_collisions()

            self.screen.fill((0, 0, 0))
            self.player.draw(self.screen)
            for enemy in self.enemies:
                enemy.draw(self.screen)

            self.display_score()
            self.display_lives()

            pygame.display.flip()

        if not self.won:
            self.show_game_over_screen()

    def display_score(self):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

    def display_lives(self):
        font = pygame.font.Font(None, 36)
        lives_text = font.render(f"Lives:", True, (255, 255, 255))
        self.screen.blit(lives_text, (620, 10))
        for i in range(self.player.lives):
            self.screen.blit(self.player.heart_image, (700 + 35 * i, 10))

    def show_game_over_screen(self):
        from game_over import game_over_screen
        game_over_screen(self.screen, self.restart_game, self.score)

    def show_game_win_screen(self):
        from game_win import game_win_screen
        game_win_screen(self.screen, self.restart_game, self.score)

    def restart_game(self):
        self.__init__()
        self.run()