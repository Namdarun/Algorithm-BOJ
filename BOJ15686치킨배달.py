#BOJ15686_치킨배달_G5
#https://www.acmicpc.net/problem/15686

import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
#각 노드를 명확히 받아야 하므로, 리스트로 추가
city = list(list(map(int, input().split())) for _ in range(n))
result = 999999
house = []      # 집의 좌표
chick = []      # 치킨집의 좌표

#1이면 집, 2면 치킨집
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chick.append([i, j])

#M개의 치킨집을 선택하는 경우의 수 
for chi in combinations(chick, m):  # m개의 치킨집 선택
    temp = 0            # 도시의 치킨 거리
    for h in house: 
        len = 1000   # 각 집마다 치킨 거리
        for j in range(m):
            #백트래킹 
            len = min(len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        temp += len
    #최솟값 찾기
    result = min(result, temp)

print(result)