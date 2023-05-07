#BOJ2805_나무자르기_S2
#https://www.acmicpc.net/problem/2805

#함수로 만들어서 풀어보자

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

s = 1
e = max(tree)

while s <= e:
    mid = (s+e) // 2
    cnt = 0

    #나무 높이가 절단기 높이보다 크면 자르기
    for i in tree:
        if i > mid:
            cnt += i-mid
    
    #목표값 이상이면 시작점
    if cnt >=m : 
        s = mid + 1

    #목표값 이하면 끝점
    else:
        e = mid - 1

print(e)
