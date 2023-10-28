def encrypter(to_encrypt, letters, shift_num, final_result):
    for i in range(0, len(to_encrypt)):
            index_letter = letters.index(to_encrypt[i])
            if to_encrypt[i] in letters:
                if (index_letter + shift_num) > 25:
                    final_result += letters[index_letter + shift_num - 25]
                else:
                    final_result += letters[index_letter + shift_num]

def decrypter(to_decrypt, letters, shift_num, final_result):
    for i in range(0, len(to_decrypt)):
        index_letter = letters.index(to_decrypt[i])
        if to_decrypt[i] in letters:
            if (index_letter - shift_num) < 0:
                final_result += letters[25 + index_letter - shift_num]
            else:
                final_result += letters[index_letter - shift_num]