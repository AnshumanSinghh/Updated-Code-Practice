def andrew_pipe(n, arr): 

    temp = []
    for i in range(n):
        for x in range(i+1, n):
            if arr[i] < arr[x]:
                break
            else:
                temp.append(arr[i])
                temp.append(arr[x])
                break
    return temp

# Driver Code Starts
if __name__ == "__main__":
    n = int(input("n: "))
    arr = [int(i) for i in input().split()]
    print(andrew_pipe(n, arr))