t = int(input())

for i in range(1, t+1):
    n, k = input().split()

    n = int(n)
    k = int(k)
    
    print((n // k) + (n % k))