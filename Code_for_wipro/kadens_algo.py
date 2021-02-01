def maxSubArraySum(a, size):
    ##Your code here
    max_soFar = 0
    max_soEnding = 0
    for i in a:
        max_soEnding = max(max_soEnding + i, 0)
        max_soFar = max(max_soEnding, max_soFar)
        print(max_soEnding, max_soFar)
    if max_soFar == 0:
        return max(a)
    return max_soFar


# Driver Code Starts
if __name__ == "__main__":
    t = int(input("Enter no of test cases: "))
    for _ in range(t):
        array = [int(i) for i in input("Enter the array elements: ").strip().split()]
        size = int(input("Enter the size of array: "))
        print(maxSubArraySum(array, size))
