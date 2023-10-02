# leap year

year = int(input('Put a year right here: '))

leap_4 = year % 4
leap_100 = year % 100
leap_400 = year % 400

if leap_4 == 0:
    if leap_100 == 0:
        if leap_400 == 0:
            print('Leap.')
        else:
            print('Not Leap.')
    else:
        print('Leap.')
else:
    print('Not Leap.')