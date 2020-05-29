abc = {chr(i+64):i for i in range(1,27)}

n = int(input())

while(n > 0):

    val = 0
    valor = 0

    l = int(input())
    
    for i in range(0, l):
        text = input()
        for c in range(0, len(text)):
            val = (abc[text[c]] - 1) + c + i
            valor += val

    print(valor)
    n -= 1