#BOJ13423_Three dots_S2
#https://www.acmicpc.net/problem/13423
#이분탐색 
#주어진 값 두개를 더해 나눈 값이 set된 입력값 안에 있는지 확인
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    cnt = 0
    set_x = set(x)
    for i in range(n):
        for j in range(i+1,n):
            if (x[i]+x[j])/2 in set_x:
                cnt += 1
            else:
                continue
    print(cnt)
    