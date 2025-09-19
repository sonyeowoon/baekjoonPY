# 피보나치 함수
'''
# 시간초과
import sys
input = sys.stdin.readline
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

t = int(input())
for i in range(t):
    n = int(input())
    if n == 0:
        print("1 0")
    else:
        print(fibonacci(n-1), fibonacci(n))
'''

import sys
input = sys.stdin.readline
zero = [0] * 41
one = [0] * 41
zero[0], one[0] = 1, 0
zero[1], one[1] = 0, 1
for i in range(2, 41):
    zero[i] = zero[i-1] + zero[i-2]
    one[i] = one[i-1] + one[i-2]
t = int(input())
for i in range(t):
    n = int(input())
    print(zero[n], one[n])
