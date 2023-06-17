import random
import pygame

class Alien:
    screen = None
    alien_image = None
    
    def __init__(self, screen, alien_image):
        self.x = random.randint(0, screen.get_width())
        self.y = random.randint(0, screen.get_height())
        self.screen = screen
        self.alien_image = alien_image

    def draw(self):
        self.alien_rect = self.alien_image.get_rect(center = (self.x , self.y))
        self.screen.blit(self.alien_image, self.alien_rect)
