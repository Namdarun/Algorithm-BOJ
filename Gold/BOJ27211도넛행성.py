#BOJ27211_도넛행성_G5
#https://www.acmicpc.net/problem/27211


n, m = map(int, input().split())
donut = [list(map(int, input().split())) for _ in range(n)]

def bfs(a, b):
    stack = []
    stack.append((a, b))
    while stack:
        # x, y = stack.pop()
        x, y = stack.pop()
        # 4방향 탐색 
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = x+di, y+dj
            # 옮긴 지역이 n과 같을 땐 초기화
            # 작아지면 그 뒤 노드에 안착
            if ni == n:
                ni = 0
            elif ni < 0:
                ni = n - 1
            elif nj == m:
                nj = 0
            elif nj < 0:
                nj = m - 1
            # 방문한 적이 없으면 1로 만들어주고 스택에 추가
            if not donut[ni][nj]:
                donut[ni][nj] = 1
                stack.append((ni, nj))
            # print(stack)

count = 0
for i in range(n):
    for j in range(m):
        if not donut[i][j]:
            bfs(i, j)
            count += 1
            
print(count)
