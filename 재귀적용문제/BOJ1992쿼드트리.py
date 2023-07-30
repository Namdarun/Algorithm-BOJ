#BOJ1992_쿼드트리_S1
#https://www.acmicpc.net/problem/1992

#분할정복이라고 한다...
#4방향으로 DFS 적용해보기

import sys
input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    graph.append(list(input()))

def dfs(x,y,n):
    if n == 1:
        result.append(graph[x][y])
        return

    check = graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if graph[i][j]!= check:
                #4분할탐색 시작, 기준숫자와 다르면 n을 2로 나눈다.
                n //= 2
                result.append('(')
                dfs(x,y,n)
                dfs(x,y+n,n)
                dfs(x+n,y,n)
                dfs(x+n,y+n,n)
                result.append(')')
                return
    
    #사각형이 모두 한 숫자로 이뤄져있음
    result.append(check)

result = []
dfs(0,0,n)

print(*result,sep='')