# 숫자 카드 2
'''
# 시간 초과
n = int(input())
cards = list(map(int, input().split()))
m = input()
ints = list(map(int, input().split()))
for num in ints:
    print(cards.count(num), end=' ')
'''
n = int(input())
cards = list(map(int, input().split()))
dicts = {}
for i in range(n):
    if str(cards[i]) in dicts:
        dicts[str(cards[i])] += 1
    else:
        dicts[str(cards[i])] = 1
m = int(input())
ints = list(map(int, input().split()))
for num in ints:
    if str(num) in dicts:
        print(dicts[str(num)], end=' ')
    else:
        print(0, end=' ')
