n = int(input())

d = 1/6

if(n==0):
   print("{:.10f}".format(3))
else:
    while (n >= 2):
        d = (1 / (6 + d))
        n -= 1
    print("{:.10f}".format(3 + d))