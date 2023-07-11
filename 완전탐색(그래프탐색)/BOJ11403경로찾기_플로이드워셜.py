#BOJ11403_경로찾기_S1
#https://www.acmicpc.net/problem/11403

# 플로이드 워셜 알고리즘이 있다고 한다.
# 플로이드-와샬 알고리즘을 이용한 풀이
# 모든 최단 경로를 구하는 알고리즘 

import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
 
# 경로가 있는지 없는지 탐색 
# 중간노드 i 
for i in range(n):
    # 각 노드별 모든 거리, i를 중간노드로 삼을때와 아닐 때 값 비교 
    for j in range(n):
        for k in range(n):
            if graph[j][i] and graph[i][k]:
                graph[j][k] = 1
                

# print(graph)
for g in graph:
    print(*g)