# 큐
# 시간초과
'''
from collections import deque

def check_input(s, l):
    if "push" in s:
        l.append(int(list(s.split())[1]))
    elif "pop" in s:
        if l:
            print(l.popleft())
        else:
            print(-1)
    elif "size" in s:
        print(len(l))
    elif "empty" in s:
        if len(l) == 0:
            print(1)
        else:
            print(0)
    elif "front" in s:
        if l:
            print(l[0])
        else:
            print(-1)
    elif "back" in s:
        if l:
            print(l[-1])
        else:
            print(-1)
n = int(input())
l = []
l = deque(l)
for i in range(n):
    s = input()
    check_input(s, l)
'''
'''
# 통과
from collections import deque
import sys

input = sys.stdin.readline

def check_input(s, l):
    if "push" in s:
        l.append(int(list(s.split())[1]))
    elif "pop" in s:
        if l:
            print(l.popleft())
        else:
            print(-1)
    elif "size" in s:
        print(len(l))
    elif "empty" in s:
        if len(l) == 0:
            print(1)
        else:
            print(0)
    elif "front" in s:
        if l:
            print(l[0])
        else:
            print(-1)
    elif "back" in s:
        if l:
            print(l[-1])
        else:
            print(-1)
n = int(input())
l = []
l = deque(l)
for i in range(n):
    s = input()
    check_input(s, l)
'''

# 모범답안
from collections import deque
import sys

input = sys.stdin.readline

def check_input(s, l):
    if s.startswith("push"):
        l.append(int(list(s.split())[1]))
    elif s.startswith("pop"):
        if l:
            print(l.popleft())
        else:
            print(-1)
    elif s.startswith("size"):
        print(len(l))
    elif s.startswith("empty"):
        if len(l) == 0:
            print(1)
        else:
            print(0)
    elif s.startswith("front"):
        if l:
            print(l[0])
        else:
            print(-1)
    elif s.startswith("back"):
        if l:
            print(l[-1])
        else:
            print(-1)
n = int(input())
l = []
l = deque(l)
for i in range(n):
    s = input()
    check_input(s, l)
