#BOJ3046_R2_B4
#https://www.acmicpc.net/problem/3046

r, s = map(int, input().split())

res = -1000
for i in range(-1000, 1001):
    if (i+r) // 2 == s and (i+r) % 2 == 0:
        print(i)

