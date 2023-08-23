#BOJ2468_안전영역_S1
#https://www.acmicpc.net/problem/2468

#BFS
import sys
input = sys.stdin.readline
from collections import deque

#입력
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(n):
        if arr[i][j] > cnt:
            cnt = arr[i][j]

#BFS 함수 
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def bfs(x,y,cnt):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            #범위 벗어남
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            #전체범위 탐색
            if arr[nx][ny] > cnt and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))

#계산하기 -> 결과값 도출
#방문여부도 2차원배열 
result = 0
for i in range(cnt):
    visited = [[0]*n for _ in range(n)]
    result_cnt = 0

    for a in range(n):
        for b in range(n):
            if arr[a][b] > i and visited[a][b] == 0:
                bfs(a, b, i)
                result_cnt += 1
    
    if result < result_cnt:
        result = result_cnt

print(result)

#DFS 추가해야함
import sys
# 재귀 깊이 설정
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

#4방향
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    visited[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < n) and visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny)

    return 1

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0
for h in range(101):
    cnt = 0
    visited = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] > h:
                visited[i][j] = arr[i][j]
    
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                cnt += dfs(i, j)

    result = max(result, cnt)
print(result)