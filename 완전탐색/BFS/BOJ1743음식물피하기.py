#BOJ1743_음식물피하기_S1
#https://www.acmicpc.net/problem/1743

# 행렬을 만들고 bfs로 완전탐색하면 되겠다.

from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1

# 4방향탐색
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j):
    q = deque()
    q.append([i, j])
    visited[i][j] = True
    cnt = 1

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 범위설정
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 1:
                visited[nx][ny] = True
                q.append([nx, ny])
                cnt += 1

    return cnt

result = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j] == 1:
            # 방문하지 않았고 1이면 갱신
            result = max(result, bfs(i, j))
print(result)