# cesar cipher

from string import ascii_lowercase as alfabet

letters = []
for a in alfabet:
    letters += a

decision = input('"e" to encrypt, "d" to decrypt: ')
final_result = []

if decision == 'e':
    to_encrypt = input('Type your message: ')

    if to_encrypt.isalpha():
        try:
            shift_num = int(input('Type the shift number: '))
        except ValueError:
            print('Wrong argument.')
        
        for i in range(0, len(to_encrypt)):
            index_letter = letters.index(to_encrypt[i])
            if to_encrypt[i] in letters:
                if (index_letter + shift_num) > 25:
                    final_result += letters[index_letter + shift_num - 25]
                else:
                    final_result += letters[index_letter + shift_num]
        print(*final_result, sep='')