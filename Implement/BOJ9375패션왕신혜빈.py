#BOJ9375_패션왕신혜빈_S2
#https://www.acmicpc.net/problem/9375

import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    dict = {}
    for j in range(n):
        wear_n, wear_t = input().split()

        if wear_t not in dict.keys():
            dict[wear_t] = 1
        else:
            dict[wear_t] += 1

    cnt = 1
    for i in dict:
        cnt *= (dict[i]+1)
    print(cnt-1)