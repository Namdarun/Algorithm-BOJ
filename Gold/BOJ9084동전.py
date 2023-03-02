#BOJ9084_동전_G5
#https://www.acmicpc.net/problem/9084

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    #n가지 동전의 각 금액들
    price = list(map(int, input().split()))
    #만들어야하는 금액 m
    m = int(input())

    #주어진 금액(m)까지 도달하는 과정의 가짓수 구하기

    #dp 처리 / 동전 한개일때 1
    dp=[0]*(m+1)
    dp[0] = 1

    # 만드는 방법이 생기면, 이전 경우의 수에 지금 동전으로 만들 수 있는 경우의 수를 합침
    for i in price:
        for j in range(m+1):
            if j >= i:
                dp[j] += dp[j-i]

    print(dp[m])

