
def min_steps(n):
    steps = 0
    print(f"n = {n} and steps = {steps}")
    while n > 0:
        if n % 2 == 0:
            n = n / 2
            print(f"Even[n /= 2]: n = {n} and steps = {steps}")
        else:
            n -= 1
            print(f"Odd[n -= 1]: n = {n} and steps = {steps}")
        steps += 1
    return steps


if __name__ == '__main__':
    n = int(input("Enter the value of n: "))
    print(min_steps(n))

