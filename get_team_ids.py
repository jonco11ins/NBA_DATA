from dotenv import load_dotenv
load_dotenv()
import requests
import time

team_abbs = ['ATL', 'BOS', 'CHA', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 
            'IND', 'LAC', 'LAL', 'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 'BKN', 
            'OKC', 'ORL', 'PHX', 'PHO', 'POR', 'SAC', 'TOR', 'UTA', 'WAS', 'SAS']

url = "https://api-nba-v1.p.rapidapi.com/teams"
headers = {
    "X-RapidAPI-Key": getenv('rapid_api_key'),
    "X-RapidAPI-Host": getenv('api_host')
}
for abb in team_abbs:
    querystring = {"code": abb}
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    print(data)

    # Assuming the ID is present under some key in the JSON response. 
    # Adjust based on the actual structure of the response.
    team_id = data.get("response", [{}])[0].get("teamId", "ID not found")
    print(f"Team abbreviation: {abb}, Team ID: {team_id}")
    
    # Sleep for 10 seconds before the next request
    time.sleep(10)