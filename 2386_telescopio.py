t = int(input())
n = int(input())

aux = 0

for i in range(0, n):
    f = int(input())
    if((f * t) >= 40000000):
        aux += 1
    
print(aux)