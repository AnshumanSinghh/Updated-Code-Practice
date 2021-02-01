def sockMerchant(n, ar):
    pairs = 0
    set_ar = set(ar)
    for i in set_ar:
        count = ar.count(i)
        pairs += count//2
    return pairs


if __name__ == '__main__':
    n = int(input("Enter the length of array: "))
    ar = [int(i) for i in input("Enter the array elements: ").strip().split()]
    print(sockMerchant(n, ar))
