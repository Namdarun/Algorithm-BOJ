#BOJ1793_타일링_S2
#https://www.acmicpc.net/problem/1793

import sys
input = sys.stdin.readline

#점화식
def check(n):
    dp = [0] * 251
    dp[0] = 1
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n+1):
        dp[i] = dp[i-1] + 2*dp[i-2]

    return dp[n]

while True:
    try:
        n = int(input())
        print(check(n))
    except:
        break
    
    
