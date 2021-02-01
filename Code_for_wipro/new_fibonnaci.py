from time import time
def fibonacci(num, calculated = {1:0, 2:1, 3:1}):
    if num in calculated: #
        return calculated[num]
    else:
        calculated[num] = fibonacci(num - 1, calculated) + fibonacci(num - 2, calculated)
        return calculated[num]

# Driver Code Starts
if __name__ == "__main__":
    num = int(input("Enter the number: "))
    t1 = time()
    for i in range(1, num):
        fibonacci(i)
    print(f"total time required {time() - t1}(s)")
    # print(fibonacci(num), end=" ")
