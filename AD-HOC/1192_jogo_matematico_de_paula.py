n = int(input())

for i in range(0, n):

    inn = input()

    a = int(inn[0])
    b = int(inn[2])

    if(a == b):
        print(a * b)
    elif(inn[1].isupper()):
        print(b - a)
    elif(inn[1].islower()):
        print(a + b)