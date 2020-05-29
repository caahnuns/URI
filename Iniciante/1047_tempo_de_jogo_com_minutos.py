inn = input().split()

h_inicial = int(inn[0])
min_inicial = int(inn[1])
h_final = int(inn[2])
min_final = int(inn[3])

hora_total = h_final - h_inicial

minuto_total = min_final - min_inicial

if(minuto_total < 0):
    minuto_total += 60
    hora_total -= 1
    if(hora_total < 0):
        hora_total += 24


if(hora_total == 0 and minuto_total == 0):
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hora_total, minuto_total))