import sys
input = sys.stdin.readline
n = int(input())
if n == 0:
    print(0)
    exit()
avrg = n / 100 * 15
if (avrg // 0.5) % 2:
    avrg = int(avrg) + 1
else:
    avrg = int(avrg)
l = []
for i in range(n):
    l.append(int(input()))
l.sort()
l = l[avrg:n-avrg]
ret = sum(l) / (n-avrg*2)
if (ret // 0.5) % 2:
    ret = int(ret) + 1
else:
    ret = int(ret)
print(ret)
