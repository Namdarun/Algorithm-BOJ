#BOJ1284_집주소_B3
#https://www.acmicpc.net/problem/1284

while True:
    n = input()
    check = 1
    if n == '0':
        break
    for i in n:
        if i == '0':
            check += 4
        elif i == '1':
            check += 2
        else:
            check += 3
        check += 1
    print(check)
    