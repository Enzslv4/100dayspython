import os


def clear():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)