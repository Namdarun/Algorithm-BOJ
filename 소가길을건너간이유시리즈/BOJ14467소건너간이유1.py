#BOJ14467_소가길을건너간이유1_B1
#https://www.acmicpc.net/problem/14467

import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
cows = [-1]*11
for _ in range(n):
    a,b = map(int, input().split())
    if cows[a] == -1:
        cows[a] = b
    elif cows[a] != b:
        cows[a] = b
        cnt += 1

print(cnt)