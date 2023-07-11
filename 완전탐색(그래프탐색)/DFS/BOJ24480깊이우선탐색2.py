#BOJ24480_깊이우선탐색2_S2
#https://www.acmicpc.net/problem/24480

import sys
input = sys.stdin.readline
#재귀 깊이 설정
sys.setrecursionlimit(10**6)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
result = [0]*(n+1)
cnt = 1

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

#재귀 설정, 내림차순에 주의
def dfs(n):
    global cnt 
    visited[n] = 1
    result[n] = cnt 
    graph[n].sort(reverse=True)
    for i in graph[n]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

dfs(r)

for i in result[1:]:
    print(i)

