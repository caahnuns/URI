m = int(input())
filhos = []

a = int(input())
filhos.append(a)

b = int(input())
filhos.append(b)

c = m - (a + b)
filhos.append(c)

print(max(filhos))