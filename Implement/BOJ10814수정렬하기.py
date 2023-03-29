#BOJ10814_수정렬하기_S5
#https://www.acmicpc.net/problem/10814

#람다 떠올리기

import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    #문자열로 받고 a만 int로 치환
    a, b = map(str, input().split())
    arr.append([int(a), b])

#arr[i][0]를 기준으로 정렬 
arr.sort(key=lambda x:x[0])

for i in arr:
    print(*i)
