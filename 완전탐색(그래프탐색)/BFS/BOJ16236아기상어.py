#BOJ16236_아기상어_G3
#https://www.acmicpc.net/problem/16236

# 이동시간이 time
# 물고기 크기 size
# 최단거리를 구하는 BFS를 사용
# 그러나 중요한 조건
# 거리가 가까운 물고기가 많다면, 가장 위, 가장 왼쪽부터 -> 정렬?

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
sea = []
for _ in range(n):
    sea.append(list(map(int, input().split())))

#상어의 위치
for i in range(n):
    for j in range(n):
        if sea[i][j] == 9:
            x = i
            y = j

#도출할 시간
time = 0

#처음 입력값
x,y,size = 0,0,2

def BFS(x,y, size):
    dist = [[0]*n for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    temp = []