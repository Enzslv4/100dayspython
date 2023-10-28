# cesar cipher

from resources import letters
from d_encrypter import encrypter, decrypter

decision = input('Type "e" to encrypt, or "d" to decrypt: ')
final_result = []

if decision == 'e':
    to_encrypt = input('Type your message: ')

    if to_encrypt.isalpha():
        try:
            shift_num = int(input('Type the shift number: '))
        except ValueError:
            print('Wrong argument.')
        
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