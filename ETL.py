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

openai_api_key = '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'

import openai

openai.api_key = openai_api_key

def generete_ai_news(user):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um especialista em markting bancário."},
            {"role": "user", "content": f"Faça uma mensagem para {user['name']} sobre a importância dos invenstimento.(Máximo de 100 caracteres)"}
        ]
    )
    return response.choices[0].message.content.strip('\"')

for user in users:
    news = generete_ai_news(user)
    print(news)
    user['news'].append({
      "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
      "description": news
  })
    
def update_user(user):
  response = requests.put(f"{sdw2023_api_url}/users/{user['id']}", json=user)
  return True if response.status_code == 200 else False

for user in users:
  success = update_user(user)
  print(f"User {user['name']} updated? {success}!")