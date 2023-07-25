#BOJ4485_녹색옷입은애가젤다지?_G4
#https://www.acmicpc.net/problem/4485

#전형적인 다익스트라문제
#배운대로 heapq로 구현해보자 -> 2차원배열이기에 x,y값을 추가해줘야 한다.

import heapq
import sys
input = sys.stdin.readline 
INF = int(1e9)
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
def dijkstra():
    q = []
    #최소힙
    heapq.heappush(q, (graph[0][0], 0, 0))
    #2차원배열로 distance 만들기
    dist[0][0] = 0

    while q:
        cost, x, y = heapq.heappop(q)

        if x == n-1 and y == n-1:
            # 진짜 오랜만에 해보는 fstring처리
            print(f'Problem {cnt}: {dist[x][y]}')
            break

        #4방향탐색
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy

        #4방향탐색
        # for i in range(4):
        #     nx = x + dx[i]
        #     ny = y + dy[i]
            # 범위 안이라면 새로운값을 추가해주고, 
            if 0<= nx < n and 0<= ny < n:
                ncost = cost + graph[nx][ny]

                #최솟값을 갱신해주고, heapq에 넣어준다.
                if ncost < dist[nx][ny]:
                    dist[nx][ny] = ncost
                    heapq.heappush(q, (ncost, nx,ny))

cnt = 1
while True:
    n = int(input())
    # 0인 입력이 주어지면 끝
    if n == 0:
        break

    #입력값, 출력값을위한 변수 cnt 
    graph= [list(map(int, input().split())) for _ in range(n)]
    #distance 또한 2차원배열로
    dist = [[INF]*n for _ in range(n)]
    dijkstra()
    cnt += 1