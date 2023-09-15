#BOJ28278_스텍2_S4
#https://www.acmicpc.net/problem/28278

#3일때만 주의하고, 나머지는 그냥 삼항연산자로 구현함 

import sys
input = sys.stdin.readline
stack = []
n = int(input())
for _ in range(n):
    arr = list(map(int, input().split()))

    if arr[0] == 1:
        stack.append(arr[1])
    elif arr[0] == 2:
        print(stack.pop() if stack else -1)
    elif arr[0] == 3:
        print(len(stack))
    elif arr[0] == 4:
        print(0 if stack else 1)
    else:
        print(stack[-1] if stack else -1)