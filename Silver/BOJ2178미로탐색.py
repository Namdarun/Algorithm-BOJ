#BOJ2178_미로 탐색 
#5105_미로의 거리_BFS와 똑같다.
def bfs(i, j, N, M):                   #그래프 G , 탐색 시작점 V
    visited = [[0]*M for _ in range(N)]             
    queue = []                      #queue 생성
    queue.append((i, j))            #시작점 v를  queue에 추가 - 한쌍으로 들어가야해 
    visited[i][j] = 1              #시작점과 도착점을 포함
    while queue:                    #queue에 추가된 요소가 있으면 (비어있지 않으면)
        i, j = queue.pop(0)         #첫번째 원소 반환
        if i == N-1 and j == M-1:   #끝지점 도착
            return visited[N-1][M-1] 
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]: #델타
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and maze[ni][nj]!=0 and visited[ni][nj]==0: #밖으로 나가는 여부 확인
                queue.append((ni, nj))
                visited[ni][nj] = visited[i][j] +1
        
N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)] 
# sti = -1
# stj = -1
# for i in range(N):
#     for j in range(M):
#         if maze[i][j] == (N, M):
#             sti, stj = i, j
#             break
#     if sti != -1: #찾아서 빠져나옴
#         break
    
print(f'{bfs(0, 0, N, M)}')