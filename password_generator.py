import random
import string
import tkinter as tk
from tkinter import messagebox


def generate_password(min_length, numbers=True, special_characters=True, repeats=True):
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
        if repeats:
            pwd += random.choice(characters)
        else:
            next_char = random.choice(characters)
            pwd += next_char
            characters = characters.replace(next_char, "")

    return pwd


def on_generate():
    try:
        length = int(entry.get())
        if length < 1:
            raise ValueError("Length must be positive.")

        password = generate_password(length, incl_numbers.get(), incl_symbols.get(), repeat_chars.get())

        result_text.config(state='normal')  # Enable editing
        result_text.delete("1.0", tk.END)   # Clear the current text
        result_text.insert(tk.END, password) # Insert the new password
        result_text.config(state='disabled') # Set back to read-only
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))


app = tk.Tk()
app.title("Password Generator")

# Set the geometry of the window (width x height)
app.geometry("800x500")

incl_numbers, incl_symbols, repeat_chars = tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()

# numbers?
checkbox = tk.Checkbutton(app, text='Include Numbers?', variable=incl_numbers, onvalue=True, offvalue=False)
checkbox.pack(padx=20)

# symbols?
checkbox = tk.Checkbutton(app, text='Include Symbols?', variable=incl_symbols, onvalue=True, offvalue=False)
checkbox.pack(padx=20)

# repeat characters?
checkbox = tk.Checkbutton(app, text='Repeat Characters?', variable=repeat_chars, onvalue=True, offvalue=False)
checkbox.pack(padx=20)

tk.Label(app, text="Enter password length:").pack(pady=30)

entry = tk.Entry(app, width=50)
entry.pack(pady=5)

generate_button = tk.Button(app, text="Generate Password", command=on_generate)
generate_button.pack(pady=10)

result_text = tk.Text(app, height=2, width=50, font=("Helvetica", 42))
result_text.pack(pady=20)

app.mainloop()
