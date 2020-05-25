t = int(input())

a, b, c, d, e = input().split()

notas = []

notas.append(int(a))
notas.append(int(b))
notas.append(int(c))
notas.append(int(d))
notas.append(int(e))

print(notas.count(t))