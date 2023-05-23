import random
import tkinter as tk
from tkinter import font

def roll_dice():
    dice = int(dice_entry.get())
    sides = int(sides_entry.get())

    results = [random.randint(1, sides) for _ in range(dice)]
    total = sum(results)

    result_text.set(f"Results: {', '.join(map(str, results))}")
    total_text.set(f"Total: {total}")

# Create the main window
window = tk.Tk()
window.title("D&D Dice Roller")
window.geometry("400x300")

# Customize the font
custom_font = font.Font(family="Helvetica", size=12)

# Create and pack the dice label and entry widgets
dice_label = tk.Label(window, text="Number of dice:", font=custom_font)
dice_label.pack()
dice_entry = tk.Entry(window, font=custom_font)
dice_entry.pack()

# Create and pack the sides label and entry widgets
sides_label = tk.Label(window, text="Number of sides:", font=custom_font)
sides_label.pack()
sides_entry = tk.Entry(window, font=custom_font)
sides_entry.pack()

# Create and pack the roll button
roll_button = tk.Button(window, text="Roll Dice", command=roll_dice, font=custom_font)
roll_button.pack()

# Create and pack the result labels
result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text, font=custom_font)
result_label.pack()

total_text = tk.StringVar()
total_label = tk.Label(window, textvariable=total_text, font=custom_font)
total_label.pack()

# Start the main event loop
window.mainloop()
