#BOJ7569_토마토_G5
#https://www.acmicpc.net/problem/7569

#BFS - 7576에 높이만 추가 
#인접한 토마토, 모든 토마토가 며칠이면 다 익게되는지 최소일
#모두 1로 만들어져야하는데, -1로 '갇혀있으면' 불가능 -1출력

from collections import deque

m, n, h = map(int, input().split())
box = []
for _ in range(h):
    box.append([list(map(int, input().split())) for _ in range(n)])
queue = deque([])
result = 0

for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                queue.append([i, j, k])

def bfs():
    while queue:
        x, y, z= queue.popleft()
        for dx, dy, dz in [[1,0,0], [-1, 0, 0], [0, 1, 0], [0,-1,0],[0, 0, 1],[0,0,-1]]:
            nx, ny, nz = x+dx, y+dy, z+dz
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and box[nx][ny][nz] == 0:
                box[nx][ny][nz] = box[x][y][z] + 1
                queue.append([nx, ny, nz])

bfs()
for i in box:
    for j in i:
        for k in j:
        #다 찾았는데 토마토를 익히지 못함
            if k == 0:
                print(-1)
                exit()
        #다른 경우 최댓값
        result = max(result, max(j))

print(result-1)