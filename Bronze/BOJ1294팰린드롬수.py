#BOJ1259_팰린드롬
#https://www.acmicpc.net/problem/1259

while True:
    go = input()

    if go=='0':
        break

    ans = 'no'

    if go == go[::-1]:
        ans = 'yes'

    print(ans)


    