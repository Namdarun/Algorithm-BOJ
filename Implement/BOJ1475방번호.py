#BOJ1475_방번호_S5
#https://www.acmicpc.net/problem/1475

#단순구현 

import sys
input = sys.stdin.readline

n = int(input())
card = [0] * 10
#간편하게 str 처리
for i in str(n):
    if i == "9" or i == "6":
        if card[6] == card[9]:
            card[6] += 1
        else:
            card[9] += 1
    else:
        card[int(i)] += 1

print(max(card))