#BOJ2576_홀수_B3
#https://www.acmicpc.net/problem/2576

min = 100
sum = 0
for _ in range(7):
    num = int(input())
    if num % 2 == 1:
        sum += num
        if num < min:
            min = num
if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)