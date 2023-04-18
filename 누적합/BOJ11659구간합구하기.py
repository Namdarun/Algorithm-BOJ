#BOJ11659_구간합구하기4_S3
#https://www.acmicpc.net/problem/11659

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

hap = [0]

#누적합 배열에 저장
check = 0
for i in arr:  
    check += i 
    hap.append(check)

#인덱스로 인해 a-1을 빼준다
for j in range(m):
    a, b = map(int, input().split())
    print(hap[b] - hap[a-1])