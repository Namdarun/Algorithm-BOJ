#BOJ2792_보석상자_S1
#https://www.acmicpc.net/problem/2792

#모두가 다 평등하게 즉, 최댓값과 최솟값의 차이가 최소가 될 때 최댓값을 도출 
#질투심 함수 

import sys
input = sys.stdin.readline

#입력
n, m = map(int, input().split())
e = 0
pearl = []
for _ in range(m):
    pearl.append(int(input().rstrip()))

e = max(pearl)    
s = 1
# 출력할 최솟값 구하기
result= e 

while s <= e: 
    mid = (s + e) // 2

    per = 0
    #질투심 변수 만들고
    #보석을 mid만큼 나눴을 때 사람
    for i in pearl:
        main = i // mid
        other = i % mid
        
        #몫을 더해줘야함
        per += main
        #나머지가 존재하면 1추가
        if other > 0:
            per += 1

    #보석이 남았으면,
    if per > n:
        s = mid + 1

    #보석을 다 나눠줄 수 있으면 최솟값 도출
    else:
        #출력할 최솟값
        result = min(result, mid)
        e = mid - 1

print(result)