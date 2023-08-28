#BOJ1926_그림_S1
#https://www.acmicpc.net/problem/1926

#BFS
from collections import deque

def bfs(x,y):
    check = 1
    arr[x][y] = 0
    q = deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()
        #4방향탐색
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            #1을 string처리해야함에 유의하자
            #범위안에 있고 1을 만나면 이동할 수 있다.
            if 0<= nx < n and 0<= ny <m and arr[nx][ny] ==1:
                q.append((nx, ny))
                arr[nx][ny] = 0
                check += 1
    return check

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
result = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            cnt += 1
            result = max(bfs(i,j), result)

print(cnt)
print(result)