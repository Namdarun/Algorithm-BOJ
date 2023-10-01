#BOJ1059_좋은구간_S4
#https://www.acmicpc.net/problem/1059

import sys
input = sys.stdin.readline

s = int(input())
l = list(map(int, input().split()))
n = int(input())

l.sort()

if n in l:
    print(0)
else:
    cnt = 0
    check_min = 0
    check_max = 0
    for i in l:
        if i < n:
            check_min = i
        elif i > n:
            check_max = i
            break
    
    for i in range(check_min+1, check_max-1):
        for j in range(i+1, check_max):
            if i <= n and j >= n:
                cnt += 1
    
    print(cnt)
            