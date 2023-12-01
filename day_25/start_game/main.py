from turtle import Turtle, Screen
from states_names import StatesNames
import pandas

data = pandas.read_csv('day_25/start_game/brazil_states.csv')
states_list = data.state.tolist()
all_states = []
missing_states = []

screen = Screen()
screen.title('Guess the States: Brazil')
screen.setup(1000, 1000)
image = 'day_25/start_game/brazil_blank_states.gif'
screen.addshape(image)
bg = Turtle()
bg.shape(image)

while len(all_states) < 27:
    add_state = screen.textinput('Add State' ,'Wich state do you wanna add?')
    if add_state in states_list:
        t = StatesNames()
        all_states.append(t)
        state_data = data[data.state == add_state]
        t.set_pos(int(state_data.x.item()), int(state_data.y.item()), state_data.state.item())

    if add_state == 'exit':
        
        for state in states_list:
            if state not in all_states:
                missing_states.append(state)
        break

states_to_learn = pandas.DataFrame(missing_states)
states_to_learn.to_csv('day_25/start_game/remaining_states.csv')
