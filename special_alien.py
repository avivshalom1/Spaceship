import random
import pygame
import json

from special_alien_bullet import SpecialAlienBullet

class SpecialAlien:
    screen = None
    alien_image = None

    def __init__(self, screen, special_alien_image, special_alien_bullet_image):
        self.x = random.randint(0, screen.get_width())
        self.y = random.randint(0, screen.get_height())

        self.screen = screen
        self.special_alien_image = special_alien_image
        self.special_alien_bullet_image = special_alien_bullet_image
        self.bullet_interval = 0
        self.bullet_timer = 0
        self.bullets = []

    def draw(self, spaceship_x, spaceship_y):

        self.special_alien_rect = self.special_alien_image.get_rect(center = (self.x , self.y))
        self.screen.blit(self.special_alien_image, self.special_alien_rect)

        for bullet in self.bullets:
            bullet.update(spaceship_x, spaceship_y)
            bullet.draw()


    def shoot(self):

        current_time = pygame.time.get_ticks()

        if self.bullet_interval == 0:
            self.bullet_interval = 1
            self.bullet_timer = pygame.time.get_ticks() 

        if self.bullet_interval < (current_time - self.bullet_timer) / 1000.0:
            self.bullets.append(SpecialAlienBullet(self.screen, self.x, self.y, self.special_alien_bullet_image))
            self.bullet_interval = 0
