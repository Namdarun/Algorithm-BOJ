#G4_BOJ9663_N-Queen
#https://www.acmicpc.net/problem/9663
#백트래킹

#20230924 복습, 풀이 다시 해야함

import sys
input = sys.stdin.readline
# 입력값을 아래에 두면 무조건 시간초과난다...?
N = int(input().rstrip())
row = [0] * N
result = 0

#퀸 가능 여부 찾는 함수
def possible(x):
    #인덱스가 행  row[n]값이 열
    for i in range(x):
        # 열이 같거나 대각선이 같으면 false
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
            return False # 대각선이 같은경우는 두 좌표에서 행 - 행 = 열 - 열 이 같으면 두개는 같은 대각선상에 있다.
    return True

#한줄씩 재귀하며 dfs 실행
def dfs(x):
    global result
 
    if x == N:
        result += 1
        return
    else:
        # 각 행에 퀸 놓기
        # i 는 열번호 0부터 N 전까지 옮겨가면서 유망한곳 찾기
        for i in range(N):
            row[x] = i
            # 행,열,대각선 체크함수 true이면 백트래킹 안하고 다음으로 넘어가기
            if possible(x): 
                dfs(x + 1)
 
dfs(0)
print(result)

#BOJ9663_N-Queen
#시간초과 버전 
#세로, 가로, 대각선이 겹치지 않는 곳에 놓아야 함
# def dfs(queen, row, n):
#     global count
#     count = 0
#     if n == row:
#         return 1
#     for col in range(n):
#         queen[row] = col
#         for i in range(row):
#             if queen[i] == queen[row]:
#                 break
#             if abs(queen[i]-queen[row]) == row - i:
#                 break
#         else:
#             count += dfs(queen, row + 1, n)
#     return count

# def solution(n):
#     return dfs([0]*n,0, n)

# N= int(input())
# dfs([0]*N, 0, N)
# print(count)