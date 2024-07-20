import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7e745d195a78f9390f15f7d1eaf63f0a'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = "4046"


def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_trainername = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_trainername.json()['data'][0]['trainer_name'] == 'Марти'




    




