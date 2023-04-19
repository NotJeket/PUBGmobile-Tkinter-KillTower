import requests, json
import tkinter as tk


# function to get the data from the JSON API
def get_json_data(url):
    response = requests.get(url)
    data = response.json()
    return data


# get the data from the two JSON sources
getallinfo_url = "http://127.0.0.1:5000/data1"
getkillinfo_url = "http://127.0.0.1:5000/data2"

getallinfo = get_json_data(getallinfo_url)
getkillinfo = get_json_data(getkillinfo_url)

# create the tkinter window
root = tk.Tk()
root.geometry("500x500")

# create a dictionary to keep track of player status
player_status = {}

# loop over the players in the TotalPlayerList
for player in getallinfo['allinfo']['TotalPlayerList']:
    team_name = player['teamName']
    player_id = player['uId']
    player_name = player['playerName']

    # check if the player is alive or dead
    is_alive = True
    for kill in getkillinfo['killInfo']:
        if kill['VictimUID'] == str(player_id):
            is_alive = False
            break

    # add the player to the dictionary
    if team_name not in player_status:
        player_status[team_name] = []
    player_status[team_name].append((player_name, is_alive))

# create the label and grid for the player status table
table_label = tk.Label(root, text="PUBG mobile killtracker")
table_label.pack()

table = tk.Frame(root)
table.pack()

for i, team_name in enumerate(player_status):
    team_label = tk.Label(table, text=team_name)
    team_label.grid(row=i, column=0)
    for j, (player_name, is_alive) in enumerate(player_status[team_name]):
        player_label = tk.Label(table, text=player_name, width=10)
        if is_alive:
            player_label.config(bg="green")
        else:
            player_label.config(bg="grey")
        player_label.grid(row=i, column=j + 1)

# run the tkinter window
root.mainloop()
