import math 
import time
def timer(func):
    def inner(*args,**kwargs):
        print('time started')
        # print(func)
        start = time.time()
        func(*args,**kwargs)
        print('time ended')
        end = time.time()
        print(f'total time taken {end-start}')
    return inner
# timer()()
@timer #decorator
def get_factorial(n):
    print('factorial starting')
    result = math.factorial(n)
    print(f'factoria of {n} is {result}')

    
get_factorial(n=5)

# vajalla way to decorate
# timer(get_factorial)()