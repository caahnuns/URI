aux = 7

for i in range(1, 11, 2):
    for j in range(aux, 17):
        print("I={} J={}".format(i, j))
        print("I={} J={}".format(i, j - 1))
        print("I={} J={}".format(i, j - 2))
        aux += 2
        break

""" i = 1
j = 7

while(i <= 9):
    print("I={} J={}".format(i, j))
    print("I={} J={}".format(i, j - 1))
    print("I={} J={}".format(i, j - 2))

    i += 2
    j += 2 """