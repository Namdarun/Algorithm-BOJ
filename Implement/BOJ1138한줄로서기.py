#BOJ1138_한줄로서기_S2
#https://www.acmicpc.net/problem/1138

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
check = [0]*n

for i in range(n):
    cnt = 0
    for j in range(n):
        # 조건이 맞을 땐 check에 더하기 
        if cnt == arr[i] and check[j] == 0:
            check[j] = i+1
            break
        # 아무도 없을 땐 내 왼쪽에 키큰 사람을 카운트
        elif check[j] == 0:
            cnt += 1

print(*check)