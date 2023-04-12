#BOJ2725_보이는점의개수_S2
#https://www.acmicpc.net/problem/2725

# 기울기가 다른 것들을 모두 골라야 함
#분자와 분모의 최대공약수가 1인 것들(기울기가 다를 수밖에 없음)
import sys
input = sys.stdin.readline

def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b 

#보이는 점들을 나타낼 표
chart = [0 for _ in range(1001)]
#총 3개로 뻗어나감
chart[1] = 3
# 그 이후부터
for i in range(2, 1001):
    cnt = 0
    for j in range(1, i+1):
        #i와 j가 같으면 기울기가 같음 = 보이지 않음
        if i == j:
            continue
        #최대공약수가 1이면 가운데선을 기준으로 양옆으로 2개씩 증가
        if gcd(i, j) == 1:
            cnt += 2
    #표에 이전값들을 더해나감
    chart[i] = chart[i-1] + cnt
    
c = int(input())
for k in range(c):
    n = int(input())
    #차트 안에 gcd가 존재
    print(chart[n])
