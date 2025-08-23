# 소수 구하기
# 시간 초과
'''
m, n = map(int, input().split())
for i in range(m, n+1):
    cnt = 0
    for j in range(2, i):
        if j * j > i:
            break
        if i % j == 0:
            cnt = 1
            break
    if cnt == 0:
        print(i)
'''
m, n = map(int, input().split())
l = [i for i in range(m, n+1) if i > 1]

for i in range(2, n+1):
    l = [i for i in l if (i == l[j] or i % l[j])]
    for i in range(2, l[j]):
        if i * i > l[j]:
            break
        if l[j] % i == 0:
            l.remove(l[j])
            break
    j += 1
print(l)

[2,3]
