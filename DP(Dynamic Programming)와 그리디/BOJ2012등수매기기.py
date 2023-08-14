#BOJ2012_등수매기기_S3
#https://www.acmicpc.net/problem/2012

import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

#정렬해야함
arr.sort()

result = 0
for i in range(1, n+1):
    result += abs(i-arr[i-1])

print(result)