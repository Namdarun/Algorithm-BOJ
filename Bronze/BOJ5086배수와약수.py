#BOJ5086_배수와약수_B3
#https://www.acmicpc.net/problem/5086

#단순구현이다.
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if b % a == 0:
        print('factor')
    elif a % b == 0:
        print('multiple')
    else:
        print('neither')