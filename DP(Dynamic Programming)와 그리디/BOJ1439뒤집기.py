#BOJ1439_뒤집기_S5
#https://www.acmicpc.net/problem/1439

import sys
input = sys.stdin.readline
check = str(input())

check1 = check.split('1')
check2 = check.split('0')

result1 = 0
result2 = 0

for i in check1:
    if '0' in i:
        result1 += 1

for i in check2:
    if '1' in i:
        result2 += 1

print(min(result1, result2))