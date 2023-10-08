# find the treasure

line_1 = ['a1', 'a2', 'a3']
line_2 = ['b1', 'b2', 'b3']
line_3 = ['c1', 'c2', 'c3']

paths = [line_1, line_2, line_3]
x = 0
y = 0
print('Find the treasure.')

choice = input('Choose a way to go(left/right, up/down): ')

available_choices = ['u', 'd', 'r', 'l']

def game_logic(x, y):
    if (x and y) < 4:
        

while True:
    if choice in available_choices:
        if choice == 'l':
            position = paths[x][y - 1]
    else:
        print('Wrong arguments.')
        restart = input('Do you need to restart?("y" or "n") ')
        if restart == 'y':
            continue
        elif restart == 'n':
            break
        else:
            break