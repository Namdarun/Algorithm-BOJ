#BOJ1654_랜선자르기_S2
#https://www.acmicpc.net/problem/1654

import sys
input = sys.stdin.readline

k, n = map(int, input().split())

#이미 가지고 있는 k개의 랜선 개수
seon = []
for i in range(k):
    seon.append(int(input()))

seon.sort()
start = 1
end = max(seon)

# start가 end보다 작은 동안
# 잘라진 랜선 개수가 n보다 많으면 그 아래로는 볼 필요가 없다
while (start <= end):
    mid = (start + end) // 2
    cnt = 0
    # 핵심
    for i in range(k):
        cnt += seon[i] // mid

    # 필요한 랜선의 개수와 cnt를 비교해서 이분탐색 적용
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1

#만들 수 있는 최대의 선 길이
print(end)