from time import time


def fake_fib(num):
    '''
    Fibonacci series using only recursion: [Not efficient way to approach]
    '''
    if num <= 1:
        return num

    else:
        return fake_fib(num - 1) + fake_fib(num - 2)


# Driver Code Starts
if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    t1 = time()
    for i in range(n):
        fake_fib(i)
    t2 = time()
    print(f"Time required is {t2 - t1}")
