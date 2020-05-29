cardapio = {1 : 4.0, 2 : 4.5, 3 : 5.0, 4 : 2.0, 5 : 1.5}

inn = input().split()

cod = int(inn[0])
qtde = int(inn[1])

valor = qtde * cardapio[cod]

print("Total: R$ {:.2f}".format(valor))