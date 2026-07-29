import tkinter as tk
from tkinter import messagebox

# Calculator function
def calculator():
    expression = entry.get()

    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        messagebox.showerror("Error", "Invalid expression")

# Create window
root = tk.Tk()
root.title("Calculator")

# Entry field
entry = tk.Entry(root, width = 30, font = ("Arial", 24))
entry.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

# Buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
]

# Create buttons
for i, button in enumerate(buttons):
    if button == "C":
        action = lambda: entry.delete(0, tk.END)
    elif button == "=":
        action = calculator
    else:
        action = lambda x = button: entry.insert(tk.END, x)

    tk.Button(
        root,
        text = button,
        width = 5,
        height = 2,
        font = ("Arial", 18),
        command = action
    ).grid(row = i // 4 + 1, column = i % 4, padx = 2, pady = 2)

root.mainloop() # Start the main event loop
