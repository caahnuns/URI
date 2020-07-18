exec = 1

while(exec == 1):

    num = input().split()

    a = int(num[0])
    b = int(num[1])

    if(a > b):
        print("Decrescente")
    elif(b > a):
        print("Crescente")
    elif(a == b):
        exec = 0