n, m = map(int, input().split())
a = set()
for i in range(n):
    a.add(input())
b = set()
for i in range(m):
    b.add(input())
tmp = list(a.intersection(b))
tmp.sort()
print(len(tmp))
for name in tmp:
    print(name)
