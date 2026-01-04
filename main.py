import json

with open('data.json', "r") as f:
    data = json.load(f)

teams = data.keys()
# print(teams)

print("Team" + "   |", end="   ") #setup the header
for team in teams:
    print(team.ljust(6) + "|", end="   ") #loop through teams and print them
print() #go to next line

for team in teams:
    print(team.ljust(7) + "|", end="   ") #loop through teams for records

    for opponent in teams:
        if opponent == team:
            print("X".ljust(6) + "|", end="   ") #check if team is facing itself
        else:
            wins = data[team][opponent]["W"] #loop through and paste the wins
            print(str(wins).ljust(6) + "|", end="   ") #print but add spacing
    print() #go to next line after finishing the row