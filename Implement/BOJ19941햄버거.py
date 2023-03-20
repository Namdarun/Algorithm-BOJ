#BOJ19941_햄버거 분배 
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
PH = list(input())

count = 0
#리스트를 돌며 P일때 K 범위만큼을 보는데, 
#N 범위 안에서 H를 count로 세고, 카운트
for i in range(len(PH)):
    if PH[i] == "P":
        for j in range(i-K, i+K+1):
            if 0 <= j < N and PH[j] == "H":
                count += 1
                PH[j] = '.'
                break

print(count)