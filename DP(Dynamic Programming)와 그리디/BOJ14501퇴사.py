# #BOJ14501_퇴사_S3
# #https://www.acmicpc.net/problem/14501

#전형적인 DP문제 
#탑다운, 바텀업으로 나눠서 풀어보자
#2차원 배열을 봐야하므로 2차원배열로 받는다.

#bottom-up
import sys
input = sys.stdin.readline

n = int(input())

time = [list(map(int, input().split())) for _ in range(n)]

dp = [0 for _ in range(n+1)]

#최대값을 dp에 저장해나간다. 
for i in range(n):
    for j in range(i+time[i][0], n+1):
        if dp[j] < dp[i] + time[i][1]:
            dp[j] = dp[i] + time[i][1]

#마지막 저장값이 j를 기준으로 한 최대수익
print(dp[-1])

#top-down
#거꾸로부터 계산해나가는 방식
import sys
input = sys.stdin.readline

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n+1)]

for i in range(n-1, -1, -1):
    if i + li[i][0] > n:
        dp[i] = dp[i+1]

    else:
        dp[i] = max(dp[i+1], li[i][1] + dp[i+ li[i][0]])
print(dp[0])

#DFS
import sys
input = sys.stdin.readline

n = int(input())
t = [0 for _ in range(n)]
p = [0 for _ in range(n)]
for i in range(n):
    t[i], p[i] = map(int, input().split())

result = 0
def solution(fired, now):
    global result 
    #퇴사날일때 업데이트
    if fired == n:
        result = max(now, result)
        return
    
    #상담할때
    if fired + t[fired] <= n:
        solution(fired + t[fired], now+p[fired])
    
    #아니면 dfs
    solution(fired + 1, now)

solution(0, 0)
print(result)