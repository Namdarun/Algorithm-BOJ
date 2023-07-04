#BOJ9656_돟게임2_S4
#https://www.acmicpc.net/problem/9656

#점화식만 다르게 하거나, 창영과 상근의 순서를 바꾸거나 둘 중에 하나를 택하면 된다
import sys
input = sys.stdin.readline

n = int(input())
dp=[0]*1001
dp[1] = 0
dp[2] = 1
dp[3] = 0

for i in range(4, 1001):
    if dp[i-1] == 1 or dp[i-3] == 1:
        dp[i] = 0
    else:
        dp[i] = 1

if dp[n] == 1:
    print('SK')
else:
    print('CY')