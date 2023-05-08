#BOJ2121_같이놀기_S3
#https://www.acmicpc.net/problem/2121

import sys
input = sys.stdin.readline

def binary(v, p):
    s = 0
    e = len(v)-1
    
    while s <= e:
        mid = (s+e) // 2
        if v[mid] == p:
            return True
        elif v[mid] > p:
            e = mid-1
        else:
            s = mid+1
    return False

N = int(input())
a, b = map(int, sys.stdin.readline().split())
v = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    v.append((x, y))

v.sort()

#범위 안에 존재하는지 이분탐색을 해가면서 가능하만 카운트해준다.
cnt = 0
for i in range(N):
    x, y = v[i]
    p1 = (x+a, y)
    p2 = (x, y+b)
    p3 = (x+a, y+b)
    if binary(v, p1) and binary(v, p2) and binary(v, p3):
        cnt += 1

print(cnt)