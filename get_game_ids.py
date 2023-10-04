import requests
from dotenv import load_dotenv
load_dotenv()
import os
import pandas as pd

url = "https://api-nba-v1.p.rapidapi.com/games"
season = '2022'
querystring = {"season":season}

headers = {
    "X-RapidAPI-Key": os.getenv('rapid_api_key'),
    "X-RapidAPI-Host": os.getenv('api_host')
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

data=response.json()
games = data['response']

# List to store the flattened game data
flattened_games = []

for game in games:
    game_info = {
        'id': game['id'],
        'league': game['league'],
        'season': game['season']
    }
    flattened_games.append(game_info)

# Create a pandas DataFrame
df = pd.DataFrame(flattened_games)

# Save the dataframe to a CSV file
df.to_csv(f"/Users/jonco11ins/Documents/NBA_data/{season}_game_ids.csv", index=False)