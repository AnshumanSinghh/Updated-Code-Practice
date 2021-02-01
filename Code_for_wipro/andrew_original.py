def andrew_original(n, arr):
    # drone will move from left to right for every pipe so will run this outer loop only once
    # and for this inner loop will run for n - 1 times
    for i in range(n):

        # for every time it will check for pipe in right having length
        # greater than the left one so will move n - 1 times for evry updated 
        # array, since every time we found such pipe will be deleted from array
        for j in range(1, n):

            if arr[j] > arr[i]:

                # if right side has pipe greater than left one then remove the greater pipe from array
                arr.remove(arr[j])
                print(arr, "i:",i, "j:", j)
                return andrew_original(len(arr), arr) # call recursively (with args having updated array and it's length) 
                                                      # until there is no greater pipes available in right side
    return arr # return the remaining pipe array

# Driver Code Starts
if __name__ == "__main__":
    n = int(input("n: "))
    arr = [int(i) for i in input().split()]
    res = andrew_original(n, arr)
    for ans in res:
        print(ans, end=" ")
