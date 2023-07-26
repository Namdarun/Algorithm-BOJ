#BOJ2178_미로탐색_S1
#https://www.acmicpc.net/problem/2178

#전형적인 bfs 문제
#1은 이동할 수 있는칸, 0은 이동할 수 없는 칸 

from collections import deque
def bfs():
    q = deque()
    q.append((0,0))
    graph[0][0] = 1

    while q:
        x, y = q.popleft()
        #4방향탐색
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            #1을 string처리해야함에 유의하자
            #범위안에 있고 1을 만나면 이동할 수 있다.
            if 0<= nx < n and 0<= ny <m and graph[nx][ny] =='1':
                graph[nx][ny] = graph[x][y]+1
                q.append((nx, ny))

#입력
n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
bfs()
# 다 돌았을 때 값
print(graph[n-1][m-1])