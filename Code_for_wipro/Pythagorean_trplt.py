def pythagorean_trplt(n): 
    '''
    [OPTIMIZED] BUT IT CAN BE OPTIMZED MORE...

    This functions returns all possible pythagorean triplets
    for 1 to n numbers
    ''' 
    num = [i for i in range(1, n + 1)]
    # print(num)
    
    for k in range(n - 1, -1, -1):
        i = 0
        j = k - 1

        while i < j:
            a = num[i] ** 2
            b = num[j] ** 2
            c = num[k] ** 2
            
            if a + b == c:
                print(num[i], num[j], num[k])
                i += 1
                j -= 1
            elif a + b < c:
                i += 1
            else:
                j -= 1
            
if __name__ == "__main__":
    # write your driver code here.
    n = int(input("Enter the value of n: "))
    pythagorean_trplt(n)
