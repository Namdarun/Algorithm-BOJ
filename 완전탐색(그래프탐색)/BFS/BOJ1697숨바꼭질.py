#BOJ1697_숨바꼭질_S1
#https://www.acmicpc.net/problem/1697

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
check = [0]*100001

q = deque()
q.append(n)
while q:
    j = q.popleft()
    # 한 사이클마다 같은 값을 찾음
    if j == m:
        print(check[m])
        break
    
    #방문 안했고 범위 내 
    for i in (j-1, j+1, j*2):
        if 0<=i<=100000 and check[i] == 0:
            check[i] = check[j] + 1
            q.append(i)