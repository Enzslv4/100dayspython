# file = open('day_24/project/test.txt')
# contents = file.read()
# print(contents)
# file.close() # try to aways remember to do this after openning a file, it goes to run sideways on the computer

# or use 'with' command to open the file only while doing something for you

with open('day_24/project/test.txt') as file:
    content = file.read()
    print(content)

with open('day_24/project/test.txt', 'a') as file:
    file.write('\neu gosto de sorvete')

with open('day_24/project/test.txt') as file:
    content = file.read()
    print(content)