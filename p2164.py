# 카드2
'''
# 시간초과
n = int(input())
l = [x for x in range(1, n+1)]
while (len(l) != 1):
    l.pop(0)
    if len(l) == 1:
        break
    l.append(l.pop(0))
print(l[0])
'''
n = int(input())
total = 1
while (total < n):
    total = total * 2
if n != total:
    total = total - (total - n) * 2
print(total)
'''
# 모범답안
from collections import deque

n = int(input())
l = [x for x in range(1, n+1)]
l = deque(l)
while (len(l) != 1):
    l.popleft()
    if len(l) == 1:
        break
    l.append(l.popleft())
print(l[0])
'''
