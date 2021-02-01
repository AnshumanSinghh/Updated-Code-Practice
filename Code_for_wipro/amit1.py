def breach(num):  
    maxnum = [0, 0, 0, 0]
    for i in range(len(num)):
        maxnum[i] = int(num[i])
    maxnum.sort(reverse=True)
    return maxnum[0], maxnum[1]

if __name__ == "__main__":
    num = list(input().split())
    lar = s_lar = 0
    for x in num:
        ans = breach(x)
        lar += ans[0]
        s_lar += ans[1]
    print(lar - s_lar)
