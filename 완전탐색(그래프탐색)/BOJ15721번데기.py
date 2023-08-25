#BOJ15721_번데기_S5
#https://www.acmicpc.net/problem/15721

#구하고자 하는 사람이 원탁에 몇번째? => index로 찾기 

import sys
input = sys.stdin.readline

a = int(input())
#구하고자 하는 t번쨰 사람
t = int(input())
#뻔이면 0, 데기면 1 
check = int(input())

arr = []
#뻔과 데기의 위치
bun = degi = 1
n = 0 
while True:
    prev_n = bun
    n += 1
    for _ in range(2):
        arr.append((bun, 0))
        bun += 1
        arr.append((degi, 1))
        degi += 1
    # 늘려나가야함
    for _ in range(n+1):
        arr.append((bun, 0))
        bun += 1
    for _ in range(n+1):
        arr.append((degi, 1))
        degi += 1
    if prev_n < t <= bun:
        # arr.append((arr.index()))
        print(arr.index((t, check))%a)
        # print(arr)
        break 

# print(arr)

