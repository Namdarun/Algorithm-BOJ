#BOJ15486_퇴사2_G5
#https://www.acmicpc.net/problem/15486

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