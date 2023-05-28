#BOJ10813_공바꾸기_B2
#https://www.acmicpc.net/problem/10813

n, m = map(int, input().split())

bowl = [_ for _ in range(1, n+1)]
for i in range(m):
    a, b = map(int, input().split())
    bowl[a-1], bowl[b-1] = bowl[b-1], bowl[a-1]

for i in range(n):
    print(bowl[i], end=' ')