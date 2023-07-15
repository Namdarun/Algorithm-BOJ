#BOJ2606_바이러스_S3
#https://www.acmicpc.net/problem/2606

#DFS의 틀 

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
cnt = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

#DFS 재귀탐색 구현
def dfs(n):
    global cnt 
    visited[n] = 1
    for i in graph[n]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

dfs(1)
print(cnt)