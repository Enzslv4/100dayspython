from data import morseCharacters, startText
import string


# To set game rules
def wannaStart():
    print(startText)
    startGame = input("Do you want to start the game?('Y'es or 'N'o) ")
    if isReadableChar(startGame) != False:
        if startGame not in string.digits:
            startGame = startGame.lower()
            if startGame == 'y':
                return True
            else:
                return False
    else:
        print("Wrong argument, please try again.")

# To treat the char
def isReadableChar(chars):
    new_char = ""
    for char in chars:
        if char in string.ascii_letters:
            char = char.lower()
            new_char += char
        elif char in string.digits:
            new_char += char
            pass
        else:
            new_char = False
            break
    return new_char

# To convert to Morse
def toMorse(chars):
    new_char = ''
    for char in chars:
        if char in morseCharacters:
            char = ''.join(str(morseCharacters[char]))
            new_char += f'{char} '
        else:
            new_char = False
    new_char = new_char[:-1]
    return new_char
