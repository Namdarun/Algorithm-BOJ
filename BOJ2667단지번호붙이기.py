#BOJ2667_단지번호붙이기_S1
#https://www.acmicpc.net/problem/2667

#1은 집이 있는 곳, 0은 집이 없는 곳
#연결 = 좌우,위아래 다른 집 있는 경우 - 대각선X
#1은 7개, 2는 8개, 3은 9개 -> 적을수록 1로 시작
#마지막 번호와 그 번호까지의 단지수를 하나씩 출력

#연결점을 찾으면 되므로, dfs로 푼다
#범위를 벗어나면 false, 해당하면 true 재귀로 돌린다. 

n = int(input())
apart = []
for i in range(n):
    apart.append(list(map(int,input())))

result = []
cnt = 0
# dx = [-1,1,0,0] 상하좌우
# dy = [0,0,-1,1]

#dfs 전개 
def dfs(x, y):
    global cnt 
    #범위 벗어날 때 
    if x < 0 or x>=n or y < 0 or y>=n:
        return False
    
    #1을 만나면, apart를 0으로 바꾸고, 
    #범위내로 1을 추가해가면서 재귀를 돌린다 
    if apart[x][y] == 1:
        cnt += 1
        apart[x][y] = 0
        for dx, dy in [[0,1], [1,0], [0,-1], [-1,0]]:
            nx,ny = x+dx, y+dy   
            dfs(nx, ny)
        # for i in range(4):
        #     dfs(x+dx[i],y+dy[i])
        return True
    
for i in range(n):
    for j in range(n):
        if dfs(i,j)==True:
            result.append(cnt)
            #초기화 해줘야함
            cnt = 0

# print(result)
print(len(result))
result.sort()
for i in result:
    print(i)