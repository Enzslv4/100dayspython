# cesar cipher

from resources import letters
from day_8.project.functions import encrypter, decrypter, int_check

decision = input('Type "e" to encrypt, or "d" to decrypt: ')
final_result = []

if decision == 'e':
    to_encrypt = input('Type your message: ')

    if to_encrypt.isalpha():
        shift_num = input('Type the shift number: ')
        int_check(shift_num)
        
        encrypter(to_encrypt, letters, shift_num, final_result)

        print('Your encrypted message is: ', *final_result, sep='')

elif decision == 'd':
    to_decrypt = input('Type your message: ')

    if to_decrypt.isalpha():
        try:
            shift_num = int(input('Type the shift number: '))
        except ValueError:
            print('Wrong argument.')
        
        decrypter(to_decrypt, letters, shift_num, final_result)
        
        print('Your decrypted message is: ', *final_result, sep='')