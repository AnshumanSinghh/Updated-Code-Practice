def pipe_warehouse(size, array): 
    n_arr = array + []
    for i in range(size - 1):
        for j in range(i+1, i+2):
            if array[i] > array[j]:
                break
            elif array[j] > array[i]:
                x = n_arr[n_arr.index(array[j])]
                print("removing: ", x, "i&j", i, j)
                n_arr.remove(x)
                print(n_arr)
    if n_arr[-1] > n_arr[-2]:
        n_arr.remove(n_arr[-1])
    return n_arr

# Driver Code Starts
if __name__ == "__main__":
    size = int(input())
    array = [int(i) for i in input().strip().split()]
    res = pipe_warehouse(size, array)
    print(*res)
