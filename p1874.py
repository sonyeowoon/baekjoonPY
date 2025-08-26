n = int(input())
l = []
s = []
flg = 1
for i in range(n):
    l.append(int(input()))
stack = []
for i in range(1,n+1):
    stack.append(i)
    s.append('+\n')
    while (stack and l and stack[-1] == l[0]):
        stack.pop()
        l.pop(0)
        s.append('-\n')
    if (l and stack and l[0] < stack[-1]):
        flg = 0
        print('NO')
        break
if flg:
    print(''.join(s))
