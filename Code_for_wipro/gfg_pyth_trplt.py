def checkTriplet(arr, n):
    arr = sorted(arr)
    triplet = 0
    arr = [x*x for x in arr]
    # print(arr)
    for i in range(n - 1, -1, -1):
        j = 0
        k = i - 1
        while j < k:
            if arr[i] == arr[j] + arr[k]:
                triplet += 1
                print("Elements are: ", arr[j], arr[k], arr[i])
                # print("Element's indexes are: ", j, k, i)
                j += 1
                k -= 1
                return True

            elif arr[i] > arr[j] + arr[k]:
                j += 1

            else:
                k -= 1
    return False


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ans = checkTriplet(arr, n)
        if ans:
            print("Yes\n")
        else:
            print("No\n")
        tc -= 1
    