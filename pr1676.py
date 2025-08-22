n = int(input())
result = 1
while n > 1:
    result *= n
    n -= 1
result = list(str(result))
cnt = 0
while (result and result[-1] == '0'):
    cnt += 1
    result.pop(-1)
print(cnt)
