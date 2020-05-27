cardapio = {1001 : 1.5, 1002 : 2.5, 1003 : 3.5, 1004 : 4.5, 1005 : 5.5}

n = int(input())
valor = 0

for i in range(0, n):
    item, q = input().split()
    valor_item = cardapio[int(item)] * int(q)
    valor += valor_item

print("{:.2f}".format(valor))