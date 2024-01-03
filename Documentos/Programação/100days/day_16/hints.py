# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color('blue1')
# timmy.forward(100)
# 
# myscreen = Screen()
# myscreen.exitonclick()
# print(myscreen.canvheight())


from prettytable import PrettyTable

table = PrettyTable()

table.add_column('Pessoas', ['Joao', 'Maria', 'Jose'])
table.add_column('Idades', [20, 25, 31])
table.add_column('Notas', [6, 7, 8])
table.align = 'c'

print(table)