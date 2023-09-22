#BOJ16439_치킨치킨치킨_S4
#https://www.acmicpc.net/problem/16439

import sys
from itertools import combinations
input = sys.stdin.readline 

n, m = map(int, input().split())
pre = [list(map(int, input().split())) for _ in range(n)]
result = 0

for i, j, k in combinations(range(m), 3):
    sum = 0
    for l in range(n):
        sum += max(pre[l][i], pre[l][j], pre[l][k])
    result = max(result, sum)

print(result)
