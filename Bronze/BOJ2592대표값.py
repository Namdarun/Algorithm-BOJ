#BOJ2592_대표값_B2
#https://www.acmicpc.net/problem/2592

arr = []
for _ in range(10):
    arr.append(int(input()))

print(sum(arr) // 10)
print(max(arr, key=arr.count))