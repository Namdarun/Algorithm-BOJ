#BOJ2668_숫자고르기_G5
#https://www.acmicpc.net/problem/2668

#두번째 좌표들을 보면서, visited여부 체크 -> false, true 활용
#인덱스에 주의(1부터 시작함)

import sys
input = sys.stdin.readline

def dfs(v, n):
    # 방문체크
    visited[v]=True
    check=graph[v]
    # 방문한 적이 없으면 재귀
    if not visited[check]:
        dfs(check, n)
    # 이미 추가되고 싸이클이 생겼을 때
    # check==n 조건을 붙이지 않으면 전부 마지막노드로 찍힘
    elif visited[check] and check==n:
        result.append(check)
    
n = int(input())
#인덱스에 주의 
graph = [0] + [int(input()) for _ in range(n)]
result = []
#인덱스에 주의, 방문하지 않았으면 재귀
for i in range(1, n+1):
    visited=[False]*(n+1)
    dfs(i, i)

print(len(result))
# 오름차순으로 출력
result.sort()
for i in result:
    print(i)