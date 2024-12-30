# Text to Morse conversion

from functions import toMorse, isReadableChar, wannaStart
from os import system as clearConsole


while wannaStart():
    clearConsole("cls")
    entryCode = input("Digit what you want to translate: ")
    if isReadableChar(entryCode) != False:
        print(f"Your result is: {toMorse(entryCode)}")
    else:
        print("Wrong arguments, please check your entry text.")