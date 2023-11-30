# file = open('day_24/project/test.txt')
# contents = file.read()
# print(contents)
# file.close() # try to aways remember to do this after openning a file, it goes to run sideways on the computer

# or use 'with' command to open the file only while doing something for you

PLACEHOLDER = '[name]'


with open('day_24/project/names.txt') as names:
    names_list = names.readlines()

with open('day_24/project/mail.txt') as mail_text:
    mail_content = mail_text.read()
    for name in names_list:
        new_name = name.strip()
        new_mail = mail_content.replace(PLACEHOLDER, new_name)
        with open(f'day_24/project/letter_to_{new_name}.txt', 'w') as mail_txt:
            mail_txt.write(new_mail)