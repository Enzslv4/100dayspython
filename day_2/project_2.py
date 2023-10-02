# tip calculator
import os

print('Welcome to the tip calculator.')

def is_number(x):
    if '.' in x: # forgot how to check better if it's float or int lol
        return float(x)
    elif x.isdigit():
        return int(x)
    else:
        return False

while True:
    total_bill = input('What whas the total bill? ')
    bill_int = is_number(total_bill)
    total_people = input('How many people to split the bill? ')
    people_int = is_number(total_people)
    percentage = input('The percentage(10, 12 or 15): ')
    percentage_int = is_number(percentage)
    
    if bill_int and people_int and percentage_int:
        per_capta = bill_int / people_int
        usable_perc = [10, 12, 15]
        final_result = round((percentage_int / 100 + 1) * per_capta, 2)
        if percentage_int in usable_perc:
            print('Each person should pay:', final_result)
            break
        else:
            os.system('cls')
            print('Wrong percentage.')
            continue
    else:
        os.system('cls')
        print('You need to put a int or float number, try again.')
        continue