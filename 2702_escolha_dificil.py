d = input()
total = [int(n) for n in d.split()]

r = input()
pedidos = [int(m) for m in r.split()]

passageiros = 0

for i in range(0, 3):
    if(pedidos[i] > total[i]):
        passageiros = passageiros + (pedidos[i] - total[i])
    
print(passageiros)