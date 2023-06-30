#BOJ2845_파티가끝나고난뒤_B4
#https://www.acmicpc.net/problem/2845

l, p = map(int, input().split())
arr = list(map(int, input().split()))
for i in arr:
    print(i - l * p, end = ' ')