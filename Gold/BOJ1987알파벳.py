#BOJ1987_알파벳_G4
#https://www.acmicpc.net/problem/1987

#상하좌우 4방향 탐색
#다음 칸이 나를 포함한, 지나온 칸과 중복되면 안됨
#DFS로 풀어보았다.

import sys
input = sys.stdin.readline

R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]
ans = 0
#중복을 제거한 visited 리스트
visited = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y, answer):
    global ans
    ans = max(ans, answer)

    #4방향 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # index 벗어나지 않는지, 중복여부 체크
        if 0 <= nx < R and 0 <= ny < C and not arr[nx][ny] in visited:
            #set 메서드(add, remove)
            visited.add(arr[nx][ny])
            DFS(nx, ny, answer+1)
            visited.remove(arr[nx][ny])

visited.add(arr[0][0])
DFS(0, 0, 1)
print(ans)

