def counting_valley(pattern):

    # valley steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
    # starting from level = 0; as hike is starting from sea level A/Q
    level = valley = 0  

    for x in pattern:

        # if its "U" then increse the level
        if x == "U":
            level += 1

        # other-wise if it's "D" and level = 0 increase the valley by one, as A/Q valley starting with
        # step down and ending at sea level
        elif x == "D":
            if level == 0:
                valley += 1

            # if level is not equals zero, it means we are goind below sea level so, level should
            # be decresed by one.
            level -= 1

    return valley

if __name__ == '__main__':
    n = int(input("Enter the length of array: "))
    pattern = input("Enter the pattern in Caps letter: ")
    ans =counting_valley(pattern)
    print(ans)
    
