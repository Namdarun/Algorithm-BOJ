#BOJ2447_별찍기2447
# https://www.acmicpc.net/problem/2447
#재귀 및 분할정복 문제 

import sys
input = sys.stdin.readline
#최대 깊이 재귀 
sys.setrecursionlimit(10**6)

def pick_star(n):
    #n이 1일때 별찍기 
    if n == 1:
        return '*'

    #재귀 -> 3으로 나눌때마다 별찍기
    star = pick_star(n//3)
    R = []
    for i in star:
        R.append(i*3)
    for j in star:
        R.append(j+' '*(n//3)+j)
        # R.append(j*3) -> 전부 찍힘
        # R.append(j+' '+j) -> 5번 대신 6번이 사라짐
        # R.append(j+' '*(n)+j) -> 가운데는 비는데 n만큼 밀려남
    for k in star:
        R.append(k*3)
    return R

N = int(input())
arr = pick_star(N)
for i in arr:
    print(i)