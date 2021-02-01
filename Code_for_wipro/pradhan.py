def gen_key(a, b, c):            

    d1 = min(int(a[0]), int(b[0]), int(c[0]))
    d2 = max(int(a[1]), int(b[1]), int(c[1]))
    d3 = min(int(a[2]), int(b[2]), int(c[2]))
    d4 = max(int(a[3]), int(b[3]), int(c[3]))

    return d1*1000 + d2*100 + d3*10 + d4

# Driver Code Starts
if __name__ == "__main__":
    a, b, c = [i for i in input().strip().split()]
    print(gen_key(a, b, c))
    