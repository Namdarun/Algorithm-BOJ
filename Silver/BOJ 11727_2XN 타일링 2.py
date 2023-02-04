#BOJ11727_2XN 타일링 2
#https://www.acmicpc.net/problem/11727

#점화식이 dp의 핵심이다. 2xn 타일링을 조금 꼬면 풀 수 있음
#input 최소화
import sys
input = sys.stdin.readline

#dp 설계
def tile_two(n):
    dp = [0]* 1001
    dp[1] = 1
    dp[2] = 3
    dp[3] = 5

    #점화식
    for i in range(4, n+1):
        dp[i] = dp[i-1] + 2*dp[i-2]

    return dp[n]

#입력
n = int(input())
print(tile_two(n)%10007)