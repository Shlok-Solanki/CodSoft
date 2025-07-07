import tkinter as tk
import random

# Global scores
user_score = 0
computer_score = 0
tie_score = 0

# Choices and emojis
choices = ["rock", "paper", "scissors"]
emojis = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}

# Game logic
def play(user_choice):
    global user_score, computer_score, tie_score

    computer_choice = random.choice(choices)

    user_display.config(text=f"You chose: {user_choice} {emojis[user_choice]}")
    computer_display.config(text=f"Computer chose: {computer_choice} {emojis[computer_choice]}")

    if user_choice == computer_choice:
        result.set("It's a tie!")
        tie_score += 1
        flash_result("gray")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result.set("You win!")
        user_score += 1
        flash_result("green")
    else:
        result.set("Computer wins!")
        computer_score += 1
        flash_result("red")

    update_scores()

# Update score display
def update_scores():
    score_label.config(text=f"You: {user_score}  |  Computer: {computer_score}  |  Ties: {tie_score}")

# Restart game
def restart_game():
    global user_score, computer_score, tie_score
    user_score = 0
    computer_score = 0
    tie_score = 0
    update_scores()
    result.set("")
    user_display.config(text="")
    computer_display.config(text="")

# Exit app
def exit_game():
    root.destroy()

# Flash result background color
def flash_result(color):
    original_color = result_label.cget("bg")
    result_label.config(bg=color)
    root.after(300, lambda: result_label.config(bg=original_color))

# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x470")
root.config(bg="#f0f0f0")

tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=10)

user_display = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
user_display.pack()
computer_display = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
computer_display.pack()

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=("Arial", 16, "bold"), fg="blue", bg="#f0f0f0")
result_label.pack(pady=10)

score_label = tk.Label(root, text="You: 0  |  Computer: 0  |  Ties: 0", font=("Arial", 12), bg="#f0f0f0")
score_label.pack(pady=5)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=15)

tk.Button(button_frame, text="Rock 🪨", width=12, font=("Arial", 12), command=lambda: play("rock")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Paper 📄", width=12, font=("Arial", 12), command=lambda: play("paper")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Scissors ✂️", width=12, font=("Arial", 12), command=lambda: play("scissors")).grid(row=0, column=2, padx=5)

control_frame = tk.Frame(root, bg="#f0f0f0")
control_frame.pack(pady=10)

tk.Button(control_frame, text="Restart", font=("Arial", 12), bg="orange", width=10, command=restart_game).grid(row=0, column=0, padx=10)
tk.Button(control_frame, text="Exit", font=("Arial", 12), bg="red", fg="white", width=10, command=exit_game).grid(row=0, column=1, padx=10)

root.mainloop()
