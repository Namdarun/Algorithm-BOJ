#BOJ17608_막대기_B2
#https://www.acmicpc.net/problem/17608

import sys
input = sys.stdin.readline 

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

end = arr[-1]
cnt = 1

for i in reversed(range(n)):
    if arr[i] > end:
        cnt += 1
        end = arr[i]

print(cnt)