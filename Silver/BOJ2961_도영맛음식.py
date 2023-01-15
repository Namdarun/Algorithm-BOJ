#BOJ2961_도영이의 맛있는 음식
#가로로 먼저 신, 쓴 나눠서 담기
# 재료 i개 뽑을 때 리스트 combination으로 만들기 
# 모든 재료를 사용한다 했으니 for문을 통해 신 경우, 쓴 경우 하나씩 탐색하기 
# 신 것은 1로(곱하기) / 쓴 것은 0 (더하기) 
# 절대값으로 최솟값 최신화 해가기 

#itertools패키지, 입력값 최소크기로 받기
import sys, itertools
from itertools import combinations
input = sys.stdin.readline

N = int(input())
sin = []
ssen = []
for _ in range(N):
    a, b = map(int, input().split())
    sin.append(a)
    ssen.append(b)

infi = float("inf")
#인덱스 맞춰주기(1~N까지)
for a in range(1, N+1):
    #중복없이 조합만들기
    li = list(combinations(list(range(N)), a))

    #조합은 2차원배열이다
    for b in li:
        sin_gop = 1
        ssen_hap = 0

        #a갯수만큼 각각 곱과 합 구하기
        for c in range(a):
            sin_gop *= sin[b[c]]
            ssen_hap += ssen[b[c]]

        #동시에 최솟값을 도출한다
        if abs(sin_gop - ssen_hap) < infi:
            infi = abs(sin_gop - ssen_hap)

print(infi)

import sys, itertools
from itertools import combinations
input = sys.stdin.readline
N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

com = []
for i in range(1, N+1):
    com.append(combinations(arr, i))

result = float("inf")
for i in com:
    for j in i:
        sin_gop = 1
        ssen_hap = 0
        for k in j:
            sin_gop *= k[0]
            ssen_hap += k[1]
        result = min(result, abs(sin_gop-ssen_hap))

print(result)