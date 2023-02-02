#BOJ9095 1,2,3더하기
#https://www.acmicpc.net/problem/9095
#dp

import sys
input = sys.stdin.readline

def solve(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return solve(n-1) + solve(n-2) + solve(n-3)


t = int(input())
for i in range(t):
    n = int(input())
    print(solve(n))