#BOJ15650_N과M(2)
N, M = map(int, input().split())
li = []

def dfs(e):
    if len(li) == M:
        print(*li)
        return
        
    for i in range(e, N+1):
        if i not in li:
            li.append(i)
            dfs(i+1)
            li.pop()

dfs(1)