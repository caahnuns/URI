aux = 0

for i in range(1, 6):
    num = int(input())
    if(num % 2 == 0):
        aux += 1

print("{} valores pares".format(aux))