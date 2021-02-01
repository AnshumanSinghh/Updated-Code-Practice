# another approach without using list slicing
def rotateLeft(n, d, arr):
    for i in range(d):
        arr = rotatearr(n, arr)
        print(f"for i = {i} array is {arr}")
    return arr


def rotatearr(n, arr):
    first = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
        print("array after exchng: ", arr)
    arr[n-1] = first
    print("array after left rotation: ", arr)
    return arr


n, d = map(int, input().split())
arr = list(map(int, input().split()))
for i in rotateLeft(n, d, arr):
    print(i, end=" ")   

def ram_katha(ram, sita): 
    '''
    About Lord Rama and Maa Sita
    ''' 
    return f"Lord {ram} and Maa {sita} Finally meets each other..."

print(ram_katha("Ram", "Seeta"))

