#BOJ14502_연구소_G4
#https://www.acmicpc.net/problem/14502

#딥카피 다시 복기하기 -> 원래의 arr을 저장해야함
#함수 2개로 만들기
#방문처리는 실패함 -> 다음에 다시 풀어볼 것 

import sys, copy
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0 
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            cnt += 1
max_value = 0
#범위탐색하는 bfs함수
def bfs():
    global max_value
    check_arr = copy.deepcopy(arr)
    q = deque()

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                q.append((i,j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and check_arr[nx][ny] == 0:
                check_arr[nx][ny] =2
                q.append((nx, ny))
    cnt = 0
    for i in range(n):
        cnt += check_arr[i].count(0)
    max_value = max(max_value, cnt)

#3개의 벽을 세울 재귀함수
def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(cnt+1)
                arr[i][j] = 0

wall(0)
print(max_value)