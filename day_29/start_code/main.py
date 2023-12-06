from tkinter import *
from string import *
import random
import pandas


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def create_pasw():
    pasw = ''
    str_type = [ascii_letters, punctuation]
    punc_limit = 3
    for _ in range(8):
        current_str_type = random.choice(str_type)
        if current_str_type == str_type[1]:
            punc_limit -= 1
            if punc_limit > 0:
                pasw += random.choice(current_str_type)
            else:
                pasw += random.choice(str_type[0])
        else:
            pasw += random.choice(str_type[0])
    return pasw


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_info():
    website = website_input.get()
    email = email_input.get()
    password = pasw_input.get()
    infos_dict = {
        'website': f'{website}',
        'email': f'{email}',
        'password': f'{password}'
    }
    # infos_data_frame = pandas.DataFrame(infos_dict)
    # infos_data_frame.to_csv('day_29/start_code/infos.csv')

def fill_pasw_created():
    pasw_input.insert(END, string='')
    new_pasw = create_pasw()
    pasw_input.insert(END, f'{new_pasw}')


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=100, pady=100)

canvas = Canvas(width=200, height=190, highlightthickness=0)
lock_image = PhotoImage(file='day_29/start_code/logo.png')
canvas.create_image(140, 95, image=lock_image)
canvas.grid(column=1, row=0)


website_label = Label(text='Website:')
website_label.grid(column=0, row=1)


website_input = Entry(width=40)
website_input.grid(column=1, row=1)


email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)


email_input = Entry(width=40)
email_input.grid(column=1, row=2)


pasw_label = Label(text='Password:')
pasw_label.grid(column=0, row=3)


pasw_input = Entry()
pasw_input.grid(column=1, row=3)


generate_pasw_button = Button(text="Generate Password", command=fill_pasw_created)
generate_pasw_button.grid(column=2, row=3)


add_button = Button(text='Add', width=34, command=add_info)
add_button.grid(column=1, row=4)


window.mainloop()