#BOJ10811_바구니바꾸기_B2
#https://www.acmicpc.net/problem/10811

n, m = map(int, input().split())
bowl = [_ for _ in range(1, n+1)]
for i in range(m):
    a, b = map(int, input().split())
    reverse_bowl = bowl[a-1:b]
    reverse_bowl.reverse()
    bowl[a-1:b] = reverse_bowl

for i in range(n):
    print(bowl[i], end=' ')