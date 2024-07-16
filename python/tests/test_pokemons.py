import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'token'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '6453'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_trainers_name():
    response_name = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_name.json()['data'][0]['trainer_name'] == 'NIk'

@pytest.mark.parametrize('key, value', [('id', '6453'), ('trainer_name', 'NIk'),('level', '1'), ('city', 'UFA')])
def test_parametr(key, value):
    response_parametr = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_parametr.json()['data'][0][key] == value