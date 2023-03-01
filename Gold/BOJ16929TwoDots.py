#BOJ16929_TwoDots_G4
#https://www.acmicpc.net/problem/16929

#고민고민!!
def dfs(x, y, cnt):
    global tx, ty, flag
    if flag: 
        return
    for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
        ni, nj = x+di, y+dj
        #범위 벗어나지 않고, 색깔이 같을 때만 하도록
        if ni < 0 or nj < 0 or ni >= N or nj >= M or a[ni][nj] != a[tx][ty]: 
            continue
        if not visit[ni][nj]:
            visit[ni][nj] = True # 방문처리 했다가
            dfs(ni, nj, cnt + 1)
            visit[ni][nj] = False # 안한 걸로
        else:
            # 4번 이상이고 위치가 같을 때 -> 사이클
            if cnt >= 4 and tx == ni and ty == nj: 
                flag = True
                return

N, M = map(int, input().split())
a = [list(input()) for _ in range(N)]
visit = [[False] * M for _ in range(N)]
flag = False

for i in range(N):
    for j in range(M):
        if not visit[i][j]:
            tx, ty = i, j
            visit[i][j] = True
            dfs(i, j, 1)
        # 4번 이상이고 위치가 같을때 
        if flag:
            print("Yes")
            exit(0)

print("No")