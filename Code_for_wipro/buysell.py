def BuySellGoods(size, array): 
    array = sorted(array, reverse=True)
    for i in range(size - 1):
        if array[i] == array[i + 1]:
            continue
        elif array[i] != array[i + 1]:
            return array[0] + array[i + 1]


if __name__ == "__main__":
    size = int(input())
    # array = [int(i) for i in input().strip().split()]
    array = list(map(int, input().split()))
    print(BuySellGoods(size, array))