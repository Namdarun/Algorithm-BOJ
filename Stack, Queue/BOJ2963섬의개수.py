#BOJ2963_섬의개수_S2
#https://www.acmicpc.net/problem/4963

#BFS를 통한 8방향 탐색 
from collections import deque

#미로_4875
def bfs(i, j):                             
    queue = []                      #queue 생성
    queue.append([i, j])            #시작점 v를  queue에 추가 - 한쌍으로 들어가야해 
    maze[i][j] = 0
    while queue:                    #queue에 추가된 요소가 있으면 (비어있지 않으면)
        i, j = queue.pop(0)            #첫번째 원소 반환
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0], [-1,-1], [-1,1], [1,1], [1,-1]]: #8방향 델타
            ni, nj = i+di, j+dj
            if 0<=ni<h and 0<=nj<w and maze[ni][nj]==1:#밖으로 나가는 여부 확인
                queue.append([ni, nj])
                maze[ni][nj] = 0
 


while True:
    w, h = map(int, input().split())
    # 0,0 을 만나면 종료
    if w == h == 0:
        break
    else:
        maze = [list(map(int, input().split())) for _ in range(h)]
        som = 0
        # 2차원배열 h -> w 
        for i in range(h):
            for j in range(w):
                if maze[i][j] == 1:
                    # 재귀 돌린다 
                    bfs(i, j)
                    som = som + 1
        print(som)