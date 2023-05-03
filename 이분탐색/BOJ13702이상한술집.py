#BOJ13702_이상한술집_S3
#https://www.acmicpc.net/problem/13702

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

start = 1
end = max(arr)

while (start <= end):
    mid = (start + end) // 2
    cnt = 1

    for i in range(n):
        cnt += arr[i] // mid 

    if cnt > k:
        start = mid + 1
    else: 
        end = mid - 1 

print(end)




