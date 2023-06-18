import random
import pygame
import math

class Alien:
    screen = None
    alien_image = None
    
    def __init__(self, screen, alien_image, spaceship):
        distance  = 0

        while(distance < 300):
            self.x = random.randint(0, screen.get_width())
            self.y = random.randint(0, screen.get_height())
            distance = math.sqrt((self.x - spaceship.x)**2 + (self.y - spaceship.y)**2)

        self.screen = screen

    def draw(self):
        self.alien_rect = self.alien_image.get_rect(center = (self.x , self.y))
        self.screen.blit(self.alien_image, self.alien_rect)
