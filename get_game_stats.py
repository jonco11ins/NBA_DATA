from dotenv import load_dotenv
import requests
import os
import csv
import time 

load_dotenv()

# Setup
url = "https://api-nba-v1.p.rapidapi.com/games/statistics"
headers = {
    "X-RapidAPI-Key": os.getenv('rapid_api_key'),
    "X-RapidAPI-Host": os.getenv('api_host')
}

game_ids = range(10980,12476)  # Modify this range as needed

flattened_data = []

# Iterate over each game ID
for game_id in game_ids:
    querystring = {"id": game_id}
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    # Process the response
    for game in data['response']:
        team = game['team']
        stats = game['statistics'][0]  # Assuming there's always at least one statistic entry
        game_info = {
            **{f"team_{key}": value for key, value in team.items()},  # prefix team-related keys with "team_"
            **stats
        }
        flattened_data.append(game_info)
        print(f"Game id: {game}")

    time.sleep(10)  # Wait for 10 seconds before the next request

# Write to CSV file
filename = "/Users/jonco11ins/Documents/NBA_data/2022_NBA_GAME_STATS.csv"
with open(filename, 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=flattened_data[0].keys())
    writer.writeheader()
    for game in flattened_data:
        writer.writerow(game)

print(f"Data saved to {filename}")