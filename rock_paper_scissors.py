import random

# user choice
# computer choice
# check winning
# calculate points


def check_winner(u_choice, c_choice):
    if u_choice == "rock" and c_choice == "paper":
        print("Computer wins!")
        return 1
    elif u_choice == "paper" and c_choice == "scissors":
        print("Computer wins!")
        return 1
    elif u_choice == "scissors" and c_choice == "rock":
        print("Computer wins!")
        return 1
    elif u_choice == c_choice:
        print("Tie..")
        return "Tie.."
    else:
        print("You win!")
        return 0

global user_score
global computer_score

user_score = 0
computer_score = 0

# while True:
for i in range(5):

    user_choice = input("Enter your choice: ")
    choice  = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choice)
    print(f"Computer's choice is {computer_choice}")

    winner = check_winner(user_choice, computer_choice)
    if winner == 1:
        computer_score += 1
    elif winner == 0:
        user_score += 1

    print(f"Your score: {user_score}")
    print(f"Computer's score: {computer_score}")
