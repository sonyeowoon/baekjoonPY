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

for i in range(2, int(n ** 0.5) + 1):
    l = [j for j in l if j == i or j % i]
for i in l:
    print(i)
