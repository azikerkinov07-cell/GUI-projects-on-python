import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark") # Set dark appearance mode
ctk.set_default_color_theme("blue") # Set default color theme to blue

# Currency exchange rates
rates = {
    "USD": 1.0,
    "EUR": 0.86,
    "RUB": 79.50,
    "UZS": 12650.00,
    "GBP": 0.74,
    "JPY": 148.20
}

def currency_converter(): # Function to convert currency
    amount = amount_entry.get() # Get the amount from the entry field

    if not amount: # Check if the amount is empty
        messagebox.showerror("Error", "Please enter an amount.")
        return

    try: # Convert the amount to float
        amount = float(amount)
    except ValueError: # Check if the amount is a valid number
        messagebox.showerror("Error", "Please enter a valid number.")
        return

    if amount <= 0: # Check if the amount is greater than 0
        messagebox.showerror("Error", "Amount must be greater than 0.")
        return

    from_cur = from_currency.get() # Get the source currency
    to_cur = to_currency.get() # Get the target currency

    result = amount / rates[from_cur] * rates[to_cur] # Convert currency

    result_label.configure(text = f"{amount:.2f} {from_cur} = {result:.2f} {to_cur}") # Display result

    amount_entry.delete(0, "end") # Clear input field

root = ctk.CTk() # Create window
root.title("Currency Converter") # Set window title
root.geometry("400x350") # Set window size

title = ctk.CTkLabel(root, text = "Currency Converter", 
                     font = ("Arial", 24, "bold")) # Title label
title.pack(pady = 15)

amount_entry = ctk.CTkEntry(root, placeholder_text = "Enter amount", 
                            width = 250, height = 40) # Amount entry field
amount_entry.pack(pady = 10)

from_currency = ctk.CTkComboBox(root, values = ["USD", 
                                                "EUR", "RUB", 
                                                "UZS", "GBP", 
                                                "JPY"], width = 250) # Source currency
from_currency.set("USD") # Default currency
from_currency.pack(pady = 10)

to_currency = ctk.CTkComboBox(root,
                               values = ["USD", "EUR", "RUB",
                                          "UZS", "GBP", "JPY"], width = 250) # Target currency
to_currency.set("EUR") # Default currency
to_currency.pack(pady = 10)

convert_button = ctk.CTkButton(root, text = "Convert",
                                command = currency_converter, width = 250, height = 40) # Convert button
convert_button.pack(pady = 15)

result_label = ctk.CTkLabel(root, text = "Result will appear here",
                             font = ("Arial", 18)) # Result label
result_label.pack(pady = 10)

root.mainloop() # Start the main event loop
