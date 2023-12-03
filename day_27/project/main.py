# tkinter intro
# units converter

from tkinter import *
from time import sleep

window = Tk()
window.title('Miles converter')
window.minsize(300, 100)

my_label = Label(text='Convert Miles to Km',font=('Arial', 10, 'bold'),) #something that will be shown on screen
my_label.pack()
result_label = Label()

def clicked():
    num_input = text_box.get()
    result = int(num_input) * 1.61
    result_label.config(text=f'The result is {result:.2f} kilometers')
    result_label.pack()


text_box = Entry(width=10)
text_box.pack()



button = Button(text='convert', command=clicked)
button.pack()


window.mainloop()