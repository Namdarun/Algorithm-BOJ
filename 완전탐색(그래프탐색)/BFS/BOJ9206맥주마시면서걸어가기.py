#BOJ9205_맥주마시면서걸어가기_G5
#https://www.acmicpc.net/problem/9205

#BFS
#한박스 20개, 50m 당 한병씩
#갈 수 있으면 happy, 아니면 sad

import sys 
input = sys.stdin.readline
from collections import deque

# reture print
def bfs():
    q = deque()
    q.append((home_x, home_y))
    #순서대로 구현하면 된다. 
    #방문한적이 없으면 q에 추가
    #맥주가 부족하지 않으면 happy 출력 
    while q:
        a, b = q.popleft()
        if abs(a-rock_x) + abs(b-rock_y) <= 1000:
            print('happy')
            return
        #편의점 확인
        for i in range(n):
            if not visited[i]:
                aa, bb = arr[i]
                if abs(a-aa) + abs(b-bb) <= 1000:
                    visited[i] = 1
                    q.append((aa, bb))
    #맥주가 부족하면(q에 넣어서 bfs처리 해도 탈출) sad 출력
    print('sad')
    return

t = int(input())
for _ in range(t):
    n = int(input())
    home_x, home_y = map(int, input().split())
    arr = []
    # 편의점의 개수 n만큼 좌표 저장
    for _ in range(n):
        store_x, store_y = map(int, input().split())
        arr.append((store_x, store_y))
    rock_x, rock_y = map(int, input().split())
    visited = [0 for _ in range(n+1)] 
    bfs()   

###다른풀이
from collections import deque

def cal_distance(x, y, nx, ny):
    return abs(nx - x) + abs(ny - y)


def bfs():
    if cal_distance(home_x, home_y, rock_x, rock_y) <= 1000:
        visited[n] = True
        return

    que = deque()

    for i in range(len(conveni)):
        temp = cal_distance(home_x, home_y, conveni[i][0], conveni[i][1])
        if temp <= 1000:
            que.append(conveni[i])
            visited[i] = True

    while que:
        cx, cy = que.popleft()
        for i in range(len(conveni)):
            temp = cal_distance(cx, cy, conveni[i][0], conveni[i][1])
            if temp <= 1000 and not visited[i]:
                que.append(conveni[i])
                visited[i] = True

t = int(input())

for _ in range(t):
    n = int(input())
    visited = [False] * (n + 1)
    conveni = []

    home_x, home_y = map(int, input().split())

    for _ in range(n):
        conveni.append([int(a) for a in input().split()])

    rock_x, rock_y = map(int, input().split())
    conveni.append([rock_x, rock_y])

    bfs()

    if visited[n] == True:
        print('happy')
    else:
        print('sad')