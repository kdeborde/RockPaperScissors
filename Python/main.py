import tkinter as tk
from tkinter import ttk
import random

# Set up our colors.
bg_color = '#2C3E50'
btn_bg_color = '#34495E'
fg_main = 'white'
fg_secondary = 'black'

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.configure(bg=bg_color)
root.geometry("400x350")
style = ttk.Style()

# Set up win counts to be able to dynamically update
player_win_count = 0
player_win_count_text = tk.StringVar()
player_win_count_text.set(str(player_win_count))
program_win_count = 0
program_win_count_text = tk.StringVar()
program_win_count_text.set(str(program_win_count))

# Set up choice and result labels to be dynamically updated.
player_choice_text = tk.StringVar()
player_choice_text.set('')
program_choice_text = tk.StringVar()
program_choice_text.set('')
result_text = tk.StringVar()
result_text.set('')


def start_game():
    choices_frame = tk.LabelFrame(root, text="Choose Rock, Paper, or Scissors:", bg=bg_color, fg=fg_main)
    choices_frame.pack(pady=10, padx=10, fill="x")

    player_option = tk.StringVar(value="Rock")
    choices = ["Rock", "Paper", "Scissors"]
    for choice in choices:
        rb = ttk.Radiobutton(choices_frame, text=choice, value=choice, variable=player_option)
        rb.pack(anchor="w", padx=5, pady=2)
        # Add event listeners for mouse over.
        rb.bind("<Enter>", on_enter)
        rb.bind("<Leave>", on_leave)

    counts_frame = tk.Frame(root, bg=bg_color)
    counts_frame.pack(pady=10, fill="x")

    # Display the player win count
    player_frame = tk.Frame(counts_frame, bg=bg_color)
    player_frame.pack(side="left", expand=True)
    player_count = tk.Label(player_frame, text=f"Player Win Count", bg=bg_color, fg=fg_main)
    player_count.pack(side="top", expand=True)
    player_additional = tk.Label(player_frame, textvariable=player_win_count_text, bg=bg_color, fg=fg_main)
    player_additional.pack(side="top", expand=True)

    # Display the program win count
    program_frame = tk.Frame(counts_frame, bg=bg_color)
    program_frame.pack(side="right", expand=True)
    program_count = tk.Label(program_frame, text=f"Program Win Count", bg=bg_color, fg=fg_main)
    program_count.pack(side="top", expand=True)
    program_additional = tk.Label(program_frame, textvariable=program_win_count_text, bg=bg_color, fg=fg_main)
    program_additional.pack(side="top", expand=True)

    play_button = ttk.Button(root, text="Play", command=lambda: play_game(player_option.get()))
    play_button.pack(pady=10)
    # Add event listeners for mouse over.
    play_button.bind("<Enter>", on_enter)
    play_button.bind("<Leave>", on_leave)

    info_frame = tk.Frame(root, bg=bg_color)
    info_frame.pack(pady=10, fill="x")
    # Update Player choice label.
    player_text_label = tk.Label(info_frame, text="Player Choice: ", bg=bg_color, fg=fg_main)
    player_text_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    player_choice_label = tk.Label(info_frame, textvariable=player_choice_text, bg=bg_color, fg=fg_main)
    player_choice_label.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    # Update label with program choice.
    program_text_label = tk.Label(info_frame, text="Program Choice: ", bg=bg_color, fg=fg_main)
    program_text_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    program_choice_label = tk.Label(info_frame, textvariable=program_choice_text, bg=bg_color, fg=fg_main)
    program_choice_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    # Dynamically update the result after play.
    result_text_label = tk.Label(info_frame, text="Result:", bg=bg_color, fg=fg_main)
    result_text_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    result_label = tk.Label(info_frame, textvariable=result_text, bg=bg_color, fg=fg_main)
    result_label.grid(row=2, column=1, padx=10, pady=5, sticky="w")

    style.theme_use('clam')
    style.configure('TRadiobutton', background=bg_color, foreground=fg_main)
    style.configure('TButton', background=btn_bg_color, foreground=fg_main)

    root.mainloop()


# Change foreground color of hovered over button.
def on_enter(e):
    # Choose which type of widget to update colors on.
    widget_type = e.widget.winfo_class()
    if widget_type == "TRadiobutton":
        style.map('TRadiobutton', foreground=[('active', fg_secondary)])
    elif widget_type == "TButton":
        style.map('TButton', foreground=[('', fg_secondary)])


# Change foreground color of button when no longer hovered.
def on_leave(e):
    widget_type = e.widget.winfo_class()
    if widget_type == "TRadiobutton":
        style.map('TRadiobutton', foreground=[('', fg_main)])
    elif widget_type == "TButton":
        style.map('TButton', foreground=[('', fg_main)])


# Function to compare player and program choice and decide who wins
def play_game(player_selected_option):
    player_selected_option = player_selected_option.lower()
    program_selected_option = get_program_choice()
    player_choice_text.set(player_selected_option.capitalize())
    program_choice_text.set(program_selected_option.capitalize())
    global player_win_count
    global program_win_count

    if player_selected_option == program_selected_option:
        result_text.set("It's a tie!")
    elif (player_selected_option == "rock" and program_selected_option == "scissors" or
          player_selected_option == "paper" and program_selected_option == "rock" or
          player_selected_option == "scissors" and program_selected_option == "paper"):
        result_text.set(f"{player_selected_option.capitalize()} beats {program_selected_option}! YOU WIN!!!")
        player_win_count += 1
    else:
        program_win_count += 1
        result_text.set(f"{player_selected_option.capitalize()} beats {program_selected_option}! YOU LOSE!!!")
    player_win_count_text.set(str(player_win_count))
    program_win_count_text.set(str(program_win_count))


def get_program_choice():
    random_num = random.randint(1, 3)
    match random_num:
        case 1:
            program_rand_choice = "rock"
        case 2:
            program_rand_choice = "paper"
        case 3:
            program_rand_choice = "scissors"
        case _:
            program_rand_choice = "it's broke"

    return program_rand_choice


if __name__ == '__main__':
    start_game()
