#BOJ23037_5의수난_B2
#https://www.acmicpc.net/problem/23037

import sys
input = sys.stdin.readline

su = list(input().strip())
result = 0
for i in range(len(su)):
    result += int(su[i])**5

print(result)