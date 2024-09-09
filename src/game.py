import pygame
from player import Player
from enemy import Enemy

class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()  # Inicializar el mezclador de sonido
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Space Invaders - Aztec Edition")
        self.player = Player()
        self.enemies = self.create_enemies()
        self.running = True
        self.score = 0
        self.won = False

        # Cargar y reproducir la música de fondo
        pygame.mixer.music.load("assets/music/game.mp3")
        pygame.mixer.music.play(-1)  # Reproducir en bucle

    def create_enemies(self):
        enemies = []
        image_paths = [
            ("assets/images/enemy1.png", "assets/images/enemy2.png"),
            ("assets/images/enemy3.png", "assets/images/enemy4.png"),
            ("assets/images/enemy5.png", "assets/images/enemy6.png")
        ]
        for row in range(3):  # 3 filas
            for col in range(10):  # 10 columnas
                x = 80 * col + 10
                y = 50 * row + 10
                enemy = Enemy(x, y, image_paths[row][0], image_paths[row][1])
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
                    self.score += 5  # Incrementar la puntuación
                    if self.score % 50 == 0:  # Eliminar una fila cada 10 puntos
                        row_to_remove = self.score // 10 - 1
                        self.remove_enemy_row(row_to_remove)
                    if self.score >= 150:  # Ajustar la puntuación de victoria a 30
                        self.running = False
                        self.won = True  # Indicar que se ha ganado el juego
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
            self.display_lives()  # Mostrar vidas

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
        # Ajustar la posición del texto "Lives:" más a la izquierda
        self.screen.blit(lives_text, (620, 10))  # Cambia 700 a 600 o el valor que prefieras
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