n = int(input())
pesquisados = []

for i in range(0, n):
    pesquisados.append(input())

q = int(input())
pesquisar = []

for i in range(0, q):
    pesquisar.append(input())

for a in range(0, len(pesquisar)):

    res = 0
    tam = 0

    for i in range(0, len(pesquisados)):

        if(pesquisados[i].startswith(pesquisar[a])):
            res += 1
            if(len(pesquisados[i]) > tam):
                tam = len(pesquisados[i])
    
    if(res == 0):
        res = -1

    if(tam > 0):
        print(res, tam)
    else:
        print(res)