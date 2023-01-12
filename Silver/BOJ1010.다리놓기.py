#BOJ1010_다리놓기

import sys
input = sys.stdin.readline

N = int(input())
#2차원배열
dp = [[0]*30 for _ in range(30)]

for i in range(30):
    for j in range(30):
        #1이면 j개
        if i == 1:
            dp[i][j] = j
            
        #2개 이상일때 숫자가 같으면 1가지방법 / 그 외는 dp
        else:
            if i == j:
                dp[i][j] = 1
                
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                
for k in range(N):
    x, y = map(int, input().split())
    print(dp[x][y])