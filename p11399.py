n = int(input())
times = list(map(int, input().split()))
times.sort()
total = 0
p = 0
for i in range(n):
    p += times[i]
    total += p
print(total)
