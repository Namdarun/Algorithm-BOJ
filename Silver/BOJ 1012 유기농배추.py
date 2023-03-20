#BOJ1012_유기농배추_S2
#https://www.acmicpc.net/problem/1012

# 입력값을 어떻게 받을 수 있을까?
# 대각선은 보지 않는다
# 인접했다면 N이든 M이든 1의 차이만 난다 
# BFS를 하고 2 이상 차이가 나면 count 끝
# visited가 종료되면 종료 후 count 도출
# 혹은
# 방문한 셀 영역을 제외하고 dfs가 동작할때마다 카운트

import sys
input = sys.stdin.readline

#테스트케이스의 개수
T = int(input()) 

def BFS(x,y):           
    queue = [(x,y)]
    #방문처리
    visited[x][y] = 0 
    

    while queue:
        x,y = queue.pop(0)

        #4방향
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy

            #범위를 넘어서면 그 다음
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

            #1이면 queue에 추가하고 0으로 바꿔줌
            if visited[nx][ny] == 1 :
                queue.append((nx,ny))
                visited[nx][ny] = 0

# 행렬만들기
for i in range(T):
    M, N, K = map(int,input().split())
    visited = [[0]*(N) for _ in range(M)]
    #인접한 노드가 없으면 세는 카운트
    cnt = 0

    #모두 1로 처리
    for j in range(K):
        x,y = map(int, input().split())
        visited[x][y] = 1

    #visited를 돌면서 1이면 bfs실행(0으로 바꿔주고) 카운트+1
    for a in range(M):
        for b in range(N):
            if visited[a][b] == 1:
                BFS(a,b)
                cnt += 1

    print(cnt)