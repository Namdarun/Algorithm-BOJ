#BOJ11724_연결요소의개수_S2
#https://www.acmicpc.net/problem/11724

#어떻게 풀지 몰라서 다시 공부함 ㅠ

import sys
sys.setrecursionlimit(10**6)

#입력 
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
group = [-1] * (n+1)

# 그룹 수
count = 1
for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

# node와 연결된 노드 탐색
def dfs(node):
    for neighbor in graph[node]:
        if (group[neighbor] == -1):
            group[neighbor] = group[node]
            dfs(neighbor)
for i in range(1, n+1):
    if (group[i] == -1):
        group[i] = count
        count += 1
        dfs(i)

print(count-1)