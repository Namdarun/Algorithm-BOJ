#BOJ10866_덱
##https://www.acmicpc.net/problem/11727
#단순 구현 노가다...
#대놓고 depue 구현하라 했다. deque 메서드 복습하기 좋은 문제 

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
dq = deque()
for i in range(n):
    dek = list(input().split())

    if dek[0]=='push_front':
        dq.appendleft(dek[1])

    elif dek[0]=='push_back':
        dq.append(dek[1])

    elif dek[0]=='pop_front':
        if dq:
            x=dq.popleft()
            print(x)
        else:
            print(-1)

    elif dek[0]=='pop_back':
        if dq:
            x=dq.pop()
            print(x)
        else:
            print(-1)

    elif dek[0]=='size':
        print(len(dq))

    elif dek[0]=='empty':
        if len(dq)==0:
            print(1)
        else:
            print(0)

    elif dek[0]=='front':
        if dq:
            print(dq[0])
        else:
            print(-1)

    elif dek[0]=='back':
        if dq:
            print(dq[-1])
        else:
            print(-1)
    