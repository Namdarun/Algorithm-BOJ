#BOJ9085_더하기_B3
#https://www.acmicpc.net/problem/9085

n = int(input())
for i in range(n):
    case = int(input())
    num = list(map(int, input().split()))
    print(sum(num))
    
    