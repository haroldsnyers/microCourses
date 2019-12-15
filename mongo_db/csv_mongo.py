import csv
from pymongo import MongoClient

#CSV to JSON Conversion
csvfile_games = open('games.csv', 'r')
reader_games = csv.DictReader( csvfile_games )
csvfile_users = open('users.csv', 'r')
reader_users = csv.DictReader( csvfile_users)
mongo_client = MongoClient('')

db=mongo_client.myNewDatabase
db.games.drop()
db.usersKicker.drop()
header_game=["teams", "score_team_a", "score_team_b", "date"]
header_user=["user", 'times played', "times won", "id_user"]
header_link=["id_game", "id_user", "team"]
header_id = "id"

for each in reader_users:
    row={}
    for field in header_user:
        row[field]=each[field]

    db.usersKicker.insert_one(row)

user_id_dict = {}
for itm in db.usersKicker.find():
   print(itm.get('_id'))
   user_id_dict[itm.get('id_user')] = itm.get("_id")

index = 1
for game in reader_games:
    row={}
    teams = {}
    print("game" + str(index))
    index += 1
    for field in header_game:
        if field == "teams":
            team_a = []
            teams_b = []
            csvfile_link = open('linkUsers.csv', 'r')
            reader_link = csv.DictReader(csvfile_link)
            for each in reader_link:
                if game["id"] == each["id_game"]:
                    if each["team"] == "a":
                        team_a.append(user_id_dict[each["id_user"]])
                    elif each["team"] == "b":
                        teams_b.append(user_id_dict[each["id_user"]])
            teams["team_a"] = team_a
            teams["team_b"] = teams_b
            row["teams"] = teams
        else:
            row[field] = game[field]

    db.games.insert_one(row)

#   id : 1,
#   teams: {
#       team_a: [1, 3],
#       team_b: [2, 4]
#   },
#   score_team_a: 11,
#   score_team_b: 6,
#   date: 18/12/2019
# }
