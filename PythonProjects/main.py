import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7e745d195a78f9390f15f7d1eaf63f0a'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
POKEMON_ID = '44406'


body_registration = {
    "trainer_token": TOKEN,
    "email": "yuliya.snetkova5@yandex.ru",
    "password": "Artemka19"
}

body_create = {
    "name": "Монстрик",
    "photo_id": 1
}

body_new_name = {
    "pokemon_id": POKEMON_ID,
    "name": "Никита",
    "photo_id": 1
}

body_add_pokeboll = {
    "pokemon_id": POKEMON_ID
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_new_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_new_name)
print(response_new_name.text)

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeboll)
print(response_add_pokeball.text)

