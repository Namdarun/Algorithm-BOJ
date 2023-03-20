#BOJ1463_1로 만들기_S3
#https://www.acmicpc.net/problem/1463

n = int(input())
#연산하는데 걸리는 최솟값
dp = [0]*(n+1)
dp[0] = 1

for i in range(2, n+1):
    #횟수를 더해줌
    dp[i] = dp[i-1]+1
    #3으로 나눠떨어지면 3으로 나눔
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    #2로 나눠떨어지면 2로 나눔
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
print(dp[n])