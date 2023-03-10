#BOJ11726_2XN 타일링
#https://www.acmicpc.net/problem/11726

#input 최소화
import sys
input = sys.stdin.readline

#dp 설계 
def tile(n):
    #n이 1000이하이므로 인덱스포함 1001
	dp = [0] * 1001
	dp[1] = 1
	dp[2] = 2

    #점화식
	for i in range(3, n+1):
		dp[i] = dp[i - 1] + dp[i - 2]
	return dp[n]

#입력 및 결과
n = int(input())
print(tile(n) % 10007)