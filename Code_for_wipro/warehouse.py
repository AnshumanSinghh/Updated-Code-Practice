def warehouse(size, x, array): 
    '''
    docstring
    ''' 
    for i in range(size):
        if array[i] == x:
            return i
        elif array[i] < x:
            pass
        else:
            return i

# def array_split(size, x, array): 
#     '''
#     docstring
#     ''' 
#     mid = size // 2
#     if array[mid] == x:
#         return mid

#     elif array[mid] > x:
#         array = array[0:mid]
#         return warehouse(0, mid, x, array)

#     else:
#         array = array[mid:]
#         return warehouse(mid, size, x, array)
    
# Driver Code Starts
if __name__ == "__main__":
    size, x = [int(i) for i in input("Size & x: ").strip().split()]
    array = [int(ele) for ele in input("array elements: ").strip().split()]
    print(warehouse(size, x, array))
