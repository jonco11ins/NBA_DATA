import requests
import os
import csv
import pandas as pd
import time
from dotenv import load_dotenv
load_dotenv()

url = "https://api-nba-v1.p.rapidapi.com/teams/statistics"
headers = {
    "X-RapidAPI-Key": os.getenv('rapid_api_key'),
    "X-RapidAPI-Host": os.getenv('api_host')
}
# Loop through the range of NBA team IDs
team_ids = [1,2,5,6,7,8,9,10,11,14,15,16,17,19,20,21,22,23,24,4,25,26,27,28,29,30,38,40,41,31]

for team_id in team_ids:
    season = "2018" #RapidAPI has limits on how many free calls can be made a day, data was run season by season to keep data free
    querystring = {"id": str(team_id), "season": season}
    response = requests.get(url, headers=headers, params=querystring)
    
    # Parse the response
    data = response.json()
    # Extracting the statistics data
    stats_data = data['response'][0]
    # Add the 'teamID' field
    stats_data['teamID'] = str(team_id)
    # Define the CSV file path with teamID in the filename
    csv_file_path = f"/Users/jonco11ins/Documents/NBA_data/Team_{team_id}_{season}_nba.csv"
    # Writing to CSV
    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = stats_data.keys()  # Extract column headers
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()  # Write the column headers
        writer.writerow(stats_data)  # Write the statistics data

        time.sleep(10)

    print(f"Data for team {team_id} written to {csv_file_path}")



#compiles all teams season files together
directory_path = "/Users/jonco11ins/Documents/NBA_data"
dfs = []
# Filter out files that don't start with 'Team'
for file in os.listdir(directory_path):
    # Check if the file starts with 'Team' and is a CSV file
    if file.startswith('Team') and file.endswith('.csv'):
        # Create the full file path
        print(f"Processing: {file}")
        full_path = os.path.join(directory_path, file)
    
        # Read the CSV into a dataframe and append it to our list
        dfs.append(pd.read_csv(full_path))

# Concatenate all the dataframes in the list into one dataframe
merged_df = pd.concat(dfs, ignore_index=True)
# Save the combined dataframe to a new CSV file
merged_file_path = os.path.join(directory_path, f'Complete_{season}_season_Teams_Data.csv')
merged_df.to_csv(merged_file_path, index=False)

print(f"Files merged and saved to {merged_file_path}")



# ADD team names to file
file_path = f"/Users/jonco11ins/Documents/NBA_data/Complete_{season}_season_Teams_Data.csv"
df = pd.read_csv(file_path)

# Create a dictionary to map teamID to Team_Name
team_map = {
    1: "ATL", 2: "BOS", 5: "CHA", 6: "CHI", 7: "CLE", 8: "DAL", 9: "DEN", 
    10: "DET", 11: "GSW", 14: "HOU", 15: "IND", 16: "LAC", 17: "LAL", 
    19: "MEM", 20: "MIA", 21: "MIL", 22: "MIN", 23: "NOP", 24: "NYK", 
    4: "BKN", 25: "OKC", 26: "ORL", 27: "PHI", 28: "PHX", 29: "POR", 
    30: "SAC", 38: "TOR", 40: "UTA", 41: "WAS", 31: "SAS"
}

# Use the map to add the new Team_Name column
df['Team_Name'] = df['teamID'].map(team_map)
# Save the modified DataFrame back to the same CSV file
df.to_csv(file_path, index=False)



#PUTTING ALL SEASONS IN ONE FILE
# Directory containing your CSV files
directory_path = "/Users/jonco11ins/Documents/NBA_data/"

# Create a new Excel writer object
with pd.ExcelWriter(os.path.join(directory_path, 'consolidated_complete_NBA_DATA.xlsx')) as writer:
    for filename in os.listdir(directory_path):
        if filename.startswith("Complete") and filename.endswith(".csv"):
            # Read the CSV file into a DataFrame
            df = pd.read_csv(os.path.join(directory_path, filename))
            
            # Write the DataFrame to a new sheet in the Excel file
            # Use the filename (without extension) as the sheet name
            sheet_name = filename.rsplit('.', 1)[0]
            df.to_excel(writer, sheet_name=sheet_name, index=False)

print("Files have been consolidated!")


# #DELETE MERGED FILES after the fact
# import os
# delete_path = "/Users/jonco11ins/Documents/NBA_data"  # Change this to your directory path
# # Iterate through each file in the directory
# for filename in os.listdir(delete_path):
#     # Check if the filename starts with "team" and ends with ".csv"
#     if filename.startswith("Team") or filename.startswith("Complete_"):
#         file_path = os.path.join(delete_path, filename)
        
#         # Remove the file
#         os.remove(file_path)
#         print(f"Deleted: {file_path}")