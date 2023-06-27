# Spaceship Game

## Game Overview 
This is a simple spaceship game built using the Pygame library. The objective of the game is to control a spaceship and shoot down aliens while avoiding collisions. Your score increases for every alien you successfully destroy.

## How to Play

 * Use the arrow keys to control the spaceship.
 * Press the spacebar to shoot bullets.
 * Avoid collisions with the aliens.
 * Your score will increase for every alien you destroy.
 * The game ends if your spaceship collides with an alien.


## Game Controls

 * Arrow Up: Move the spaceship forward.
 * Arrow Down: Slow down the spaceship.
 * Arrow Left: Rotate the spaceship left.
 * Arrow Right: Rotate the spaceship right.
 * Spacebar: Shoot bullets.
 * Escape: Quit the game.

## How to Run


xhost +local:docker
docker run --rm -it --volume /tmp/.X11-unix:/tmp/.X11-unix --env DISPLAY=$DISPLAY   spaceship



 * Make sure you have the required dependencies installed.
 * Run the Python script spaceship_game.py.
 * Enter your name in the provided input box.
 * Press Enter to start the game.
 * Control the spaceship using the arrow keys and shoot bullets using the spacebar.
 * Avoid collisions with the aliens and try to achieve the highest score possible.
 * The game will display the top 5 scores and player names from the database.

Enjoy playing the spaceship game!
