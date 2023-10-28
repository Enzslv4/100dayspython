# prime numb

numb = int(input('Digit a number:\n'))
results = []

def is_prime(x):
    if x == 0:
        return results.append('0')
    else:
        return results.append('1')

for i in range(2, numb):
    rest_div = numb % i
    # print(rest_div)
    is_prime(rest_div)
    
if '0' in results:
    print('Not prime number.')
else:
    print('Prime Number.')