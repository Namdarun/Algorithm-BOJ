#BOJ2631_줄세우기_G4
#https://www.acmicpc.net/problem/2631

#전형적인 dp문제 

import sys
input = sys.stdin.readline

n = int(input())

#인덱스 참고
dp = [1]*(n+1)
num = [0]
for i in range(n):
    num.append(int(input()))

#점화식 
#줄을 세우다 = 오름차순 = 계속 갱신해가면서 추가해준다
for i in range(1,n+1):
    for j in range(1,i):
        if num[j]<num[i]:
            dp[i]=max(dp[i],dp[j]+1)

#n- 긴 증가하는 부분수열의 길이 
print(n-max(dp))