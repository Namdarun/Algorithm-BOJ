#BOJ10810_공넣기_B3
#https://www.acmicpc.net/submit/10810

n, m = map(int, input().split())
bowl = [0 for _ in range(n)]

for _ in range(m):
    i, j, k = map(int, input().split())
    for c in range(i, j+1):
        bowl[c-1] = k
        
for i in range(n):
    print(bowl[i], end=' ')