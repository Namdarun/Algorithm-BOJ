#BOJ1240_노드사이의 거리_G5
#https://www.acmicpc.net/problem/1240
import sys
input = sys.stdin.readline

#입력
N, M = map(int, input().split())
#트리 
Tree = [[] for _ in range(N+1)]
#N-1의 줄에 두 점, 그리고 두 점 사이의 거리를 추가한다.
#연결지어야하므로 N1, N2 둘 다에 추가
for _ in range(N-1):
    N1, N2, le = map(int, input().split())
    Tree[N1].append((N2, le))
    Tree[N2].append((N1, le))

#출발 지점과 끝점을 연결하고
#방문노드 여부를 확인해서
#시작점과 끝지점이 일치하기 전까지 q에 시작점과 거리를 추가해나간다.
#일치하면 그 거리를 도출한다.
for _ in range(M):
    s, e = map(int, input().split())
    visited = [0 for _ in range(N+1)]
    visited[s] = 1
    queue = [(s, 0)]
    while queue:
        x, result = queue.pop(0)
        if x == e:
            print(result)
            break
        for y, plus in Tree[x]:
            if not visited[y]:
                #방문체크
                visited[y] = 1
                queue.append([y, result + plus])