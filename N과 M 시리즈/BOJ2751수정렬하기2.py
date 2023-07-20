#BOJ2751_수정렬하기2_S5
#https://www.acmicpc.net/problem/2751

import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

for i in sorted(arr):
    print(i)