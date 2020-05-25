inn = float(input())

if(inn >= 0 and inn <= 25):
    print("Intervalo [0,25]")
elif(inn > 25 and inn <= 50):
    print("Intervalo (25,50]")
elif(inn > 50 and inn <= 75):
    print("Intervalo (50,75]")
elif(inn > 75 and inn <= 100):
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")