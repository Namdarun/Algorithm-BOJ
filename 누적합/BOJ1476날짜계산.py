#BOJ1476_날짜계산_S5
#https://www.acmicpc.net/problem/1476

#브루트포스 알고리즘
#연도에서 주어진 esm을 각각 뺏을 때 나머지가 모두 0일때 연도가 나옴. 계산문제 
e, s, m = map(int, input().split())
check = 1
while True:
    if (check-e)%15 == 0 and (check-s)%28 == 0 and (check-m)%19 == 0:
        break
    check += 1

print(check)