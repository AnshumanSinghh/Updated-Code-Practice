def left_rotation(nr, arr):
    """
    You have to perform nr left rotation on given array

    Args:
        nr ([int type]): [no of times to perform left rotation]
        arr ([int type]): [perform nr times left rotation and then return the modified array]
    """
    part1 = arr[:nr] # list slicing from index 0 to nr - 1
    part2 = arr[nr:] # list slicing from index nr to last

    return part2 + part1 # after left rotation part1 goes to the right most end.


if __name__=='__main__':
    n, nr = [int(i) for i in input("Enter the value of n & nr: ").strip().split()]
    print(nr)
    arr = [int(i) for i in input("Enter the elements of array: ").strip().split()]
    print(left_rotation(nr, arr))
