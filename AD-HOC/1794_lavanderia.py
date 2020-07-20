n = int(input())

la, lb = input().split()
sa, sb = input().split()

la = int(la)
lb = int(lb)
sa = int(sa)
sb = int(sb)

if((la <= n and n <= lb) and (sa <= n and n <= sb)):
    print("possivel")
else:
    print("impossivel")