import random
import string
import tkinter as tk
from tkinter import messagebox


def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    for _ in range(min_length):
        pwd += random.choice(characters)

    return pwd


def on_generate():
    try:
        length = int(entry.get())
        if length < 1:
            raise ValueError("Length must be positive.")

        password = generate_password(length, incl_numbers.get(), incl_symbols.get())

        result_label.config(text=password)
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))


app = tk.Tk()
app.title("Password Generator")

# Set the geometry of the window (widthxheight)
app.geometry("800x500")

incl_numbers, incl_symbols = tk.BooleanVar(), tk.BooleanVar()

checkbox = tk.Checkbutton(app, text='Include Numbers?', variable=incl_numbers, onvalue=True, offvalue=False)
checkbox.pack(padx=20)
checkbox = tk.Checkbutton(app, text='Include Symbols?', variable=incl_symbols, onvalue=True, offvalue=False)
checkbox.pack(padx=20)

tk.Label(app, text="Enter password length:").pack(pady=30)

entry = tk.Entry(app, width=50)
entry.pack(pady=5)

generate_button = tk.Button(app, text="Generate Password", command=on_generate)
generate_button.pack(pady=10)

result_label = tk.Label(app, text="", font=("Helvetica", 42), wraplength=350)
result_label.pack(pady=20)

app.mainloop()
