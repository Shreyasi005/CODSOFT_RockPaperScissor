import tkinter as tk
import random


choices = ["rock", "paper", "scissors"]


def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"


def play(user_choice):
    global user_score, comp_score

    computer_choice = random.choice(choices)
    winner = determine_winner(user_choice, computer_choice)

    result_text = f"You chose {user_choice} | Computer chose {computer_choice}\n"

    if winner == "tie":
        result_text += "Result: It's a tie!"
    elif winner == "user":
        user_score += 1
        result_text += "Result: You win!"
    else:
        comp_score += 1
        result_text += "Result: Computer wins!"

    result_label.config(text=result_text)
    score_label.config(text=f"Score => You: {user_score} | Computer: {comp_score}")
    
def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    result_label.config(text="Make your move!")
    score_label.config(text="Score => You: 0 | Computer: 0")


user_score = 0
comp_score = 0


window = tk.Tk()
window.title("Rock-Paper-Scissors Game")
window.geometry("400x300")
window.resizable(False, False)


tk.Label(window, text="🎮 Rock-Paper-Scissors Game 🎮", font=("Helvetica", 16)).pack(pady=10)


result_label = tk.Label(window, text="Make your move!", font=("Helvetica", 12))
result_label.pack(pady=10)


score_label = tk.Label(window, text="Score => You: 0 | Computer: 0", font=("Helvetica", 12))
score_label.pack(pady=10)


btn_frame = tk.Frame(window)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Rock", width=10, command=lambda: play("rock")).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Paper", width=10, command=lambda: play("paper")).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Scissors", width=10, command=lambda: play("scissors")).grid(row=0, column=2, padx=5)


tk.Button(window, text="Reset Game", command=reset_game).pack(pady=10)


window.mainloop()