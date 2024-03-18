import time
print(time.time())
# seconds since Jan 1st, 1970 

# Write your code below 👇

def speed_calc_decorator(function):
    first_run = time.time()
    function()
    second_run = time.time()
    print(second_run - first_run)

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i
        
@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i