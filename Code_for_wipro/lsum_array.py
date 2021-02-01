def largest_sum_array(array, size): 
    '''
    To calculate the maximum subarray sum possible [based on: KADENS ALGORITHM]
    ''' 
    temp_sum = flag = l_sum = 0
    t_min = array[0]

    for i in range(size):

        temp_sum += array[i] # to store the temporary sum
        temp_sum = max(temp_sum, 0) # to make temp_sum non-negative number, if temp_sum becomes -ve make it zero
        l_sum = max(temp_sum, l_sum) # to store the max sum until now

        if array[i] < 0: # to check if all the number are negative number or not
            flag += 1
            t_min = max(t_min, array[i])

    if flag == size: # if all are -ve numbers means, our will become equals to size of the array
        return t_min # if so return the first num as in case where if all number are -ve the 1st 
                        # element of array will be going to be the largest sum possible that array or
                        # another way to achieve this is by checking if l_sum == 0, l_sum will be zero
                        # only if all elements are -ve otherwise l_sum > 0.

    return l_sum # if all elements are not -ve it means return the sum what we have stored in l_sum


# Driver Code Starts
if __name__ == "__main__":
    array = [int(i) for i in input("Enter the array elements: ").strip().split()]
    size = int(input("Enter the size of array: "))
    print(largest_sum_array(array, size))
