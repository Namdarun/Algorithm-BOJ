#BOJ15681_트리와쿼리_G5
#https://www.acmicpc.net/problem/15681

#언제나 올바른 트리 - 마지막 입력값을 루트로하는 서브트리에 속한 정점의 개수
#DFS로 해보자 

import sys
input = sys.stdin.readline
#dfs 재귀깊이 설정
sys.setrecursionlimit(10**9)

# 재귀설정 -> 서브트리에 있고, 방문한적이 없으면, 
# x => 루트의 번호
def dfs(x):
    visited[x]=1
    for i in tree[x]:
        # 간선이 트리에 속함
        if not visited[i]:
            dfs(i)
            # 방문체크때마다 더해줘야 서브트리가 됨
            visited[x] += visited[i]


#정점의 개수, 루트의 번호, 쿼리의 수
n, r, q = map(int, input().split())
tree = [[] for _ in range(n+1)]
visited = [0]*(n+1)

#트리 입력 
for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(r)

# 쿼리 수만큼 정점을 넣고, 방문노드에 같이 넣어둔 정점의 개수를 출력해준다,
for i in range(q):
    u = int(input())
    print(visited[u])