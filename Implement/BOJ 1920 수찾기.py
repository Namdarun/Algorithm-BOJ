#BOJ1920_수찾기_S4
#https://www.acmicpc.net/problem/1920

# 입력
N = int(input())
#set로 받기 
A = set(map(int, input().split()))	
M = int(input())
arr = list(map(int, input().split()))

for i in arr:
    if i in A:
        print(1)
    else:
        print(0)