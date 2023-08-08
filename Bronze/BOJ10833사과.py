#BOJ10833_사과_B3
#https://www.acmicpc.net/problem/10833

import sys
input = sys.stdin.readline

result = 0
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    result += b%a

print(result)