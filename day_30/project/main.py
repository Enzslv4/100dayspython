from tkinter import *
from string import *
from tkinter import messagebox
import random
import json

# todays lessons: learn how to play with JSON


# -------------------------- PASSWORD GENERATOR ----------------------------- #


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
    new_data = {
        website:{
            'email': email,
            'password': password
        }
    }
    if website == '' or email == '' or password == '':
        messagebox.showwarning(title='Data Status', message='You left empty spaces! Please fill them.')
    else:
        answer = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {email}\nPassword: {password} \nIs it ok to save?')
        if answer:
            try:
                with open('day_30/project/infos.json', 'r') as file:
                    data = json.load(file)
                with open('day_30/project/infos.json', 'w') as file:
                    json.dump(new_data, file, indent=4)
            except FileNotFoundError:
                with open('day_30/project/infos.json', 'w') as file:
                    data = json.load(file)
                    json.dump(data, file, indent=4)  
            finally:
                data.update(new_data)
                website_input.delete(0, END)
                pasw_input.delete(0, END)


def fill_pasw_created():
    pasw_input.delete(0, END)
    new_pasw = create_pasw()
    pasw_input.insert(END, f'{new_pasw}')


# ----------------------------- SEARCH -------------------------------- #


def search():
    website = website_input.get()
    if website == '':
        messagebox.showwarning(title='Data Status', message='You left empty spaces! Please fill them.')
    else:
        with open('day_30/project/infos.json') as file:
            data = json.load(file)
            if website in data:
                email = data[website]['email']
                pasw = data[website]['password']
                messagebox.showinfo(title=website, message=f'Email: {email}\nPassword: {pasw}')


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)


#   Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file='day_29/start_code/logo.png')
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)


#   Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

pasw_label = Label(text='Password:')
pasw_label.grid(column=0, row=3)


#   Inputs
website_input = Entry(width=32)
website_input.focus()
website_input.grid(column=1, row=1)

email_input = Entry(width=50)
email_input.insert(0, 'enzosilva142002@gmail.com')
email_input.grid(column=1, row=2, columnspan=2)

pasw_input = Entry(width=32)
pasw_input.grid(column=1, row=3)


#   Buttons
generate_pasw_button = Button(text="Generate Password", command=fill_pasw_created)
generate_pasw_button.grid(column=2, row=3)

add_button = Button(text='Add', width=43, command=add_info, highlightthickness=0)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text='Search', command=search, width=13)
search_button.grid(column=2, row=1)


window.mainloop()