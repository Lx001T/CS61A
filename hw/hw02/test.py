identity = lambda x : x

n = 5
sum = 0
while n > 0:

    sum += identity(n) * identity(n-1)
    n -= 1
    print(sum)