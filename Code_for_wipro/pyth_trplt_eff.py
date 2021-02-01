"""
    [MOST EFFICIENT APPROACH FOR THIS PRORAM]

    An Efficient Solution can print all triplets in O(k) time where k is number of triplets printed. 
    The idea is to use square sum relation of Pythagorean triplet, i.e., addition of squares of a and 
    b is equal to square of c, we can write these number in terms of m and n such that,

       a = m2 - n2
       b = 2 * m * n
       c  = m2 + n2

because,
       a2 = m4 + n4 – 2 * m2 * n2
       b2 = 4 * m2 * n2
       c2 = m4 + n4 + 2* m2 * n2
    We can see that a2 + b2 = c2, so instead of iterating for a, b and c we can iterate for m and n and 
    can generate these triplets.
"""


def pythagoreanTriplets(limits):
    '''
    docstring
    ''' 
    c, m = 0, 2

    # iterate until given limit is reached
    while c < limits:

        # iterate from n to m - 1
        for n in range(1, m):
            print(f"m is {m} and n is {n}") 

            # now using square sum relation of Pythagorean triplet
            # for any value of n & m
            a = m ** 2 - n ** 2  
            b = 2 * m *  n
            c = m **2 + n **2

            # but if c is greater than given limit it means c must not be included and break the loop
            if c > limits:
                break
            print(a, b, c)
        m += 1
    

if __name__ == "__main__":
    # write your driver code here.
    n = int(input("Enter the value of limit: "))
    pythagoreanTriplets(n)
