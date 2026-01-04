import json

with open('data.json', "r") as f:
    data = json.load(f)

teams = data.keys()
print(teams)

print("Team" + "   |", end="   ")
for team in teams:
    print(team + "   |", end="   ")
print()

for team in teams:
    print(team + "    |", end="   ")

    for opponent in teams:
        if opponent == team:
            print("X" + "     |", end="   ")
        else:
            wins = data[team][opponent]["W"]
            print(str(wins) + "   |", end="   ")
    
    print()


