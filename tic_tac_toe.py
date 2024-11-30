import tkinter as tk
import random


# draw the table
# check winner
# toggle player
# empty_space
# new game
# make window  (label, buttons in frame, reset button, title)

def toggle_player(row, column):
    global player

    if check_winner() is False:

        if buttons[row][column]['text'] == "" and check_winner() is False:

            buttons[row][column]['text'] = player

            player = "O" if player == "X" else "X"
            label.config(text=f"Player {player}'s turn")

    if check_winner() is True and player == "X":
        label.config(text=f"{players[1]} wins!")
        
    elif check_winner() is True and player == "O":
        label.config(text=f"{players[0]} wins!")
    
    elif check_winner() == "tie":
        label.config(text="Tie")


def check_winner():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False


def empty_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True


def new_game():

    global player
    player = random.choice(players)
    label.config(text=f"{player}'s turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")


root = tk.Tk()
root.title("Tic-Tac-Toe")

players = ["X", "O"]
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

reset_button = tk.Button(root, text="Restart", font=("normal", 18), command= new_game)
reset_button.config(activebackground="black", activeforeground="white")
reset_button.pack(side="bottom")

frame = tk.Frame(root)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = tk.Button(frame, text="", font=("normal", 25), width=6, height=2,
                                      command=lambda row=row, column=column : toggle_player(row,column))
        buttons[row][column].grid(row=row, column=column)

label = tk.Label(root, text=f"Player {player}'s turn", font=("normal", 16), fg='white', bg="black")
label.pack(side="bottom")

root.mainloop()
