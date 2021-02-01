from math import floor, sqrt
from time import time

def prime_range(num):
    """
    Parameter: integer number 

    Returns: Prime number(Boolean Value) for the given range..

    starting number(Lower Bound) and Ending number(Upper Bound)

    For Example:-- for range 1 to 100
    o/p = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
    """
    if num == 1 or num == 0:
        return False # 1 is not the Prime number

    elif num == 2:
        return True # 2 is the only even Prime

    elif num > 2 and num % 2 == 0:
        return False # any even number other than 2 is not a Prime

    else:
        # now at this point we have only odd numbers left, so here we will start 
        # from 3 and take a step of two bcz we have already checked for evem numbers.
        max_divisor = floor(sqrt(num)) + 1
        for i in range(3, max_divisor, 2):
            if num % i == 0:
                return False
        return True


if __name__ == "__main__":
    lower_bound = int(input("Enter the Lower Bound: "))
    upper_bound = int(input("Enter the Upper Bound: "))
    t1 = time()
    for number in range(lower_bound, upper_bound+1):
        result = prime_range(number)
        if result:
            print(number, end=" ")
    t2 = time()
    print("Time required: ", t2 - t1)

