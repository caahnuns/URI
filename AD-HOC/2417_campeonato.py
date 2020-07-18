info = input().split()

gol_c = int(info[2])
gol_f = int(info[5])

pt_c = (int(info[0]) * 3) + int(info[1])
pt_f = (int(info[3]) * 3) + int(info[4])

if((pt_c > pt_f) or (pt_c == pt_f and gol_c > gol_f)):
    print("C")
elif((pt_f > pt_c) or (pt_c == pt_f and gol_f > gol_c)):
    print("F")
else:
    print("=")