#BOJ10448_유레카이론
#https://www.acmicpc.net/problem/10448

import sys
input = sys.stdin.readline

Tru = [i * (i + 1) // 2 for i in range(1, 46)]  # 45번째 삼각수 == 1035
eur = [0] * 1001

for i in Tru:
    for j in Tru:
        for k in Tru:
            num = i + j + k
            if num <= 1000:
                eur[num] = 1 # 세 숫자의 조합으로 만들어지는 수

t = int(input())
for _ in range(t):
    print(eur[int(input())])