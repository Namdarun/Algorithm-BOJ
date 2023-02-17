#BOJ 20053_최소, 최대2
#https://www.acmicpc.net/problem/20053

a = int(input())
for i in range(a):
    b = int(input())
    num = list(map(int, input().split()))
    print(min(num), end=' ')
    print(max(num))