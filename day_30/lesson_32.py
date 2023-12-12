# try except lesson


fruits = ['Apple', 'Pear', 'Orange']

def make_pie(index):
    fruit = fruits[index]
    print(fruit + 'pie')

try:
    make_pie(3)
except IndexError:
    print('Fruit pie')
