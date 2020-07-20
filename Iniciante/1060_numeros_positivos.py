pos = 0

for i in range(0, 6):
    n = float(input())
    if(n > 0):
        pos += 1

print("{} valores positivos".format(pos))