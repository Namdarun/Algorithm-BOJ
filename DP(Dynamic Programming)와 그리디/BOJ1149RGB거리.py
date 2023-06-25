# #BOJ1149_RGB거리_S1
# #https://www.acmicpc.net/problem/1149

# # 1차원 배열로 받고, 색을 다 다르게 칠하는 최솟값
# # 입력값 
# n = int(input())
# home = []
# for i in range(n):
#     home.append(list(map(int, input().split())))
# #나머지 두개의 색 비용 중 최솟값을 가져옴
# for i in range(1, len(home)):
#     home[i][0] = min(home[i-1][1], home[i-1][2]) + home[i][0]
#     # print(home[i][0])
#     home[i][1] = min(home[i-1][0], home[i-1][2]) + home[i][1]
#     # print(home[i][1])
#     home[i][2] = min(home[i-1][0], home[i-1][1]) + home[i][2]
#     # print(home[i][2])
# print(min(home[-1]))


#새로운 풀이
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 비용을 저장해서 재사용
for i in range(1, n):
    arr[i][0] += min(arr[i-1][1], arr[i-1][2])
    arr[i][1] += min(arr[i-1][0], arr[i-1][2])
    arr[i][2] += min(arr[i-1][0], arr[i-1][1])

# 메모이제이션으로 마지막열에서 가장 최소값이 답
print(min(arr[-1]))