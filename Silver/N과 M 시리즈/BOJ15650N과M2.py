#BOJ15650_N과M2
#백트래킹
#unindent does not match any outer indentation level 
#들여쓰기 에러 뜨면 그냥 지우고 다시 해야하나요?
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