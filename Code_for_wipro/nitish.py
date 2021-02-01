def token_generator(num): 
    ans = ""
    for i in range(len(num)):
        x= int(num[i])
        if x % 2 == 0:
            ans += str(x + 1)
        else:
            ans += str(x - 1)

    return ans
        

# Driver Code Starts
if __name__ == "__main__":
    num = input()
    print(token_generator(num))
    
