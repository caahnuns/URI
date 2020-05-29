i = int(input())

km = 0

for n in range(0, i):
    t, v = input().split()
    t = int(t)
    v = int(v)
    km += (t * v)

print(km)