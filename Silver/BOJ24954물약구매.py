#BOJ24954물약구매
import sys
from itertools import permutations
input = sys.stdin.readline

#arr에 값들을 추가해준다
N = int(input())
price = list(map(int, input().split()))
arr = [[] for _ in range(N)]

for i in range(N):
    dc = int(input())
    for _ in range(dc):
        arr[i].append(list(map(int, input().split())))

#조합을 만들고
num = permutations(range(0,N), N)
#무한값 설정
result = float("inf")

#num 조합을 돌며
for i in num:
    #바꿔줄 변수
    save = price[:]
    #비교할 최솟값 / 
    cost = 0
    for j in i:
        cost += save[j]
        #2차원 배열을 돌면서 물약값을 변경시켜준다(최소 1은 포함되게)
        for k,s in arr[j]:
            save[k-1] = max(1, save[k-1]-s)
    #최솟값 도출 
    result = min(result, cost)   

print(result)