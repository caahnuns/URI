continuar = True

while(continuar):
    x, y = input().split()

    if(int(x) > 0 and int(y) > 0):
        print("primeiro")
    elif(int(x) < 0 and int(y) > 0):
        print("segundo")
    elif(int(x) < 0 and int(y) < 0):
        print("terceiro")
    elif(int(x) > 0 and int(y) < 0):
        print("quarto")
    elif(int(x) == 0 or int(y) == 0):
        continuar = False