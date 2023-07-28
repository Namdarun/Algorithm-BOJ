#BOJ11725_트리의부모찾기_S2
#https://www.acmicpc.net/problem/11725

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
# 트리그리기
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(n+1)
q = deque()
# 인덱스
q.append(1)

def bfs():
    while q:
        # c와 연결되어있는데 가보지 않았으면 그 값을 넣음
        c = q.popleft()
        for i in graph[c]:
            if visited[i] == 0:
                visited[i] = c
                q.append(i)

bfs()
# print(visited[2:])
# print(visited)
result = visited[2:]
for i in result:
    print(i)