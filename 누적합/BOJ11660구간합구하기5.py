#BOJ11660_구간합구하기5_S1
#https://www.acmicpc.net/problem/11660

#점수따먹기와 똑같은 방식으로 불편된다.
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
gan = []
for i in range(n):
    gan.append(list(map(int, input().split())))

go = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        go[i][j] = go[i][j-1] + go[i-1][j] - go[i-1][j-1] + gan[i-1][j-1]


for k in range(m):
    #변수 위치설정에 주의해라
    x1, y1, x2, y2 = map(int, input().split())
    result = go[x2][y2] - go[x2][y1-1] - go[x1-1][y2] + go[x1-1][y1-1] 
    #한줄씩 출력
    print(result)