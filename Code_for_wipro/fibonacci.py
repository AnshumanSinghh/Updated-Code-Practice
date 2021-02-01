from time import time
# from functools import lru_cache

fibonacci_cache = {}
# @lru_cache(maxsize = 1000)  # using lru_cache to store the value
def fib_num(num): 
    '''
    returns Fibbonaci number using memoization
    ''' 
    value = 0
    # if fib_number is in dictionary then return it's value
    if num in fibonacci_cache:
        return fibonacci_cache[num]
    
    elif num == 1:
        value = 1

    elif num == 2:
        value = 1

    # if num > 2 return sum prev_fib_number + present_fib_number, using Reccursion
    elif num > 2:
        value = fib_num(num - 1) + fib_num(num - 2)
    
    # if the value was not in dictionary then add the number: value in dictionary
    fibonacci_cache[num] = value
    return value # return the fibonacci value
    


# Driver Code Starts
if __name__ == "__main__":
    n = int(input("Enter the num: "))
    t1 = time()
    for i in range(n):
        # print(fib_num(i), end=", ")
        fib_num(i)
    print(f"total time required {time() - t1}(s)")
