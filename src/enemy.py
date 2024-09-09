import pygame
import random
import time

class Enemy:
    def __init__(self, x, y, image_left_path, image_right_path):
        self.image_left = pygame.image.load(image_left_path)
        self.image_left = pygame.transform.scale(self.image_left, (50, 50))
        self.image_right = pygame.image.load(image_right_path)
        self.image_right = pygame.transform.scale(self.image_right, (50, 50))
        self.image = self.image_left
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = 0.6
        self.bullets = []
        self.last_shot_time = time.time()
        self.shoot_interval = random.uniform(1, 5)  # Intervalo de disparo más corto

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.right >= 800 or self.rect.left <= 0:
            self.speed_x *= -1
            self.rect.y += 20
            if self.speed_x > 0:
                self.image = self.image_right
            else:
                self.image = self.image_left

        self.shoot()

        # Actualizar balas disparadas por el enemigo
        for bullet in self.bullets:
            bullet.update()
            if bullet.rect.top > 600:
                self.bullets.remove(bullet)

    def shoot(self):
        current_time = time.time()
        if current_time - self.last_shot_time >= self.shoot_interval:
            bullet = EnemyBullet(self.rect.centerx, self.rect.bottom)
            self.bullets.append(bullet)
            self.last_shot_time = current_time
            self.shoot_interval = max(1, random.uniform(1, 3))  # Intervalo de disparo más corto pero no menor a 1 segundo

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        for bullet in self.bullets:
            bullet.draw(screen)

    def check_collision(self, other_rect):
        return self.rect.colliderect(other_rect)

class EnemyBullet:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/images/fire.png")
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2.0  # Aumenta la velocidad de la bala

    def update(self):
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def check_collision(self, other_rect):
        return self.rect.colliderect(other_rect)