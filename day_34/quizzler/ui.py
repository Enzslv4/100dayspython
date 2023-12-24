from tkinter import *
from data import questions_data

THEME_COLOR = "#375362"


#-------------------------------- GETTING DATA --------------------------------#

score = 0
def treating_data(param): 
    global score 
    try:
        questions_data.remove(questions_data[0])
        answer =  questions_data[0]['correct_answer']
        print(answer)
        if answer == param:
            score +=1
        else:
            if score > 0:
                score -= 1
        score_label.config(text=f'Score: {score}')
    except IndexError:
        canvas.itemconfig(question_canvas, text='You ran out of questions!')


def get_quote_true():
    if len(questions_data) > 0:
        canvas.itemconfig(question_canvas, text=questions_data[0]['question'])
        treating_data('True')
        

def get_quote_false():
    if len(questions_data) > 0:
        canvas.itemconfig(question_canvas, text=questions_data[0]['question'])
        treating_data('False')

#-------------------------------- UI --------------------------------#


window = Tk()
window.title('Quizzler')
window.config(padx=50, pady=50, bg=THEME_COLOR)


# Images
true_image = PhotoImage(file='day_34/quizzler/images/true.png')
false_image = PhotoImage(file='day_34/quizzler/images/false.png')


# Labels
score_label = Label(text=f'Score: {score}', bg=THEME_COLOR, fg='white', font=20)
score_label.grid(row=0, column=1)


# Canvas
canvas = Canvas(width=500, height=500, bg='white')
question_canvas = canvas.create_text(250, 250, width=450, text=questions_data[0]['question'], font=("Arial", 20, 'italic'), fill=THEME_COLOR)
questions_data.remove(questions_data[0])
canvas.grid(row=1, column=0, columnspan=2, pady=50)


# Buttons
true_button = Button(image=true_image, highlightthickness=0, command=get_quote_true)
true_button.grid(row=2, column=0)
false_button = Button(image=false_image, highlightthickness=0, command=get_quote_false)
false_button.grid(row=2, column=1)

window.mainloop()