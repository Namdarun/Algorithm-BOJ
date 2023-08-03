#BOJ1292_쉽게푸는문제_B1
#https://www.acmicpc.net/problem/1292

a, b = map(int, input().split())
arr = []
for i in range(1, b+1):
    for j in range(i):
        arr.append(i)

result = sum(arr[a-1:b])
print(result)