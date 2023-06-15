#BOJ2003_수들의 합2_S4
#https://www.acmicpc.net/problem/2003

import sys
input = sys.stdin.readline

def check(n, m, arr):
    s, e = 0, 0
    checking = arr[0]
    result = 0

    while True:
        if checking < m:
            e+= 1
            if e >= n:
                break
            checking += arr[e]

        elif  checking == m:
            result += 1
            checking -= arr[s]
            s += 1
        else:
            checking -= arr[s]
            s += 1

    return result 

n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(check(n,m,arr))