import requests
import pandas as pd
import json

#looking at this player given he was the league MVP
url = "https://api-nba-v1.p.rapidapi.com/players/statistics"

querystring = {"team":"27","season":"2022","id":"159"}

headers = {
    "X-RapidAPI-Key": os.getenv('rapid_api_key'),
    "X-RapidAPI-Host": os.getenv('api_host')
}

response = requests.get(url, headers=headers, params=querystring)

data = response.json()
# Convert the 'response' list of dictionaries to a DataFrame
df = pd.DataFrame(data['response'])

# Save the DataFrame to a CSV file
df.to_csv('/Users/jonco11ins/Documents/NBA_data/2022_joel_embiid_STATS.csv', index=False)
