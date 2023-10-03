# pizza hunt

size = int(input("Choose a size for your pizza('S'mall, 'M'edium, 'L'arge): "))

if size == 'S':
    bill = 15
    pep = 2
elif size == 'M':
    bill = 20
    pep = 3
else:
    bill = 25
    pep = 3

pepperoni = input("Do you want pepperoni('Y' or 'N')? ").lower()

if pepperoni == 'y':
    cheese = input("Do you want cheese('Y' or 'N')? ").lower()
    if cheese == 'y':
        print(bill + pep)
else:
    print(bill)