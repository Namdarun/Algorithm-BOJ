#BOJ1934_최소공배수_B1
#https://www.acmicpc.net/problem/1934
#유클리드 호제법 검색함 

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    aa = a
    bb = b
    c = 1
    while c != 0:
        c=aa%bb
        aa = bb
        bb = c
    #두 수의 곱을 최대공약수로 나누면 최소공배수
    print(int(a*b/aa))