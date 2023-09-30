# tip calculator

print('Welcome to the tip calculator.')

total_bill = input('What whas the total bill? ')
total_people = input('How many people to split the bill? ')
percentage = input('The percentage(10, 12 or 15): ')

if total_bill.isdigit() and total_people.isdigit() and percentage.isdigit():
    bill_int = int(total_bill)
    people_int = int(total_people)
    percentage_int = int(percentage)
    per_capta = bill_int / people_int
    print(per_capta)
else:
    print('Deu ruim')