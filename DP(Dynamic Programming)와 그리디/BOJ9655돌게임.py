#BOJ9655_돌게임_S5
#https://www.acmicpc.net/problem/9655

#홀수일 때 상근, 짝수일때 창영

import sys
input = sys.stdin.readline

n = int(input())
dp=[0]*1001
dp[1] = 1
dp[2] = 0
dp[3] = 1

for i in range(4, 1001):
    if dp[i-1] == 1 or dp[i-3] == 1:
        dp[i] = 0
    else:
        dp[i] = 1

if dp[n] == 1:
    print('SK')
else:
    print('CY')