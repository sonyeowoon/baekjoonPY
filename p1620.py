n, m = map(int, input().split())
d = dict()
for i in range(1, n+1):
    d[str(i)] = input()
reverseD = {v:k for k,v in d.items()}
for i in range(m):
    s = input()
    if s.isdigit():
        print(d[s])
    else:
        print(reverseD[s])
