#BOJ1389_케빈베이컨의6단계법칙_S1
#https://www.acmicpc.net/problem/1389

#BFS, 플루이드 워셜 
#노드를 연결하고 거리를 최솟값으로 갱신해나가면 된다. 

from collections import deque
import sys
input = sys.stdin.readline

#bfs
def bfs(node):
    q = deque()
    q.append(node)
    visited[node] = 1
    while q:
        s = q.popleft()
        for i in range(n+1):
            if graph[s][i] and visited[i] == 0: 
                visited[i] = visited[s]+1
                q.append(i)

n, m = map(int, input().split())
# visited = [0]*(n+1)

#노드리스트
graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

min_num = 100000000
index = 0
for i in range(1, n+1):
    visited = [0]*(n+1)
    bfs(i)
    if min_num > sum(visited):
        min_num = sum(visited)
        index = i 

print(index)
