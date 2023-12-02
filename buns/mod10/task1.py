import requests
import json

url = 'https://swapi.dev/api/starships/10/'
response = requests.get(url)
spaceship_data = response.json()

pilots = []
for pilotData in spaceship_data['pilots']:
    pilot_data = requests.get(pilotData).json()
    world_data = requests.get(pilot_data['homeworld']).json()
    pilot_information = {
        'name': pilot_data['name'],
        'height': pilot_data['height'],
        'mass': pilot_data['mass'],
        'homeworld': {
            'name': world_data['name'],
            'link': pilot_data['homeworld']
        }
    }
    pilots.append(pilot_information)

ship_info = {
    'name': spaceship_data['name'],
    'max_speed': spaceship_data['max_atmosphering_speed'],
    'class': spaceship_data['starship_class'],
    'pilots': pilots
}


print(json.dumps(ship_info, indent=4))

with open('spaceship_info.json', 'w') as f:
    json.dump(ship_info, f, indent=4)