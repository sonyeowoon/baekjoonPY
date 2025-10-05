t = int(input())
for i in range(t):
    n = int(input())
    out = 0
    for j in range(n+1):
        if j % 2:
            out += j
    print(out)
