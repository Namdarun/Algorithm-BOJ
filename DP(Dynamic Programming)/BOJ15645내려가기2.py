#BOJ15645_내려가기2_S1
#https://www.acmicpc.net/problem/15645

#최댓값, 최솟값 따로 저장해야한다.
#그리고 3 단락으로 나눠서 dp를 만들어나가야한다.

import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
max_value = [[0]*3 for _ in range(n)]
min_value = [[0]*3 for _ in range(n)]

for i in range(3):
    max_value[0][i] = graph[0][i]
    min_value[0][i] = graph[0][i]

for i in range(1, n):
    for j in range(3):
        if j == 0:
            max_value[i][j] += max(max_value[i-1][j], max_value[i-1][j+1])
            min_value[i][j] += min(min_value[i-1][j], min_value[i-1][j+1])
        #중간의 경우 양옆을 포함한다
        elif j == 1:
            max_value[i][j] += max(max_value[i-1][j], max_value[i-1][j-1], max_value[i-1][j+1])
            min_value[i][j] += min(min_value[i-1][j], min_value[i-1][j-1], min_value[i-1][j+1])

        #0일때와 겹치지 않게 주의
        elif j == 2:
            max_value[i][j] += max(max_value[i-1][j], max_value[i-1][j-1])
            min_value[i][j] += min(min_value[i-1][j], min_value[i-1][j-1])

        max_value[i][j] += graph[i][j]
        min_value[i][j] += graph[i][j]
        # print(graph)

print(max(max_value[n-1]), min(min_value[n-1]))