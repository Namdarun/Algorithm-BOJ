#BOJ2630_색종이만들기_S2
#https://www.acmicpc.net/problem/2630
#4분면을 확인후 재귀돌리기
import sys
input = sys.stdin.readline

N = int(input())
PAPER = [list(map(int, input().split())) for _ in range(N)]
white, blue = 0, 0

def traversal(x, y, N):
    global white, blue
    color = PAPER[x][y]
    for row in range(x, x + N):
        for col in range(y, y + N):
            if color != PAPER[row][col]:
                # 각각 1, 2, 3, 4분면 이동해서 재귀돌리기
                traversal(x, y, N // 2)
                traversal(x, y + N // 2, N // 2)
                traversal(x + N // 2, y, N // 2)
                traversal(x + N // 2, y + N // 2, N // 2)
                return 0
    # 모든 범위 내애 종이 색깔이 같다면
    if color == 0:
        white += 1
    else:
        blue += 1


traversal(0, 0, N)
print(white)
print(blue)