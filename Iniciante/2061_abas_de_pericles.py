n, m = input().split()

abas = int(n)
m = int(m)

for i in range(0, m):
    acao = input()
    if(acao == "fechou"):
        abas += 1
    elif(acao == "clicou"):
        abas -= 1

print(abas)