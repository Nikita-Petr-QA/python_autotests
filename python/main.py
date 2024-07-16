import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'token'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}
body_new_name = {
    "pokemon_id": "43470",
    "name": "Кукуруза",
    "photo_id": 2
}
add_pokeball = {
    "pokemon_id": "43564"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response.text)

response_new_name = requests.put(url = f'{URL}/pokemons', headers= HEADER, json = body_new_name)
print(response_new_name.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers= HEADER, json = add_pokeball)
print(response_pokeball.text)
