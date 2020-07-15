permutacao = input()

hashcode = {}
for i in range(0, len(permutacao)):
    hashcode[permutacao[i]] = chr(i+97)

encrypt = input()

decrypt = ""

for c in range(0, len(encrypt)):
    decrypt += (hashcode[encrypt[c]])

print(decrypt)