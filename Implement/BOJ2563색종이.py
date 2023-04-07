#BOJ2563_색종이_S5
#https://www.acmicpc.net/problem/2563

import sys
input = sys.stdin.readline
n = int(input())
paper = [[0]*100 for _ in range(100)]

cnt = 0
for i in range(n):
    garo, sero = map(int, input().split())

    for a in range(garo, garo+10):
        for b in range(sero, sero+10):
            paper[a][b] = 1

# print(paper)

result = 0
for k in paper:
    result += k.count(1)

print(result)
