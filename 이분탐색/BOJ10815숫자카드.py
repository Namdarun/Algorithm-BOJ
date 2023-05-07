#BOJ10815_숫자카드_S5
#https://www.acmicpc.net/problem/10815

# n = int(input())
# card = list(map(int, input().split()))
# m = int(input())
# check = list(map(int, input().split()))

# card.sort()

#시간초과 버전 
# for i in check:
#     if i in card:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')


n = int(input())
card = list(map(int, input().split()))

card.sort()

def binary(num):
    s = 0
    e = n-1
    while s <= e:
        mid = (s+e)//2
        if card[mid] == num:
            return 1
        elif card[mid] > num:
            e = mid - 1
        else:
            s = mid + 1

    return 0

m = int(input())
check = list(map(int, input().split()))

for i in check:
    print(binary(i), end=' ')