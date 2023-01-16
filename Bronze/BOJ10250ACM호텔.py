#BOJ10250_ACM호텔
import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())

    floor = n % h 
    line = (n//h) + 1
    if floor == 0:
        floor = h
        line -= 1

    print(floor * 100 + line)


