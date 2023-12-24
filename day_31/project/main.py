#   capstone project
from tkinter import *
from pandas import *
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGES = ['English', 'French']

#------------------------------------  GETTING DATA  ------------------------------------#

data = read_csv('day_31/project/data/french_words.csv')

words_data = data.to_dict(orient="records")


#------------------------------------  CHECK ANSWER  ------------------------------------#


current_card = {}

def next_card():
    global current_card, flip_timer, words_data
    window.after_cancel(flip_timer)
    canvas.itemconfig(bg_img, image=card_front_image)
    canvas.itemconfig(language_text, text=LANGUAGES[1], fill='black')
    try:
        current_card = random.choice(words_data)
    except IndexError:
        data = read_csv('day_31/project/data/french_words.csv')
        words_data = data.to_dict(orient="records")
    canvas.itemconfig(word_text, text=current_card[LANGUAGES[1]], fill='black')
    flip_timer = window.after(3000, flip_card)
    

def flip_card():
    canvas.itemconfig(language_text, text=LANGUAGES[0], fill='white')
    canvas.itemconfig(word_text, text=current_card[LANGUAGES[0]], fill='white')
    canvas.itemconfig(bg_img, image=card_back_image)

def is_known():
    try:
        if len(words_data) > 0:
            global current_card
            words_data.remove(current_card)
            next_card()
            known_cards = DataFrame(words_data)
            known_cards.to_csv('day_31/project/data/learned_cards.csv', index=False)
    except IndexError:
        print('No more words')


def missed():
    try:
        if len(words_data) > 0:
            next_card()
    except IndexError:
        print('No more words')


#------------------------------------  UI SETUP  ------------------------------------#


window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)


# Images
card_front_image = PhotoImage(file='day_31/project/images/card_front.png')
card_back_image = PhotoImage(file='day_31/project/images/card_back.png')
right_image = PhotoImage(file='day_31/project/images/right.png')
wrong_image = PhotoImage(file='day_31/project/images/wrong.png')


# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
bg_img = canvas.create_image(400, 263, image=card_front_image)
language_text = canvas.create_text(400, 150, text='title', fill='black', font=('Arial', 20, 'italic'))
word_text = canvas.create_text(400, 253, text='word', fill='black', font=('Arial', 40, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)
next_card()


# Buttons
ok_button = Button(image=right_image, command=is_known, highlightthickness=0, width=100, height=100)
ok_button.grid(column=1, row=1)

miss_button = Button(image=wrong_image, command=missed, highlightthickness=0, width=100, height=100)
miss_button.grid(column=0, row=1)


window.mainloop()