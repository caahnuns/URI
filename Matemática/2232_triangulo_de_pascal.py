t = int(input())
v = 1

for v in range(1, t+1):

    n = int(input())

    triangulo = 0

    for i in range(n-1, -1, -1):
        linha = 2 ** i
        triangulo += linha

    print(triangulo)