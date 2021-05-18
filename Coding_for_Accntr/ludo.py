def ludo(s):
    ans = []
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == s:
                ans.append((i, j))
    return ans


if __name__ == '__main__':
    s = int(input("Enter the value of sum: "))
    print(ludo(s))