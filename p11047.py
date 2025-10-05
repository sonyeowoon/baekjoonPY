from collections import deque
n, k = map(int, input().split())
deq = deque()
for i in range(n):
    deq.appendleft(int(input()))
cnt = 0
for i in range(n):
    if k == 0:
        break
    cur = deq[i]
    if cur > k:
        continue
    cnt += k // cur
    k %= cur
print(cnt)
