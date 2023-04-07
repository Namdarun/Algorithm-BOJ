#BOJ1978_소수판정_B2
#https://www.acmicpc.net/problem/1978

n = int(input())
num = list(map(int, input().split()))
count = 0

for x in num:
    for i in range(2, x+1):
        if x % i == 0:
            if x == i:
                count += 1
            break

print(count)
