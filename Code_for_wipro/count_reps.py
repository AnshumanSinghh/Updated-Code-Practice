# to count number of rapeatations of each number [NOT OPTIMIZED]
l1 = [1,1,1,2,2,3,3,4,4,5,5,5,5,5,6,6,7]
ans = []
n = len(l1)
print("n: ", n)
counts = 0

for i in range(0, n - 1):
    if l1[i] == l1[i+1]:
        counts += 1
        print("--->", l1[i], l1[i+1], "counts==>", counts)
        continue    
    else: #l1[i] != l1[i + 1]:
        ans.append([l1[i], counts])
        counts = 1
ans.append([l1[i], counts])

print("ans is: ", ans)
