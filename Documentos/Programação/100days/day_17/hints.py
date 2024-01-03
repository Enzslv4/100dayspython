class User:
    def __init__(self, name, age):
        print('New user created.')
        self.name = name
        self.age = age
        print(self.name, self.age)


user_1 = User('Enzo', 21)
user_2 = User('Maria', 22)