import random
import pygame
import json
import math


class SpecialAlienBullet:
    screen = None
    special_alien_bullet_image = None

    def __init__(self,screen, x, y, special_alien_bullet_image):
        self.x = x
        self.y = y

        self.special_alien_bullet_image = special_alien_bullet_image
        self.screen = screen
        self.special_alien_bullet_rect = self.special_alien_bullet_image.get_rect(center=(x, y))
        self.speed = 3
    
    def update(self, spaceship_x, spaceship_y):

        dx = spaceship_x - self.x
        dy = spaceship_y - self.y 
        angle = math.atan2(dy, dx)  # Angle in radians
        self.rotate_angle = math.degrees(angle)

        movement_vector = pygame.math.Vector2(0, -self.speed).rotate(-self.rotate_angle)

        # Update the position using the direction vector
        self.x += movement_vector.x 
        self.y += movement_vector.y 

    def draw(self):
        self.rotated_special_alien_bullet_image = pygame.transform.rotate(self.special_alien_bullet_image, self.rotate_angle)
        self.rotated_special_alien_bullet_rect = self.rotated_special_alien_bullet_image.get_rect(center = (self.x, self.y))
        self.screen.blit(self.rotated_special_alien_bullet_image, self.rotated_special_alien_bullet_rect)

