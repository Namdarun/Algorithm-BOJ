#BOJ5568_카드놓기_S4
#https://www.acmicpc.net/problem/5568

import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
k = int(input())
arr = []
result = set()

for i in range(n):
    arr.append(int(input()))

for j in permutations(arr, k):
    result.add(''.join((list(map(str, j)))))
    # result.add(''.join(j))

# print(result)
print(len(result))