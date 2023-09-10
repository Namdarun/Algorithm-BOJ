#BOJ2693_N번째큰수_B1
#https://www.acmicpc.net/problem/2693

n = int(input())
for i in range(n):
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[-3])