import random 

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter the number of players(2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
           break
        else: 
            print("Must be between 2 -  4 players")
    else:
        print("Invalid, try again")


max_score = 50
players_scores = [0 for _ in range(players)]

while max(players_scores) < max_score:
for player_idx in range(players):

    should_roll = input("Would you like to roll(y)? ")
    if should_roll.lower() != "y":
        break

    value = roll()
    if value == 1:
        print("you rolled  a 1! Turn done!")
        break
    else:
        current_score += value
        print("you rolled a:", value)







print(players)
