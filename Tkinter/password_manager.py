from tkinter import *
from tkinter import messagebox
import re
import secrets
import string
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1): 
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    # Combine all characters
    all_characters = letters + digits + symbols
    
    while True:
        passwords = ''
        # Generate password
        for _ in range(length):
            passwords += secrets.choice(all_characters)
        
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]
        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, passwords))
            for constraint, pattern in constraints
        ):
            break
    password.insert(0, passwords)
    pyperclip.copy(passwords)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if len(website.get()) == 0 or len(password.get()) == 0:
        messagebox.showinfo(title='Oops', message='PLease fill all empty fields')   
    else:
        is_ok = messagebox.askokcancel(title=website.get(), message=f'These are your details\nEmail: {email.get()}\nPassword: {password.get()}')

    if is_ok:
        with open('data.txt', 'a') as data_file:
            data_file.write(f'\n{website.get()} | {email.get()} | {password.get()}')
            website.delete(0, END)
            password.delete(0, END)
        
# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
# logo_image = PhotoImage(file='logo.png')
# canvas.create_image(100, 100, image=logo_image)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)
website = Entry(width=35)
website.focus()
website.grid(column=1, row=1, columnspan=3)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)
email = Entry(width=35)
email.grid(column=1, row=2, columnspan=2)
email.insert(0, 'otienohjohncharles@gmail.com')

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)
password = Entry(width=21)
password.grid(column=1, row=3)

password_btn = Button(text='Generate Password', bg='green', command=generate_password)
password_btn.grid(column=2, row=3)

add_btn = Button(text='Add', width=35, bg='yellow', command=save)
add_btn.grid(column=1, row=4, columnspan=2)

canvas.grid(column=1, row=0)
root.mainloop()