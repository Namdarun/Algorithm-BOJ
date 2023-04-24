#BOJ1182_부분수열의합_S2
#https://www.acmicpc.net/problem/1182

import sys
from itertools import combinations
input = sys.stdin.readline

#입력
n, s = map(int, input().split())
arr = list(map(int, input().split()))
#누적합 
cnt = 0
for i in range(1, n+1):
    #arr에서 i개를 뽑는 모든 경우의 수 
    comb = combinations(arr, i)

    #그 경우의 수 x끼리의 합이 s일때 카운트 하나 더하기
    for x in comb:
        if sum(x) == s:
            cnt += 1

print(cnt)