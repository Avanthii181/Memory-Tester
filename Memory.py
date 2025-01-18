import tkinter as tk
from tkinter import messagebox
import random

# List of patterns (you can add more or use different symbols)
card_values = ["♦", "♠", "♥", "♣", "◆", "◇", "●", "★", "♦", "♠", "♥", "♣", "◆", "◇", "●", "★"]

# Shuffle the card values to randomize them
random.shuffle(card_values)

# Function to handle card flipping
def flip_card(row, col):
    global first_card, second_card, first_pos, second_pos, turned_cards
    
    # If two cards are already flipped, do nothing
    if len(turned_cards) == 2:
        return

    button = buttons[row][col]
    
    # If the card is already turned, do nothing
    if button["state"] == "disabled":
        return
    
    # Show the card value (pattern)
    button.config(text=card_values[row * 4 + col], state="disabled")
    
    # First card flip
    if not first_card:
        first_card = card_values[row * 4 + col]
        first_pos = (row, col)
        return
    
    # Second card flip
    second_card = card_values[row * 4 + col]
    second_pos = (row, col)

    # If cards match
    if first_card == second_card:
        turned_cards.append((first_pos, second_pos))
        first_card = second_card = None
        if len(turned_cards) == len(card_values) // 2:
            messagebox.showinfo("Game Over", "Congratulations, you won!")
    else:
        # If they don't match, flip them back after a short delay
        root.after(500, flip_back)

# Function to flip back the cards if they don't match
def flip_back():
    global first_card, second_card, first_pos, second_pos
    buttons[first_pos[0]][first_pos[1]].config(text="", state="normal")
    buttons[second_pos[0]][second_pos[1]].config(text="", state="normal")
    first_card = second_card = None

# Function to reset the game
def reset_game():
    global first_card, second_card, turned_cards
    random.shuffle(card_values)
    for row in range(4):
        for col in range(4):
            buttons[row][col].config(text="", state="normal")
    first_card = second_card = None
    turned_cards = []

# Set up the main game window
root = tk.Tk()
root.title("Memory Game")

# Initialize global variables
buttons = [[None, None, None, None] for _ in range(4)]
first_card = second_card = None
turned_cards = []
first_pos = second_pos = None

# Create buttons for the memory game grid (4x4)
for i in range(4):
    for j in range(4):
        buttons[i][j] = tk.Button(root, text="", width=10, height=3, font=("Arial", 20),
                                  command=lambda i=i, j=j: flip_card(i, j))
        buttons[i][j].grid(row=i, column=j)

# Add a reset button
reset_button = tk.Button(root, text="Reset", width=10, height=2, font=("Arial", 14), command=reset_game)
reset_button.grid(row=4, column=0, columnspan=4)

# Start the Tkinter main loop
root.mainloop()
