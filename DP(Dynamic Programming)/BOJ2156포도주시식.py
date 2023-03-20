#BOJ2156_포도주시식 
#https://www.acmicpc.net/problem/2156

import sys
input = sys.stdin.readline

N = int(input())
size = [0]
for i in range(N):
    num = int(input())
    size.append(num)
#여기까지 입력 

#인덱스를 맞춰주기 위해 1번값추가
dp = [0]
dp.append(size[1])

#1보다 크다면
if N > 1:
    dp.append(size[1] + size[2])
for i in range(3, N + 1):
    dp.append(max(dp[i - 1], dp[i - 3] + size[i - 1] + size[i], dp[i - 2] + size[i]))
print(dp[N])