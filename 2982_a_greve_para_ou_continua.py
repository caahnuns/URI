n = int(input())

gastos = 0
verba = 0

for i in range(0, n):
    t, c = input().split()
    if(t == "G"):
        gastos += int(c)
    else:
        verba += int(c)

if(verba < gastos):
    print("NAO VAI TER CORTE, VAI TER LUTA!")
else:
    print("A greve vai parar.")