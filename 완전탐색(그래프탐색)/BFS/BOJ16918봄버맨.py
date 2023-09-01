#BOJ16918_봄버맨_S1
#https://www.acmicpc.net/problem/16918

#전형적인 bfs인데, 추가되는게 아니라 끊긴다
#구현을 곁들인 

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        #초기는 .으로 둬야함
        graph[x][y] = '.'
        #4방향탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < r and 0<= ny < c: 
                if graph[nx][ny] =='O':
                    graph[nx][ny] ='.'

#조건 추가 = 폭탄의 위치를 큐에 추가 
def check_bomb():
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'O':
                q.append((i, j))

def check_none():
    for i in range(r):
        for j in range(c):
            if graph[i][j] != 'O':
                #이중이퀄에 주의하자
                graph[i][j] = 'O'

r, c, n = map(int, input().split())
graph = [list(map(str, input().strip())) for _ in range(r)]

#인덱스 맞춰주기
n -= 1
while n:
    q = deque()
    check_bomb()
    check_none()
    n -= 1
    if n == 0:
        break
    bfs()
    n -= 1

# print(graph)
for i in graph:
    print(*i, sep='')