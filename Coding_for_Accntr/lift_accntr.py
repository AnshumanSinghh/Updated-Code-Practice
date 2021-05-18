"""
Given: array
Output: max possible sum which is equal to third element present in the array.
"""


def escalator(n, arr):
    arr.sort()
    print(arr)
    ans = []

    for k in range(n - 1, -1, -1):
        i = 0
        j = k - 1
        while i < j:
            if (arr[i] + arr[j]) == arr[k]:
                # print(arr[i], arr[j], arr[k])
                ans.append((arr[i], arr[j], arr[k]))
                i += 1
                j -= 1
                # print(f"j and k are {j} and {k}")

            elif (arr[i] + arr[j]) < arr[k]:
                # print(f"arr[k] greater {arr[i]}, {arr[j]}, {arr[k]}")
                i += 1
                # k -= 1

            else:
                # print(f"arr[k] lesser {arr[i]}, {arr[j]}, {arr[k]}")
                j -= 1
        print(f"{n - k} iteration complete.")
    return ans


if __name__ == '__main__':
    n = int(input("Enter the value of n: "))
    arr = [int(i)**2 for i in input("Enter the space separated array elements: ").split()]
    print(escalator(n, arr))
    # 2 5 7 4 6 9
