#BOJ14503_로봇청소기_G5
#https://www.acmicpc.net/problem/14503

# 구현
# 현재칸 - 청소되지 않았으면 청소
# 주변 4칸이 다 청소됐을때, 후진할 수 있으면 후진하고 1번
# 벽이면 break
# 주변 4칸 중 청소되지 않는 칸 존재할 때 - 반시계(왼쪽) 90도 회전
# 앞칸이 청소안되있으면 한 칸 전진 -> 1번으로 이동 
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [[0] * m for _ in range(n)]
r, c, d = map(int, input().split())
arr = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    arr.append(list(map(int, input().split())))

# 시작점 
visited[r][c] = 1
# 청소하는 칸의 개수
count = 1

# 끝날때까지 하니까 while문
while True:
    #시작, 주변칸에 청소가능한지 여부 확인
    flag = 0 
    for _ in range(4):
        nx = r + dx[(d+3)%4]
        ny = c + dy[(d+3)%4]

        # 왼쪽
        d = (d+3)%4

        # 범위내, 청소가능 -> 방문처리, 카운트, 현재위치, 청소체크
        if 0<= nx<n and 0<=ny<m and arr[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                count += 1
                r = nx
                c = ny
                count = 1
                break

    # 네 방향 봤는데, 청소할 수가 없다. 해치웠나?
    # 벽이면 break, 아니면 후진
    if flag == 0:
        if arr[r-dx[d]][c-dy[d]] == 1:
            print(count)
            break
        else:
            r, c = r-dx[d], c-dy[d]