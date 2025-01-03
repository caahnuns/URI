continuar = 1

while(continuar == 1):

    n = input()

    if(int(n) == 0):
        continuar = 0
    else:
        tam = len(n)
        res = 0

        for i in range(0, tam):
            num = tam - i
            fat = 1

            for f in range(num, 0, -1):
                fat *= f
            
            res += (int(n[i]) * fat)

        print(res)