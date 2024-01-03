# + even number in a given range
total = 0
max = int(input("Digit a max number:\n"))

if max <= 1000:
    for number in range(0, max + 1, 2):
        total += number
    print(total)
else:
    print('Nothing to say.')
