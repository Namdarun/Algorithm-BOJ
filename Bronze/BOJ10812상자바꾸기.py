#BOJ10812_상자바꾸기_B2
#https://www.acmicpc.net/problem/10812

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]

for _ in range(m):
    i, j, k = map(int, input().split())
    arr = arr[:i-1]+arr[k-1:j] + arr[i-1:k-1] + arr[j:]

print(*arr)