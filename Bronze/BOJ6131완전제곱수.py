#BOJ6131_완전제곱수_B3
#https://www.acmicpc.net/problem/6131

n = int(input())

cnt = 0

for i in range(1, 501):
    for j in range(1, 501):
        if i**2  == j**2 + n :
            cnt += 1


print(cnt)
