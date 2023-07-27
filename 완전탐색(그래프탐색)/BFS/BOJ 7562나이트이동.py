#BOJ7562_나이트이동_S1
#https://www.acmicpc.net/problem/7562
#무조건 bfs

#8방향 설정 주의 
# from collections import deque

# def bfs(x, y, a, b):
#     q = deque()
#     q.append([x, y])
#     graph[x][y] = 1
#     while q:
#         x, y = q.popleft()
#         if x == a and y == b:
#             return graph[x][y]-1
#         for dx, dy in [[1,2], [1,-2], [2,1], [2,-1], [-1,2], [-1,-2], [-2,1], [-2, -1]]:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < l and 0 <= ny < l:
#                 if graph[nx][ny] == 0:
#                     q.append([nx, ny])
#                     graph[nx][ny] = graph[x][y] + 1


# tc = int(input())
# while tc:
#     # 한 변의 길이
#     l = int(input())
#     graph = [[0]*l for _ in range(l)]
#     x1, y1 = map(int, input().split())
#     x2, y2 = map(int, input().split())
#     #이동할수가 없으면
#     if x1 == x2 and y1 == y2:
#         print(0)
#         tc -= 1
#         continue
#     ans = bfs(x1, y1, x2, y2)
#     print(ans)
#     tc -= 1


#재풀이
#8방향 설정 주의 
from collections import deque
import sys
input = sys.stdin.readline

def bfs(now_x, now_y):
    # 현재시점
    graph[now_x][now_y] = 1
    q = deque()
    q.append((now_x, now_y))
    while q:
        x, y = q.popleft()
        # 목적지에 도달했다면
        if x == dest_x and y == dest_y:
            # 1부터 시작했으므로 1을 처음 시작점을 없애고 반환
            return graph[dest_x][dest_y]-1
        
        #8방향을 탐색해서
        for dx, dy in [(1,2), (1,-2), (2,1), (2,-1), (-1,2), (-1,-2), (-2,1), (-2, -1)]:
            nx, ny = x + dx, y + dy
            # 범위안에 있고, 지나지 않았으면 1씩 더해준다.
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

# 각 케이스마다
tc = int(input())
for _ in range(tc):
    # 함수 적용해주기
    n = int(input())    
    graph = [[0]*n for _ in range(n)]
    now_x, now_y = map(int, input().split())
    dest_x, dest_y = map(int, input().split())
    print(bfs(now_x, now_y))