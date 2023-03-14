# #BOJ10828_스텍_S4
# #https://www.acmicpc.net/problem/10828
# #그냥 순서대로 구현만 하면 된다

#스택
import sys
stack = []

for i in range(int(sys.stdin.readline())):
    order = sys.stdin.readline().split()
    if order[0] == "push":
        stack.append(order[1])
    if order[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    if order[0] == "size":
        print(len(stack))
    if order[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if order[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])