import json

# Create the configuration dictionary
config = {
    "database": {
        "host": "192.168.1.106",
        "name": "spaceship_scoring_board",
        "user": "spaceship_user",
        "password": "Evi1995!!"
    },
    "images": {
        "spaceship": "spaceship.png",
        "background": "background.jpg",
        "explosion": "explosion.png",
        "bullet": "bullet.png",
        "alien": "alien.png"
    },
    "gameplay": {
        "speed": 3,
        "bullet_speed": 5,
        "angle_rate": 1,
        "explosion_duration": 0.5,
        "spawn_interval": 0
    }
}

# Convert the dictionary to a JSON string
json_str = json.dumps(config, indent=4)

# Write the JSON string to a file
with open('config.json', 'w') as config_file:
    config_file.write(json_str)
