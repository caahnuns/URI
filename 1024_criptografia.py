n = int(input())

while(n > 0):
    a = input()

    s = ""
    e = ""

    for i in range(0, len(a)):
        if(a[i].isalpha()):
            s += (chr(ord(a[i]) + 3))
        else:
            s += (a[i])

    rev = s[::-1]

    mid = len(rev) // 2

    start = rev[0:mid:]
    end = rev[mid:len(rev):]

    for i in range(0, len(end)):
        e += (chr(ord(end[i]) - 1))

    print(start + e)
    n -= 1