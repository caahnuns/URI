text = input()

decod = ""

inn = text.split()

for i in range(1, len(inn) + 1):
    w = inn[i - 1]
    for l in range(1, len(w) + 1):
        if(l % 2 == 1):
            decod += w[l]
    decod += " "

print(decod[:-1])