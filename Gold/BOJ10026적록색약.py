#BOJ10026_적록색약_G5
#https://www.acmicpc.net/problem/10026

#아직 방문하지 않았고, 같은 색인 경우 방문표시 후 큐에 넣음 
#적록색약 : R=G로 통일 후 BFS과정 반복
from collections import deque
def bfs(x,y):
    queue.append((x,y))

    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in [[0,1], [1,0], [0,-1], [-1,0]]:
            nx,ny = x+dx, y+dy        
            # 인덱스 범위 내, 같은 색, 방문x
            if 0<=nx<N and 0<=ny<N and a[nx][ny] == a[x][y] and not visited[nx][ny]:
                # 방문체크 후 큐에 넣음
                visited[nx][ny] = 1  
                queue.append((nx,ny))

#입력값
N = int(input())
a = [list(input()) for _ in range(N)]
queue = deque()

# 적록색약 여부에 따라 계산을 다르게 둔다
#방문여부 체크
visited = [[0] * N for _ in range(N)]
# 적록색약 아닌 경우(일반적인 계산방법)
cnt1 = 0
for i in range(N):
    for j in range(N):
            # 아직 방문 안한 경우만 체킹
        if not visited[i][j]:  
            bfs(i,j)
            cnt1 += 1

# 적록색약인 경우 -> G를 R로 바꾸고 계산
for i in range(N):
    for j in range(N):
        if a[i][j] == 'G':
            a[i][j] = 'R'

#방문여부 체크(초기화)
visited = [[0] * N for _ in range(N)]
cnt2 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i,j)
            cnt2 += 1

print(cnt1, cnt2)