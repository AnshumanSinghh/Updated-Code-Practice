"""
input: array length (n) and array
output: push zeros to end and then return the updated list.
"""


def trailing_zeros(n, arr):
    for x in arr:
        if x == 0:
            arr.remove(0)
            arr.append(0)
    return arr


if __name__ == '__main__':
    n = int(input("Enter the array size: "))
    arr = [int(i) for i in input("Enter the array elements: ").split()]
    print(trailing_zeros(n, arr))