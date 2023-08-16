#BOJ5014_스타트링크_S1
#https://www.acmicpc.net/problem/5014

#F = 건물 총 층수 
#S = 현재 있는 층 
#G = 스타트링크 있는 층 
#U = up
#D = down

import sys
input = sys.stdin.readline
from collections import deque

f, s, g, u, d = map(int, input().split())
check = [0]*(f+1)

#BFS
def bfs():
    q = deque()
    q.append(s)
    check[s] = 1

    while q:
        j = q.popleft()

        if j == g:
            return check[j]-1
        
        #범위에 주의하자. 특히 i for문이 어려움
        else:
            for i in (j+u, j-d):
                if (0<i<=f) and check[i] == 0:
                    check[i] = check[j] + 1
                    q.append(i)

    return "use the stairs"

print(bfs())