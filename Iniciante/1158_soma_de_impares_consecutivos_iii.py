t = int(input())

for e in range(0, t):
    num = input().split()

    x = int(num[0])
    y = int(num[1])

    if(x % 2 == 0):
        x += 1

    res = x

    for i in range(1, y):
        x += 2
        res += x

    print(res)