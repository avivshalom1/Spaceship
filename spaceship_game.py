#!/usr/bin/env python3
import pygame
import sys
import math
import mysql.connector
import datetime
import string
import json
import random
import time

from alien import Alien
from bullet import Bullet
from spaceship import Spaceship

# Initialize Pygame
pygame.init()

# Read the configuration from the JSON file
with open('config.json', 'r') as configfile:
    config = json.load(configfile)

# Replace the connection details with your own
host = config['database']['host']
database = config['database']['name']
user = config['database']['user']
password = config['database']['password']

# Establish the connection
conn = mysql.connector.connect(
    host=host,
    database=database,
    user=user,
    password=password
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Define the INSERT statement
insert_query = """
INSERT INTO scoring (Player_Name, Score, Date, Hour)
VALUES (%s, %s, %s, %s)
"""

# Define the SELECT statement
score_query = """
SELECT score
FROM scoring
ORDER BY score DESC
LIMIT 5
"""

# Define the SELECT statement
names_query = """
SELECT Player_Name
FROM scoring
ORDER BY score DESC
LIMIT 5
"""


# Set up the display
width, height = 0, 0
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

# Load spaceship image
spaceship_image = pygame.image.load(config['images']['spaceship']).convert_alpha()
spaceship_image = pygame.transform.scale(spaceship_image, (100, 100))

background_image = pygame.image.load(config['images']['background']).convert()
background_image = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))

explosion_image = pygame.image.load(config['images']['explosion']).convert_alpha()
explosion_image = pygame.transform.scale(explosion_image, (300, 300))

bullet_image = pygame.image.load(config['images']['bullet']).convert_alpha()
bullet_image = pygame.transform.scale(bullet_image, (30, 30))

alien_image = pygame.image.load(config['images']['alien']).convert_alpha()
alien_image = pygame.transform.scale(alien_image, (50, 50))
Alien.alien_image = alien_image

font = pygame.font.Font(None, 80)


speed = config['gameplay']['speed']
base_speed = speed
bullet_speed = config['gameplay']['bullet_speed']
angle_rate = config['gameplay']['angle_rate']

rotate_angle = 0.0

enter_key_pressed = False
is_exploding = False

explosion_duration = config['gameplay']['explosion_duration']
spawn_interval = config['gameplay']['spawn_interval']
explosion_timer = 0.0
alien_timer = 0.0

current_time = 0

# Initializing list of Bullets
spaceship = Spaceship(screen.get_width() // 2, 1000, rotate_angle, screen, spaceship_image)
bullets = [] 
aliens = []

Bullet.screen = screen
Bullet.bullet_image = bullet_image

player_name = ""

def DisplayWelcomeScreen():
    text_surface = font.render("Insert your name: ", True, (255, 255, 255)) 
    text_surface2 = font.render(player_name, True, (255, 255, 255))  
    text_surface3 = font.render("Press Enter to start!", True, (255, 255, 255)) 

    screen.blit(background_image, (0,0))
    screen.blit(text_surface, (700, 100 ))
    screen.blit(text_surface2, (750, 170 ))
    screen.blit(text_surface3, (670, 300 ))

    cursor.execute(score_query)
    rows = cursor.fetchall()

    row_y = 700
    for row_score in rows:
        texted_row = font.render(str(row_score).strip(string.punctuation), True, (255, 255, 255))
        screen.blit(texted_row, (1100, row_y ))
        row_y += 60

    cursor.execute(names_query)
    rows = cursor.fetchall()

    row_y = 700
    for row_name in rows:
        texted_row = font.render(str(row_name).strip(string.punctuation), True, (255, 255, 255))
        screen.blit(texted_row, (600, row_y ))
        row_y += 60            

    pygame.display.flip()




def DrawSpaceshipInSpace():

    screen.blit(background_image, (0,0))
    spaceship.draw()

def DrawScore(score):
    text_surface = font.render("Score:", True, (255, 255, 255))  # Text color is white (RGB: 255, 255, 255)
    text_surface2 = font.render(str(score), True, (255, 255, 255))  # Text color is white (RGB: 255, 255, 255)
    
    screen.blit(text_surface, (screen.get_width() // 2 - 70, 100 ))
    screen.blit(text_surface2, (screen.get_width() // 2, 170 ))

def DrawBullets(rotate_angle):
    for bullet in bullets:
        bullet.draw()

    for bullet in bullets:
        if not screen.get_rect().colliderect(bullet.rotated_bullet_rect):
            bullets.remove(bullet)

def DrawAliens():
    for alien in aliens:
        alien.draw()

def HandleEndOfGame(score):
    if score > 10:
        values = (player_name.strip(), score, datetime.date.today(), datetime.datetime.now().time())
        cursor.execute(insert_query, values)
        conn.commit()
    cursor.close()
    conn.close()
    pygame.quit()
    sys.exit()

def CheckForCollision():
    for alien in aliens:
        distance = math.sqrt((spaceship.x - alien.random_x)**2 + (spaceship.y - alien.random_y)**2)
        if distance < 50: 
            HandleEndOfGame(score)


def CheckForDeadAliens(score):
    for bullet in bullets:
        for alien in aliens:
            distance = math.sqrt((bullet.x - alien.random_x)**2 + (bullet.y - alien.random_y)**2)
            if distance < 20: # threshold = 10
                bullets.remove(bullet)
                aliens.remove(alien)
                score += 10
    
    return score

score = 0

while True:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and enter_key_pressed == False:
            if event.key == pygame.K_BACKSPACE:
                player_name = player_name[:-1]
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            else:
                player_name += event.unicode

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RETURN]:
        enter_key_pressed = True

    if not enter_key_pressed:
        DisplayWelcomeScreen()

    else:
        spaceship.update(is_exploding, rotate_angle)
        
        for bullet in bullets:
            bullet.update()
            
        spaceship.speed = base_speed

        if keys[pygame.K_UP]:
            spaceship.speed *= 1.5

        if keys[pygame.K_LEFT]:
            rotate_angle += angle_rate * (not is_exploding)

        if keys[pygame.K_RIGHT]:
            rotate_angle -= angle_rate * (not is_exploding)

        if keys[pygame.K_DOWN]:
            spaceship.speed = 2

        if keys[pygame.K_SPACE]:
            if len(bullets) < 100:
                bullets.append(Bullet(spaceship.x, spaceship.y, rotate_angle))
            
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        # Check if the spaceship is within the boundaries of the screen
        if not screen.get_rect().colliderect(spaceship.rotated_spaceship_rect):
            is_exploding = True
            if explosion_timer == 0:
                explosion_timer = pygame.time.get_ticks() 

        current_time = pygame.time.get_ticks()

        if is_exploding:
            elapsed_time = (current_time - explosion_timer) / 1000.0  # Convert to seconds
            # Check if the explosion duration has elapsed
            if elapsed_time < explosion_duration:
                spaceship.spaceship_image = explosion_image

            else:
                HandleEndOfGame(score)

        if spawn_interval == 0:
            spawn_interval = random.uniform(1, 2)
            alien_timer = pygame.time.get_ticks() 
        
        if spawn_interval < (current_time - alien_timer) / 1000.0:
            aliens.append(Alien(screen, alien_image))
            spawn_interval = 0

        score = CheckForDeadAliens(score)

        CheckForCollision()

        DrawSpaceshipInSpace()

        DrawScore(score)

        DrawBullets(rotate_angle)

        DrawAliens()

        #pandas?
        pygame.display.flip()

 