n = int(input())

inn = 0
out = 0

for i in range(1, n+1):
    x = int(input())
    if(x >= 10 and x <= 20):
        inn += 1
    else:
        out += 1

print("{} in".format(inn))
print("{} out".format(out))