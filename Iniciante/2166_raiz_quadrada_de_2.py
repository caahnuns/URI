n = int(input())

d = 1/2

if(n==0):
   print("{:.10f}".format(1))
else:
    while (n >= 2):
        d = (1 / (2 + d))
        n -= 1
    print("{:.10f}".format(1 + d))