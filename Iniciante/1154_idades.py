executar = 1

total = 0
cont = 0

while(executar == 1):
    idade = int(input())
    if(idade < 0):
        executar = 0
    else:
        total += idade
        cont += 1
        
print("{:.2f}".format(total/cont))