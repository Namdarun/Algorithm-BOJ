#BOJ2747_피보나치 수_B2
#https://www.acmicpc.net/problem/2747
n = int(input())
a, b = 0, 1
for i in range(n):
    a, b = b, a+b

print(a)