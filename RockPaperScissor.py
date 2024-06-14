import tkinter as tk
import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return "Player wins!"
    else:
        return "Computer wins!"

def player_choice(choice):
    global player_score, computer_score
    
    computer_choice = random.choice(choices)
    result = determine_winner(choice, computer_choice)
    result_label.config(text=result)
    
    if result == "Player wins!":
        player_score += 1
    elif result == "Computer wins!":
        computer_score += 1
    
    score_label.config(text=f"Player: {player_score} | Computer: {computer_score}")
    
    if player_score == 3:
        result_label.config(text="Player wins the game!")
        disable_buttons()
    elif computer_score == 3:
        result_label.config(text="Computer wins the game!")
        disable_buttons()

def disable_buttons():
    rock_button.config(state="disabled")
    paper_button.config(state="disabled")
    scissors_button.config(state="disabled")
    replay_button.config(state="normal")

def replay_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    score_label.config(text=f"Player: {player_score} | Computer: {computer_score}")
    result_label.config(text="")
    rock_button.config(state="normal")
    paper_button.config(state="normal")
    scissors_button.config(state="normal")
    replay_button.config(state="disabled")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x200")

player_score = 0
computer_score = 0
choices = ["Rock", "Paper", "Scissors"]

rock_button = tk.Button(root, text="Rock", command=lambda: player_choice("Rock"), width=8, bg="#4CAF50", fg="white", font=("Arial", 12))
rock_button.grid(row=0, column=0, padx=10, pady=5)

paper_button = tk.Button(root, text="Paper", command=lambda: player_choice("Paper"), width=8, bg="#2196F3", fg="white", font=("Arial", 12))
paper_button.grid(row=0, column=1, padx=10, pady=5)

scissors_button = tk.Button(root, text="Scissors", command=lambda: player_choice("Scissors"), width=8, bg="#f44336", fg="white", font=("Arial", 12))
scissors_button.grid(row=0, column=2, padx=10, pady=5)

replay_button = tk.Button(root, text="Replay", command=replay_game, state="disabled", width=8, bg="#FFC107", fg="white", font=("Arial", 12))
replay_button.grid(row=1, column=1, pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=2, column=0, columnspan=3, pady=(10, 5))

score_label = tk.Label(root, text=f"Player: {player_score} | Computer: {computer_score}", font=("Arial", 12))
score_label.grid(row=3, column=0, columnspan=3)

root.mainloop()
