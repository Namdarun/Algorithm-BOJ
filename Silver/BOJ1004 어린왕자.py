#BOJ1004_어린왕자_S3
#https://www.acmicpc.net/problem/1004
#단순구현 
#출발점과 도착점이 주어지는 원 안에 속하는지? 
#둘 중 하나만 속할 때 +1

t = int(input())
for i in range(t):
    #답 = t에 유의
    count = 0
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    for j in range(n):
        px, py, pr = map(int, input().split())
        a1 = (((x1 - px) **2) + ((y1 - py) **2)) **0.5
        a2 = (((x2 - px) **2) + ((y2 - py) **2)) **0.5
        if (a1 < pr and a2 > pr) or (a1 > pr and a2 < pr):
            count += 1
    print(count)