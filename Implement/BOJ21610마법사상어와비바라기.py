#BOJ21610_마법사상어와 비바라기_G5
#https://www.acmicpc.net/problem/21610

def get_exist():
    global exist
    exist = [[False] * n for _ in range(n)]
    for x, y in cloud:
        exist[x][y] = True
def get_cloud():
    global cloud
    cloud = []
    for i in range(n):
        for j in range(n):
            if exist[i][j]:
                cloud.append([i, j])
def move(d, s):
    for i in range(len(cloud)):
        x = cloud[i][0]
        y = cloud[i][1]
        for _ in range(s):
            x = (x + dx[d] + n) % n
            y = (y + dy[d] + n) % n
        cloud[i][0] = x
        cloud[i][1] = y
    get_exist()
def rain():
    for i in range(n):
        for j in range(n):
            if exist[i][j]:
                arr[i][j] += 1
    # for x, y in cloud:
    #     arr[x][y] += 1
def w_copy():
    # arr2 = [[0] * n for _ in range(n)]
    # for i in range(n):
    #     for j in range(n):
    #         arr2[i][j] = arr[i][j]
    arr2 = [i[:] for i in arr]
    for i in range(n):
        for j in range(n):
            if not exist[i][j]:
                continue
            for k in range(4):
                nx = i + dx2[k]
                ny = j + dy2[k]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if arr2[nx][ny] != 0:
                    arr[i][j] += 1
def make_cloud():
    global cloud
    cloud = []
    for i in range(n):
        for j in range(n):
            if not exist[i][j] and arr[i][j] >= 2:
                arr[i][j] -= 2
                cloud.append([i, j])
    get_exist()
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
exist = [[False] * n for _ in range(n)]
cloud = []
exist[n - 2][0] = True
exist[n - 2][1] = True
exist[n - 1][0] = True
exist[n - 1][1] = True
get_cloud()
#  ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dx2 = [-1, -1, 1, 1]
dy2 = [-1, 1, -1, 1]
for _ in range(m):
    d, s = map(int, input().split())
    move(d, s)
    rain()
    w_copy()
    make_cloud()
print(sum([sum(i) for i in arr]))