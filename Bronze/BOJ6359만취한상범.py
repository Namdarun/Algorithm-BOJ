#BOJ6359_만취한상범_B2
#https://www.acmicpc.net/problem/6359

for _ in range(int(input())):
    N = int(input())
    count = 0
    rooms = [True for _ in range(N+1)]
    for i in range(1,N+1):
        check = i
        while check <= N:
            if rooms[check]:
                rooms[check] = False
            else:
                rooms[check] = True
            check += i
    for i in range(1,N+1):
        if not rooms[i]:
            count += 1
    print(count)