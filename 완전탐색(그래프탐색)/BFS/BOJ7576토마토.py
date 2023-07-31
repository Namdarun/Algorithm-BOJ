# #BOJ7576_토마토_G5
# #https://www.acmicpc.net/problem/7576

# #BFS?
# #인접한 토마토, 모든 토마토가 며칠이면 다 익게되는지 최소일
# #모두 1로 만들어져야하는데, -1로 '갇혀있으면' 불가능 -1출력

# from collections import deque

# m, n = map(int, input().split())
# box = []
# for i in range(n):
#     box.append(list(map(int, input().split())))
# queue = deque([])
# result = 0

# for i in range(n):
#     for j in range(m):
#         if box[i][j] == 1:
#             queue.append([i, j])

# def bfs():
#     while queue:
#         x, y = queue.popleft()
#         for dx, dy in [[0,1], [1,0], [0,-1], [-1,0]]:
#             nx,ny = x+dx, y+dy   
#             if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
#                 box[nx][ny] = box[x][y] + 1
#                 queue.append([nx, ny])

# bfs()
# for i in box:
#     for j in i:
#         #다 찾았는데 토마토를 익히지 못함
#         if j == 0:
#             print(-1)
#             exit()
#     #다른 경우 최댓값
#     result = max(result, max(i))
# print(result-1)


#재풀이 
#나이트이동과 비슷하다
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
q= deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i, j])

while q:
    x, y = q.popleft()
    #4방향탐색
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        #1을 string처리해야함에 유의하자
        #범위안에 있고 1을 만나면 이동할 수 있다.
        if 0<= nx < n and 0<= ny <m and graph[nx][ny] ==0:
            graph[nx][ny] = graph[x][y]+1
            q.append([nx, ny])

cnt = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    cnt = max(cnt, max(i))
print(cnt-1)