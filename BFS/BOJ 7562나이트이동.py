#BOJ7562_나이트이동_S1
#https://www.acmicpc.net/problem/7562
#무조건 bfs

#8방향 설정 주의 
from collections import deque

def bfs(x, y, a, b):
    q = deque()
    q.append([x, y])
    arr[x][y] = 1
    while q:
        x, y = q.popleft()
        if x == a and y == b:
            return arr[x][y]-1
        for dx, dy in [[1,2], [1,-2], [2,1], [2,-1], [-1,2], [-1,-2], [-2,1], [-2, -1]]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < l and 0 <= ny < l:
                if arr[nx][ny] == 0:
                    q.append([nx, ny])
                    arr[nx][ny] = arr[x][y] + 1


tc = int(input())
while tc:
    # 한 변의 길이
    l = int(input())
    arr = [[0]*l for _ in range(l)]
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    #이동할수가 없으면
    if x1 == x2 and y1 == y2:
        print(0)
        tc -= 1
        continue
    ans = bfs(x1, y1, x2, y2)
    print(ans)
    tc -= 1