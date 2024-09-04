import pygame
import time

class Player:
    def __init__(self):
        self.image = pygame.image.load("assets/aztecaplayer.png")
        self.image = pygame.transform.scale(self.image, (50, 50))  # Ajusta el tamaño si es necesario
        self.rect = self.image.get_rect()
        self.rect.x = 370
        self.rect.y = 480
        self.speed = 5
        self.bullets = []
        self.last_shot_time = 0  # Tiempo del último disparo
        self.lives = 3  # Inicializar con 3 vidas
        self.heart_image = pygame.image.load("assets/heart.png")
        self.heart_image = pygame.transform.scale(self.heart_image, (30, 30))  # Ajustar el tamaño del corazón

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.speed
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        current_time = time.time()
        if current_time - self.last_shot_time >= 0.2:  # Disparar cada 0.2 segundos
            bullet = Bullet(self.rect.centerx, self.rect.top)
            self.bullets.append(bullet)
            self.last_shot_time = current_time

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        for bullet in self.bullets:
            bullet.draw(screen)
        self.update_bullets()

    def update_bullets(self):
        for bullet in self.bullets:
            bullet.update()
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

    def check_collision(self, bullet_rect):
        """Verificar colisiones con balas enemigas."""
        return self.rect.colliderect(bullet_rect)

    def lose_life(self):
        self.lives -= 1
        if self.lives <= 0:
            return True  # Indica que el jugador ha perdido todas sus vidas
        return False


class Bullet:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/bullet.png")
        self.image = pygame.transform.scale(self.image, (35, 35))  # Ajustar el tamaño de la bala
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = -7

    def update(self):
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)