import sys

a = 0
b = 0
c = 0
tmp = 0
for line in sys.stdin:
    n = line.split()
    a = int(n[0])
    b = int(n[1])
    c = int(n[2])
    cnt = 0
    while(c - a > 2):
        cnt += 1
        if(b - a < c - b):
            a = b + 1
            tmp = a
            a = b
            b = tmp
        else:
            c = b - 1
            tmp = c
            c = b
            b = tmp
    print(cnt)
