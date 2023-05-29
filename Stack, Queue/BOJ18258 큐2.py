#BOJ18258_큐2_S4
#https://www.acmicpc.net/problem/18258

# 조건에 맞는 queue를 이해하자 

import sys
input = sys.stdin.readline

n = int(input())
queue = []
front = 0 
back = -1

for i in range(n):
    #마지막 개행문자까지 넘겨주기
    arr = input()[:-1]
    if arr[0:4] == 'push':
        # 정수를 큐에 넣자
        queue.append(int(arr[5:]))
        back += 1
        # 큐 가장 앞에 있는 정수를 빼고 수 출력
        # 없으면 -1 출력
    elif arr == 'pop':
        if back - front == -1:
            print(-1)
        else:
            print(queue[front])
            front+=1 
    
    # 큐에 들어있는 정수 개수 출력
    elif arr == 'size':
        print(back-front+1)
    
    # 큐가 비어있으면 1, 아니면 0출력
    elif arr=='empty':
        if back - front == -1:
            print(1)
        else:
            print(0)

    # 큐 가장 앞에 있는 정수 출력
    # 없는 경우 -1 출력
    elif arr == 'front':
        if back-front == -1:
            print(-1)
        else:
            print(queue[front])

    # 큐 가장 뒤에 있는 정수 출력 
    # 없으면 -1 출력
    elif arr == 'back':
        if back-front == -1:
            print(-1)
        else:
            print(queue[back])

    # 아무것도 아니면 넘어가기
    else:
        continue