# tkinter intro
# units converter

from tkinter import *
from time import sleep

window = Tk()
window.title('Miles to Km converter')
window.config(padx=20, pady=20)

label_miles = Label(text='Miles') #something that will be shown on screen
label_miles.grid(column=2, row=0)


result_label = Label(text='0')
result_label.grid(column=1,row=1)


label_equal_to = Label(text='is equal to')
label_equal_to.grid(column=0, row=1)

km_label = Label(text='Km')
km_label.grid(column=2, row=1)

def clicked():
    num_input = text_box.get()
    result = int(num_input) * 1.61
    result_label.config(text=f'{result:.2f}')
    result_label.grid(column=1, row=1)


text_box = Entry(width=10)
text_box.grid(column=1, row=0)


calculate_buttom = Button(text='Calculate', command=clicked)
calculate_buttom.grid(column=1, row=2)


window.mainloop()