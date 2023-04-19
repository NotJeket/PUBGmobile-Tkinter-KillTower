**PUBG Mobile Killtracker**

This code retrieves data from two JSON APIs and displays the status of each player in a table using tkinter.

**Screenshot**

![](Aspose.Words.519502d0-1632-440e-ba62-9814d2301199.001.png)

**Diagram**

![](Aspose.Words.519502d0-1632-440e-ba62-9814d2301199.002.png)

**Dependencies**

- requests
- json
- tkinter

**Installation**

1. Install Python 3.x
1. Install dependencies by running pip install requests json tkinter in the command line
1. Download or clone this repository

**Usage**

1. Run the code with python pubg\_killtracker.py
1. A window will open displaying a table with each player's name and whether they are alive or dead in the game.

**How it Works**

1. Two JSON API URLs are defined.
1. The get\_json\_data function retrieves the JSON data from a given URL.
1. The getallinfo and getkillinfo variables are used to retrieve data from the two JSON APIs.
1. A tkinter window is created.
1. A dictionary is used to store the player status.
1. A loop is used to go over each player in the JSON data.
1. The is\_alive variable is set to True if the player has not been killed and False otherwise.
1. The player's information is added to the dictionary, with the team name as the key.
1. The tkinter table is created with the team names and player names, and their status is shown in green or grey depending on whether they are alive or dead.

**Limitations**

- This code only works with the specific JSON API URLs provided in the getallinfo\_url and getkillinfo\_url variables.
- The table only displays player names and whether they are alive or dead, it does not display other information such as their score or team ranking.

**Future Improvements**

- Generalize the JSON API URLs so that the code can be used with any JSON API that contains player data.
- Add more information to the table, such as player score or team ranking.
- Add error handling for cases where the JSON API data cannot be retrieved.

