def hailstone(x):


    n = 1
    while x != 1:
        print(x)
        if x % 2 == 1:
            x = 3 * x + 1
            n += 1
        else:
            x = x // 2
            n += 1
    print(1)
    return n
a = hailstone(10)
print(a)
