#BOJ2164_카드2_S4
#https://www.acmicpc.net/problem/2164

# 시간초과 버전 
N = int(input())
card = []
for i in range(1,N+1):
    card.append(i)

while len(card) > 0:
    card.pop(0)
    plus = card.pop(0)
    card.append(plus)
    if len(card) == 1:
        print(*card)
        break

#통과
from collections import deque
N = int(input())
# deque에 담기
# deque([1, 2, 3, 4, 5, 6])
card = deque(range(1, N+1))

while(len(card) >1):
    card.popleft()
    # 한 번더 뽑아서 붙여주기
    plus = card.popleft()
    card.append(plus)
    
print(card[0])