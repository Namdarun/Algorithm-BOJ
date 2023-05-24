#BOJ2702_초6수학_B2
#https://www.acmicpc.net/problem/2702

#유클리드 호제법을 이용해 풀면 된다. 

import sys
input = sys.stdin.readline

def gcd(x, y):
    while y:
        if x>y:
            x, y = y, x
        y %= x
    return x

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    gcd_num = gcd(a, b)
    print(a*b // gcd_num, gcd_num)