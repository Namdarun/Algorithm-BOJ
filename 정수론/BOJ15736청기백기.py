#BOJ15736_청기백기_S4
#https://www.acmicpc.net/problem/15736

#완전탐색...?

import sys
input = sys.stdin.readline
N = int(input())
#뒤집혀진 깃발(흰색) 
white = 1

#i번째 선수는 3부터시작
i = 3
idx = 0
while True:
    #첫번째 선수는 전부
    #두번째 선수는 2의 배수
    #i번째 선수는 i의 배수
    for j in range(1, i + 1):
        idx += 1

    #N번째선수를 넘으면 종료
    if idx >= N:
        break

    i += 2
    white += 1

print(white)