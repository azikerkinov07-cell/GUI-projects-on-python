import customtkinter as ctk
import random
import string

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def generate_password():
    length = 12 # Length of the password
    characters = string.ascii_letters + string.digits + string.punctuation # Characters
    password = ''.join(random.choice(characters) for i in range(length)) # Generate password
    password_entry.delete(0, "end") # Clear input field
    password_entry.insert(0, password) # Insert password into input field

root = ctk.CTk()
root.title("Password Generator")
root.geometry("400x300")

password_entry = ctk.CTkEntry(root, placeholder_text="Сгенерированный пароль",
                               width=300, height=40, font=("Arial", 14))
password_entry.pack(pady=20)

generate_button = ctk.CTkButton(root, text="Сгенерировать пароль", command=generate_password,
                                width=250, height=40, font=("Arial", 14))
generate_button.pack(pady=10)

root.mainloop()
