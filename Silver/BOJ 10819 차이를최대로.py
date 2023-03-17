#BOJ10819_차이를최대로_S2
#https://www.acmicpc.net/problem/10819

from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

#arr로 만들 수 있는 가능한 순열조합 
per = permutations(arr)
result = 0

#가능한 순열들을 뽑아서 s에 저장해나간다
for i in per:
    s = 0
    for j in range(len(i)-1):
        #입력값에 -가 포함되어 있으므로 절대값으로 구한다
        s += abs(i[j]-i[j+1])
    #최댓값 갱신 
    if s > result:
        result = s

print(result)