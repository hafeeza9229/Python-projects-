import random


def roll():
    min_value = 1
    max_value = 6
    rolls = random.randint(min_value, max_value)

    return rolls


while True:
    players = input("Enter the number of players (2-4):")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print("Invalid, try again.")


max_score = 50
player_score = [0 for _ in range(players)]

while max(player_score) <= max_score:

    for players_index in range(players):
        print("\nPlayer number", players_index + 1, "has just started.\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y) ? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:

                print("You rolled 1! Turn done.")
                current_score = 0
                break

            else:
                current_score += value
                print(f"You rolled a: {value}")

            print(f"Your current score is {current_score}.")

        player_score[players_index] += current_score
        print("Your total score is: ", player_score[players_index])
