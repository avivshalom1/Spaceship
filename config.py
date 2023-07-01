import json
import netifaces

def get_ip_address(interface_name):
    try:
        interface_info = netifaces.ifaddresses(interface_name)
        ipv4_address = interface_info[netifaces.AF_INET][0]['addr']
        return ipv4_address
    except KeyError:
        return None

interface = "wlp3s0"
host = get_ip_address(interface)


# Create the configuration dictionary
config = {
    "database": {
        "host": host,
        "name": "spaceship_scoring_board",
        "user": "spaceship_user",
        "password": "Evi1995!!"
    },
    "images": {
        "spaceship": "spaceship.png",
        "background": "background.jpg",
        "explosion": "explosion.png",
        "bullet": "bullet.png",
        "alien": "alien.png",
        "special_alien": "special_alien.png",
        "special_alien_bullet": "special_alien_bullet.png",
        "alien_prize": "alien_prize.png",
        "special_alien_prize": "special_alien_prize.png",

    },
    "gameplay": {
        "speed": 3,
        "bullet_speed": 5,
        "angle_rate": 1,
        "explosion_duration": 0.5
    }
}

# Convert the dictionary to a JSON string
json_str = json.dumps(config, indent=4)

# Write the JSON string to a file
with open('config.json', 'w') as config_file:
    config_file.write(json_str)
