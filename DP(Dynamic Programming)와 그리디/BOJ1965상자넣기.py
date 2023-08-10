#BOJ1965_상자넣기_S2
#https://www.acmicpc.net/problem/1965

import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

#본인을 포함한 값을 세어주지 않으므로 마지막에 1을 더해준다.
dp = [0]*n
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

# print(dp)
print(max(dp)+1)
