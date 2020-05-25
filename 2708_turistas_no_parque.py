fim = False

ida = 0
volta = 0
jipe = 0

while(fim == False):
    info = input()

    if(info.startswith("SALIDA")):
        ida += int(info[7:])
        jipe += 1
    elif(info.startswith("VUELTA")):
        volta += int(info[7:])
        jipe -= 1
    elif(info == "ABEND"):
        fim = True

print(ida - volta)
print(jipe)