#BOJ10655_마라톤
import sys
input = sys.stdin.readline
N = int(input())
arr = []
total = 0
min = 0
for i in range(N):
    arr.append(list(map(int, input().split())))
#여기까지 입력(입력을 람다로 받을 수 있을까?)

#풀이 - 각 좌표별 거리 계산
for i in range(1, len(arr)):
    total += abs(arr[i][0] - arr[i-1][0]) + abs(arr[i][1] - arr[i-1][1])

#좌표 목록들 중 1개 생략시 최대거리 구하기 
for i in range(1, (len(arr)-1)):
    left = abs(arr[i][0] - arr[i-1][0]) + abs(arr[i][1] - arr[i-1][1])
    right = abs(arr[i+1][0] - arr[i][0]) + abs(arr[i+1][1] - arr[i][1])
    next = abs(arr[i+1][0] - arr[i-1][0]) + abs(arr[i+1][1] - arr[i-1][1])
    pass_distance = left + right - next
    #최댓값 도출해서 total값에서 빼면 최솟값이 된다
    min = max(pass_distance, min)
    
print(total-min)