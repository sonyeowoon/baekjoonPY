import sys
from collections import deque

input = sys.stdin.readline
t = int(input())
for i in range(t):
    n, p = map(int, input().split())
    deq = deque(map(int, input().split()))
    cnt = 1
    idx = p
    while (deq):
        maxdeq = max(deq)
        cur = deq.popleft()
        if cur < maxdeq:
            deq.append(cur)
            if idx == 0:
                idx = len(deq) - 1
        else:
            if idx == 0:
                print(cnt)
                break
            idx -= 1
        cnt += 1
