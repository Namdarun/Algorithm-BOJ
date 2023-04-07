#BOJ19532_수학은비대면강의_B2
#https://www.acmicpc.net/problem/19532

#완탐, 흔한 연립방정식 
a, b, c, d, e, f = map(int, input().split())

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (a*i) + (b*j) == c and (d*i) + (e*j) == f:
            print(i, j)

