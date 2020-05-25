p1, c1, p2, c2 = input().split()

p1 = int(p1)
c1 = int(c1)
p2 = int(p2)
c2 = int(c2)

esq = p1 * c1
dir = p2 * c2

if(esq == dir):
    print(0)
elif(esq > dir):
    print(-1)
else:
    print(1)