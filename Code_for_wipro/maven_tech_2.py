'''
Find name closensess between two strings:
Given: 
    If two strings have common char at same index then ignore next time this charcater and increment count by +2.
    Else if both strings have same char but at different position then don't ignore nect time and increase the count by +1.
'''
input1 = list(input("Input1: "))  # string is immutable so convert it into list.
input2 = list(input("Input2: "))  
res = 0
for i in range(len(input1)):
    for j in range(len(input2)):
        # to treat caps char and small char same, I have added 32 to the ascii value of the char and then converted into char.
        if (input1[i] == input2[j] or chr(ord(input1[i]) + 32) == input2[j]) and i == j: 
            input2[j] = 0
            res += 2
        elif input1[i] == input2[j]:
            res += 1
print("Name Closeness is:", res)
