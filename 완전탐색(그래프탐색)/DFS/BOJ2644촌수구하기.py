#BOJ2644_촌수계산_S2
#https://www.acmicpc.net/problem/2644

import sys
input = sys.stdin.readline
#재귀 깊이 설정
sys.setrecursionlimit(10**6)

def dfs(v):
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = visited[v] + 1
            dfs(i)

n = int(input())
n_a, n_b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
# visited가 곧 촌수계산결과
visited = [0]*(n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 재귀 시작점
dfs(n_a)
if visited[n_b] > 0:
    print(visited[n_b])
else:
    print(-1)

