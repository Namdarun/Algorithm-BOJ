#BOJ16967_배열복원하기_S3
#https://www.acmicpc.net/problem/16967

# 조건에 맞게 하나씩 넣으면 된다.
import sys
input = sys.stdin.readline

h, w, x, y = map(int, input().split())
result = []
arr = []

for _ in range(h+x):
    arr.append(list(map(int, input().split())))

for i in range(h):
    result.append(arr[i][:w])

#두 배열 모두에 포함
for i in range(h):
    for j in range(w):
        if i+x < h and j+y < w:
            result[i+x][j+y] -= result[i][j]

for k in result:
    print(*k)