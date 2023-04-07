#BOJ2875_대회OR인턴_B3
#https://www.acmicpc.net/problem/2875

m, n, k = map(int, input().split())
cnt = 0
#최대의 팀 수 
#2명 여, 1명 남 
#조건 설정
while m >= 2 and n >= 1 and m+n >= k+3:
    m -= 2
    n -= 1
    cnt += 1

print(cnt)