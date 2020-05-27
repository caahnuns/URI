n = int(input())

copos_quebrados = 0

for i in range(0, n):
    l, c = input().split()
    
    l = int(l)
    c = int(c)

    if(l > c):
        copos_quebrados += c

print(copos_quebrados)