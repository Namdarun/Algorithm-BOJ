#BOJ11659_구간합구하기4_S3
#https://www.acmicpc.net/problem/11659

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

hap = [0]

check = 0
for i in arr:  
    check += i 
    hap.append(check)

for j in range(m):
    a, b = map(int, input().split())
    print(hap[b] - hap[a-1])