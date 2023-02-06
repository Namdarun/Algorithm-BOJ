#BOJ1789_수들의 합
#https://www.acmicpc.net/problem/1789
#1부터 시작해서 n까지 더해가다가 n보다 더 커지면 -1이 답

n = int(input())
sum = 0
result = 0

for i in range(1, n+1):
    sum += i
    result += 1
    if sum > n:
        result = result -1
        break

print(result)