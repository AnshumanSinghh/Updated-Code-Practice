def count_numbers(arr):

    """
    # OPTIMIZED CODE
    Args:
        arr ([int type]): [containing repeated numbers]

    Returns:
        [dictionary]: [having key(as number):value(repeatations for each number)]
    """
   # create a empty lsit to store key as number and value as number of repeatations for that number
    rep = {}

    # iterate through each element of array
    for x in arr:

        # if number is already present in dictionary then increase it's reps by 1
        if x in rep:
            rep[x] += 1
        # other-wise just mention the reps for that number as 1 only
        else:
            rep[x] = 1

    return rep  # finally return the dictionary
    

if __name__ == '__main__':
    n = int(input("Enter the length of array: "))
    arr = [int(i) for i in input("Enter the array elements: ").strip().split()]
    ans = count_numbers(arr)

    # let number of pairs be 0 at initial
    pair = 0

    # the iterate through each key and value of dictionary
    for _, val in ans.items():

        # temp will count number of pairs for each value
        temp = val // 2

        # then pair will be added to the temp so that it can store the total number of pairs
        pair += temp  

    print(pair)  # finally print the total pairs
