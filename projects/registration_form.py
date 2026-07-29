import customtkinter as ctk
from tkinter import messagebox

# Set appearance and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Function to handle registration
def registration():
    username = username_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()

    # Validation checks
    if not username or not password or not email or not phone:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    # Validate email format
    if not email.endswith("@gmail.com"):
        messagebox.showerror("Error", "Please enter a valid Gmail address.")
        return

    # Validate phone number format
    if not phone.isdigit() or len(phone) != 16:
        messagebox.showerror("Error", "Please enter a valid 16-digit phone number.")
        return

    # Validate password complexity
    if not password.isalnum() or len(password) < 8:
        messagebox.showerror("Error", "Password must be at least 8 characters long and contain only letters and numbers.")
        return

    # If all validations pass, show success message
    messagebox.showinfo("Success", "Registration successful!")

    username_entry.delete(0, "end")
    password_entry.delete(0, "end")
    email_entry.delete(0, "end")
    phone_entry.delete(0, "end")

root = ctk.CTk()
root.title("Registration Form")
root.geometry("500x500")

title = ctk.CTkLabel(root, text="Registration Form",
                 font=("Arial", 24), text_color="white")
title.pack(pady=10)

username_entry = ctk.CTkEntry(root, placeholder_text="Enter your username",
                              font=("Arial", 14), width=300, height=40)
username_entry.pack(pady=5)

password_entry = ctk.CTkEntry(root, placeholder_text="Enter your password", show="*",
                              font=("Arial", 14), width=300, height=40)
password_entry.pack(pady=5)

email_entry = ctk.CTkEntry(root, placeholder_text="Enter your email",
                           font=("Arial", 14), width=300, height=40)
email_entry.pack(pady=5)

phone_entry = ctk.CTkEntry(root, placeholder_text="Enter your phone number",
                          font=("Arial", 14), width=300, height=40)
phone_entry.pack(pady=5)

register_button = ctk.CTkButton(root, text="Register", command=registration,
                                font=("Arial", 14), width=300, height=40)
register_button.pack(pady=5)

root.mainloop() # Start the main event loop
