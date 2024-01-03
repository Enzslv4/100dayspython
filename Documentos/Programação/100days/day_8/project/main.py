# cesar cipher

from resources import letters
from functions import encrypter, decrypter, int_check
from art import logo


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
        shift_num = input('Type the shift number: ')
        int_check(shift_num)
        
        decrypter(to_decrypt, letters, shift_num, final_result)
        
        print('Your decrypted message is: ', *final_result, sep='')