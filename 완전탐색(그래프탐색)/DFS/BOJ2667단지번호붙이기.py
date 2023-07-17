#BOJ2667_단지번호붙이기_S1
#https://www.acmicpc.net/problem/2667

import sys
input = sys.stdin.readline

#4방향 탐색을 하는 것 외에 다른 게 없다
dx = [1,0,-1,0]
dy = [0,-1,0,1]
n = int(input())
graph = [list(input()) for _ in range(n)]
# print(graph)
cnt = 0
result = []

#DFS 재귀탐색 구현
def dfs(x,y):
    global cnt 
    #재귀 돌릴 때 방문한 곳은 0으로 바꿈 (바꿀 때 ==가 아님에 주의)
    graph[x][y]=0
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        # if 0 <= nx < n and 0 <= ny < n:
        if graph[nx][ny] == '1':
            dfs(nx,ny)


for i in range(n):
    for j in range(n):
        if graph[i][j]=='1':
            cnt = 0
            dfs(i,j)
            result.append(cnt)

print(len(result))
result.sort()
for i in result:
    print(i)
