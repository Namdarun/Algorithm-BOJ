#BOJ3273_두 수의 합_B3
#https://www.acmicpc.net/problem/3273

import sys
input = sys.stdin.readline

#배열하고 정렬
n = int(input())
arr = list(map(int, input().split()))
what = int(input())
arr.sort()

#what보다 작을 경우 두 값을 합을 늘림
#what일 경우 결과를 1 증가
#what보다 클 경우 오른쪽을 줄인다
left, right = 0, n-1
result = 0

while left < right:
    check = arr[left] + arr[right]
    if check == what:
        result += 1

    if check < what:
        left += 1
        continue
    right -= 1

print(result)