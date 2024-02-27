from tkinter import *
import pandas
import random

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg='#B1DDC6')
data = pandas.read_csv('french.csv')
french_dict = data.to_dict(orient='records')
current_card = {}

def next_card():
    global current_card, card_timer
    window.after_cancel(card_timer)
    current_card = random.choice(french_dict)
    canvas.itemconfig(title_text, text='French', font=('Arial', 20, 'bold'), fill='black')
    canvas.itemconfig(word_text, text=current_card['French'], font=('Arial', 20, 'bold'), fill='black')
    card_timer = window.after(2000, flip_card)

def flip_card():
    canvas.itemconfig(title_text, text='English', font=('Arial', 20, 'bold'), fill='white')
    canvas.itemconfig(word_text, text=current_card['English'], font=('Arial', 20, 'bold'), fill='white')
    canvas.itemconfig(card_image, image=back_img)

card_timer = window.after(2000, flip_card)
canvas = Canvas(width=800, height=530)
front_img = PhotoImage(file='images/card_front.png')
back_img = PhotoImage(file='images/card_back.png')
card_image = canvas.create_image(400, 265, image=front_img)
title_text = canvas.create_text(400, 150, text='', font=('Arial', 20, 'bold'))
word_text = canvas.create_text(400, 265, text='', font=('Arial', 20, 'bold'))
canvas.config(bg='#B1DDC6', highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

yes_image = PhotoImage(file='images/right.png')
yes_button = Button(image=yes_image, highlightthickness=0, command=next_card)
yes_button.grid(row=1, column=1)

no_image = PhotoImage(file='images/wrong.png')
no_button = Button(image=no_image, highlightthickness=0, command=next_card)
no_button.grid(row=1, column=0)

next_card()
window.mainloop()