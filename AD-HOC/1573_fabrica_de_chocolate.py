continuar = 1

while(continuar == 1):
    x, y, z = input().split()

    x = int(x)
    y = int(y)
    z = int(z)

    if(x == y == z == 0):
        continuar = 0
    else:
        vol = x * y * z
        print(int(vol ** (1/3)))