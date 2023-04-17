#BOJ1749_점수따먹기_G4
#https://www.acmicpc.net/problem/1749

#2차원배열의 누적합, 최대가 되는 부분행렬

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
game = []
for i in range(n):
    game.append(list(map(int, input().split())))

hap = [[0 for _ in range(m+1)] for _ in range(n+1)]

#누적합 
for i in range(1, n+1):
    for j in range(1, m+1):
        hap[i][j] = hap[i][j-1] + game[i-1][j-1] + hap[i-1][j] - hap[i-1][j-1]
#최댓값을 갱신해나갈 것
max_hap = int(-10e9)

for x1 in range(1, n+1):
    for y1 in range(1, m+1):
        for x2 in range(x1, n+1):
            for y2 in range(y1, m+1):
                #배웠던 부분
                max_hap = max(max_hap, hap[x2][y2] - hap[x1-1][y2] - hap[x2][y1-1] + hap[x1-1][y1-1])
print(max_hap)