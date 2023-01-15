#BOJ11866_요세푸스문제0
#디큐사용
from collections import deque

#입력
N, K = map(int, input().split())
q = deque()

#입력(1번부터)
for i in range(1, N+1):
    q.append(i)
    
print("<", end='')
#q가 존재하는 동안 하나씩 빼서 출력한다
while q:
    for i in range(K-1):
        q.append(q.popleft())
    print(q.popleft(),end='')
    if q:
        print(",", end=' ')
        
print(">")