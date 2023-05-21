#BOJ1158_요세푸스문제_S4
#https://www.acmicpc.net/problem/1158

#시간초과에 주의해 deque를 사용했다. 
from collections import deque
n, k = map(int, input().split())
saram = deque()
for i in range(1, n+1):
    saram.append(i)

result = []
while saram:
    for _ in range(k-1):
        saram.append(saram.popleft())
    
    result.append(saram.popleft())

#replace 메서드 기억하기
print(str(result).replace('[','<').replace(']','>'))