#BOJ2293_동전1_G5
#https://www.acmicpc.net/problem/2293

n, k = map(int, input().split())
#리스트화 
v = [int(input()) for _ in range(n)]

dp = [0]*(k+1)
#동전 1개
dp[0] = 1

#점화식
for i in v:
    for j in range(i, k+1):
        dp[j] += dp[j-i]

print(dp[k])
