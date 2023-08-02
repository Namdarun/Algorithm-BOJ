#BOJ2530_인공지능시계_B4
#https://www.acmicpc.net/problem/2530

h, m, s = map(int, input().split())
t = int(input())

s+= t
m+= s//60
h+= m//60
print(h%24, m%60, s%60)