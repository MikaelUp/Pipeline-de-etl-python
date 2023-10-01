import pandas as pd

sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'

df = pd.read_csv('SDW2023.CSV')
user_ids = df['UserID'].tolist()
print(user_ids)

import json
import requests

def get_user(id):
    response = requests.get(f'{sdw2023_api_url}/users/{id}')
    return response.json() if response.status_code == 200 else None

users =  [user for id in user_ids if (user := get_user(id)) is not None]
print(json.dumps(users, indent=2))