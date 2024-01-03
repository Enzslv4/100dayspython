"""
A CODE NO READABLE AT ALL KKKKKKK
feeling bad for u
"""

height = int(input("Your height(in cm's): "))

def final_bill(y):
    prices = [5, 7, 12]
    answers = ['yes', 'no']
    photo = input("Do you want to take photos?('yes' or 'no'): ")
    if photo == answers[0]:
        total_bill = prices[y] + 3
        return str(total_bill)
    else:
        total_bill = prices[y]
        return str(total_bill)

if height >= 120:
    age = int(input('Your age: '))
    if age < 12:
        print('You need to pay $' + final_bill(0))
    elif 12 <= age < 18:
        print('You need to pay $' + final_bill(1))
    else:
        print('You need to pay $' + final_bill(2))
else:
    print("Can't ride(not enough height).")